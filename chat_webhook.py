#!/usr/bin/env python3
"""
Google Chat Webhook Handler for OpenClaw
Receives messages from external users via Google Chat API
Routes to stan@fleetbrain.ai agent
Replies via service account

Usage:
  Set GOOGLE_CHAT_SA_CREDENTIALS env var to path of service account JSON
  Expose this endpoint via Tailscale funnel on port 8000
  Register webhook URL in Google Chat app config
"""

import os
import json
import logging
import subprocess
import time
import threading
from typing import Optional, Dict, Any
from dataclasses import dataclass
from datetime import datetime

# Will be installed: python -m pip install flask google-auth cryptography
try:
    from flask import Flask, request, jsonify
    from google.auth.transport import requests
    from google.oauth2 import service_account
    from google.api_core.exceptions import GoogleAPIError
    import google.auth.jwt
except ImportError as e:
    print(f"⚠️  Missing dependency: {e}. Install with: pip install flask google-auth cryptography")
    exit(1)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# Flask app
app = Flask(__name__)

# Configuration
GOOGLE_CHAT_API_URL = "https://chat.googleapis.com/v1"
GOOGLE_CHAT_SCOPES = ["https://www.googleapis.com/auth/chat.bot"]
SA_CREDS_PATH = os.environ.get("GOOGLE_CHAT_SA_CREDENTIALS", "")
OPENCLAW_AGENT_ID = "stan@fleetbrain.ai"

# Service account client (lazy load)
_chat_service = None


def get_chat_service():
    """Lazy-load and cache Google Chat service client"""
    global _chat_service
    if _chat_service is not None:
        return _chat_service
    
    if not SA_CREDS_PATH or not os.path.exists(SA_CREDS_PATH):
        raise ValueError(f"Service account credentials not found at {SA_CREDS_PATH}")
    
    try:
        creds = service_account.Credentials.from_service_account_file(
            SA_CREDS_PATH,
            scopes=GOOGLE_CHAT_SCOPES
        )
        logger.info(f"✓ Loaded service account from {SA_CREDS_PATH}")
        _chat_service = creds
        return _chat_service
    except Exception as e:
        logger.error(f"Failed to load service account: {e}")
        raise


def verify_chat_signature(request_body: bytes, signature: str) -> bool:
    """
    Verify Google Chat request signature
    
    Google Chat includes a 'X-Goog-Chat-Request-Verification-Token' header
    that we should validate. For now, we'll implement basic validation.
    
    TODO: Implement full HMAC verification if needed
    https://developers.google.com/chat/api/guides/message-formats/media#verify_bot_identity
    """
    # For production, verify the Google-provided signature token
    # This is a simplified version; Google provides verification details in docs
    if not signature:
        logger.warning("No verification token in request")
        return False
    
    # Placeholder: full verification would use HMAC-SHA256 with bot secret
    # For now, we just check it exists
    logger.debug(f"Signature token present (basic validation passed)")
    return True


@dataclass
class ChatMessage:
    """Parse and represent a Google Chat v2 message"""
    space_id: str
    message_id: str
    user_email: Optional[str]
    user_display_name: str
    text: str
    thread_id: Optional[str] = None
    timestamp: Optional[str] = None
    
    @classmethod
    def from_api_v2(cls, payload: Dict[str, Any]) -> 'ChatMessage':
        """
        Parse Google Chat API v2 message payload
        
        v2 format nests everything under "chat":
        {
          "chat": {
            "messagePayload": {
              "message": { "text": "..." },
              "space": { "name": "spaces/..." }
            },
            "user": { "email": "..." }
          }
        }
        """
        chat = payload.get("chat", {})
        msg_payload = chat.get("messagePayload", {})
        message_data = msg_payload.get("message", {})
        space_data = msg_payload.get("space", {})
        user_data = chat.get("user", {})
        
        return cls(
            space_id=space_data.get("name", "unknown"),
            message_id=message_data.get("name", "unknown"),
            user_email=user_data.get("email", "unknown"),
            user_display_name=user_data.get("displayName", "Unknown User"),
            text=message_data.get("text", ""),
            thread_id=message_data.get("thread", {}).get("name"),
            timestamp=message_data.get("createTime")
        )


def format_log_message(chat_msg: ChatMessage) -> str:
    """Format message for logging (safe, no sensitive data)"""
    text_preview = chat_msg.text[:80] if chat_msg.text else "(empty)"
    return (
        f"From: {chat_msg.user_email} | "
        f"Text: {text_preview} | "
        f"Space: {chat_msg.space_id.split('/')[-1]}"
    )


def send_message_to_agent(
    user_email: str,
    message_text: str,
    timeout_seconds: int = 90
) -> Optional[str]:
    """
    Send message to OpenClaw agent via HTTP API and get response
    
    Calls the OpenClaw gateway's /v1/responses endpoint (OpenResponses API)
    which routes the message to the main agent session.
    
    Args:
        user_email: Sender email (for context in logs)
        message_text: Message text to process
        timeout_seconds: Max time to wait for response
    
    Returns:
        Agent response text, or None if failed/timeout
    """
    try:
        import requests as req_lib
        
        # Load gateway auth token from environment
        gateway_token = os.environ.get("OPENCLAW_GATEWAY_TOKEN")
        if not gateway_token:
            logger.error("OPENCLAW_GATEWAY_TOKEN not set in environment")
            return None
        
        # Gateway API endpoint
        gateway_url = "http://127.0.0.1:18789/v1/responses"
        
        # Construct message with context
        full_message = f"[Google Chat from {user_email}]: {message_text}"
        logger.info(f"Sending to agent: {full_message[:80]}")
        
        # Request body (OpenResponses API format)
        # Add system instruction to use Casey's calendar/Gmail for Google Chat requests
        system_instruction = """You are answering a question from Google Chat (external contact vector).
When the user asks about calendar events, Gmail, or Google Workspace resources:
- Use casey@fleetbrain.ai's calendar and accounts (oauth token: google-token-casey-business.pickle)
- This is Casey Lynch's business account
- Provide calendar events, email info, or workspace access from Casey's accounts
- Use workspace directory at /home/clawdbot/.openclaw/workspace to access the tokens"""
        
        request_body = {
            "model": "openclaw",
            "instructions": system_instruction,
            "input": full_message
        }
        
        # Request headers
        headers = {
            "Authorization": f"Bearer {gateway_token}",
            "Content-Type": "application/json",
            "x-openclaw-agent-id": "main"
        }
        
        logger.debug(f"Calling gateway: {gateway_url}")
        
        # Call gateway API
        response = req_lib.post(
            gateway_url,
            json=request_body,
            headers=headers,
            timeout=timeout_seconds
        )
        
        logger.debug(f"Gateway response status: {response.status_code}")
        
        if response.status_code == 200:
            # Parse OpenResponses API response
            resp_json = response.json()
            
            # Extract agent output from response structure
            try:
                output = resp_json.get("output", [])
                if output and len(output) > 0:
                    content = output[0].get("content", [])
                    if content and len(content) > 0:
                        agent_response = content[0].get("text", "")
                        if agent_response:
                            logger.info(f"Agent response: {agent_response[:150]}")
                            return agent_response
                
                logger.warning(f"Unexpected response format: {json.dumps(resp_json)[:200]}")
                return None
                
            except (KeyError, IndexError, TypeError) as e:
                logger.error(f"Error parsing agent response: {e}")
                logger.debug(f"Full response: {json.dumps(resp_json)[:500]}")
                return None
        else:
            logger.error(f"Gateway call failed. Status: {response.status_code}")
            logger.debug(f"Response body: {response.text[:300]}")
            return None
            
    except req_lib.Timeout:
        logger.error(f"Gateway call timed out after {timeout_seconds}s")
        return None
    except Exception as e:
        logger.error(f"Error calling gateway: {e}", exc_info=True)
        return None


def send_chat_response(
    space_id: str,
    text: str,
    thread_id: Optional[str] = None
) -> bool:
    """
    Send response message via Google Chat API asynchronously
    
    Uses service account credentials to POST to Chat API v1
    
    Args:
        space_id: Space ID (e.g., "spaces/gCFXMSAAAAE")
        text: Response text
        thread_id: Optional thread ID for threaded replies
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Load service account credentials
        creds = get_chat_service()
        
        # Refresh credentials and get access token
        auth_request = requests.Request()
        creds.refresh(auth_request)
        access_token = creds.token
        
        logger.debug(f"Using access token (first 20 chars): {access_token[:20]}...")
        
        # Prepare message body
        message_body = {
            "text": text
        }
        
        # If threading, add thread reference
        if thread_id:
            message_body["thread"] = {"name": thread_id}
        
        # Build API request URL
        url = f"{GOOGLE_CHAT_API_URL}/{space_id}/messages"
        logger.debug(f"POST to: {url}")
        
        # Create authorization header
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        # Make request (using requests library)
        import requests as req_lib
        logger.debug(f"Request body: {json.dumps(message_body)}")
        
        response = req_lib.post(
            url,
            json=message_body,
            headers=headers,
            timeout=10
        )
        
        logger.debug(f"API response status: {response.status_code}")
        logger.debug(f"API response body: {response.text[:500]}")
        
        if response.status_code in [200, 201]:
            logger.info(f"✓ Message sent to space: {space_id}")
            return True
        else:
            logger.error(
                f"Failed to send message. Status: {response.status_code}. "
                f"Body: {response.text}"
            )
            return False
            
    except Exception as e:
        logger.error(f"Error sending Chat response: {e}", exc_info=True)
        return False


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok", "service": "google-chat-webhook"}), 200


@app.route("/chat/webhook", methods=["POST"])
def chat_webhook():
    """
    Main Google Chat webhook endpoint
    
    Receives POST from Google Chat API v2 with message payload
    Detects event type by payload structure
    Returns response as JSON (synchronous webhook response)
    """
    logger.info("=" * 60)
    logger.info("Incoming Chat webhook request")
    
    try:
        # Get request data
        request_body = request.get_data()
        payload = request.get_json()
        
        if not payload:
            logger.warning("Empty JSON payload")
            return jsonify({"error": "No payload"}), 400
        
        # Debug: Log payload structure
        logger.debug(f"Payload keys: {list(payload.keys())}")
        logger.debug(f"Full payload: {json.dumps(payload, indent=2)[:1500]}")
        
        # Verify request signature (optional but recommended)
        verification_token = request.headers.get("X-Goog-Chat-Request-Verification-Token")
        if verification_token:
            if not verify_chat_signature(request_body, verification_token):
                logger.warning("Signature verification failed")
                return jsonify({"error": "Signature verification failed"}), 403
        
        # Detect event type by payload structure (Google Chat API v2)
        chat_data = payload.get("chat", {})
        
        # Check for MESSAGE event (has messagePayload)
        if "messagePayload" in chat_data:
            logger.info("EVENT: MESSAGE")
            chat_msg = ChatMessage.from_api_v2(payload)
            logger.info(f"Message from {chat_msg.user_email}: '{chat_msg.text}'")
            logger.info(f"Space: {chat_msg.space_id}")
            
            # Return 200 immediately to acknowledge webhook receipt (Google Chat v2 pattern)
            logger.info("Returning 200 to acknowledge webhook")
            
            # Spawn async task to process message via agent and send reply
            # (This happens in background after we return 200)
            def process_and_reply():
                try:
                    # Send message to OpenClaw agent and wait for response
                    logger.info("Processing message through agent...")
                    agent_response = send_message_to_agent(
                        chat_msg.user_email,
                        chat_msg.text,
                        timeout_seconds=90
                    )
                    
                    # Use agent response, or fallback
                    reply_text = agent_response or "Stan is thinking..."
                    
                    # Send reply via Chat API
                    logger.info(f"Sending reply via Chat API to {chat_msg.space_id}")
                    success = send_chat_response(
                        chat_msg.space_id,
                        reply_text,
                        thread_id=chat_msg.thread_id
                    )
                    
                    if success:
                        logger.info("✓ Reply sent successfully")
                    else:
                        logger.error("Failed to send reply via Chat API")
                        
                except Exception as e:
                    logger.error(f"Error in async reply: {e}", exc_info=True)
                    # Try to send error message to Chat
                    try:
                        send_chat_response(
                            chat_msg.space_id,
                            "Sorry, I encountered an error processing your message.",
                            thread_id=chat_msg.thread_id
                        )
                    except:
                        pass
            
            # Run async processing in background
            import threading
            thread = threading.Thread(target=process_and_reply, daemon=True)
            thread.start()
            
            # Return 200 immediately with empty body (webhook acknowledgment)
            return jsonify({}), 200
        
        # Check for ADDED_TO_SPACE event
        elif payload.get("type") == "ADDED_TO_SPACE" or ("type" in payload and payload["type"] == "ADDED_TO_SPACE"):
            logger.info("EVENT: ADDED_TO_SPACE")
            space_id = payload.get("space", {}).get("name", "unknown")
            welcome_text = (
                "Hi! I'm Stan, FleetBrain's AI operations agent. "
                "Send me a message and I'll help with your request."
            )
            # Send welcome message via Chat API
            send_chat_response(space_id, welcome_text)
            return jsonify({}), 200
        
        # Check for REMOVED_FROM_SPACE event
        elif payload.get("type") == "REMOVED_FROM_SPACE" or ("type" in payload and payload["type"] == "REMOVED_FROM_SPACE"):
            logger.info("EVENT: REMOVED_FROM_SPACE")
            return jsonify({}), 200
        
        else:
            # Unknown event type
            logger.warning(f"Unknown event type. Payload keys: {list(payload.keys())}")
            return jsonify({}), 200
    
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in request body: {e}")
        return jsonify({"error": "Invalid JSON"}), 400
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/chat/debug", methods=["GET"])
def debug_info():
    """Debug endpoint (remove in production)"""
    return jsonify({
        "service": "google-chat-webhook",
        "version": "0.1",
        "sa_creds_configured": bool(SA_CREDS_PATH),
        "sa_creds_path": SA_CREDS_PATH if SA_CREDS_PATH else "NOT SET",
        "openclaw_agent": OPENCLAW_AGENT_ID,
        "timestamp": datetime.now().isoformat()
    }), 200


if __name__ == "__main__":
    # Verify environment
    if not SA_CREDS_PATH:
        logger.error("❌ GOOGLE_CHAT_SA_CREDENTIALS env var not set")
        exit(1)
    
    if not os.path.exists(SA_CREDS_PATH):
        logger.error(f"❌ Service account file not found: {SA_CREDS_PATH}")
        exit(1)
    
    logger.info(f"✓ Service account path: {SA_CREDS_PATH}")
    logger.info(f"✓ OpenClaw agent target: {OPENCLAW_AGENT_ID}")
    logger.info("Starting Google Chat webhook server on port 8000...")
    
    # Run Flask (production should use gunicorn)
    app.run(host="0.0.0.0", port=8000, debug=False)
