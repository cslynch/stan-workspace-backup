## OpenClaw Update Available

Version: 2026.2.15 (current: 2026.2.6)
Released: February 16, 2026
Status: Stable Release

Relevant changes:

**Security Hardening (Critical):**
- SHA-1 → SHA-256 sandbox configuration hashing for deterministic cache identity
- Telegram bot token redaction from error logs/stack traces (prevents credential leakage)
- Dangerous sandbox Docker config blocked (bind mounts, host networking, unconfined seccomp/apparmor)
- Gateway/Session: Redact sensitive session/path details from status responses for non-admin clients
- Config/Gateway: Case-insensitive sensitive-key whitelist matching (prevents accidental redaction of non-secrets)
- Gateway/Agent: Reject malformed agent:-prefixed session keys (prevents accidental cross-session routing)
- Gateway/Chat: Harden inbound message handling (reject null bytes, strip unsafe control characters, normalize Unicode to NFC)
- Agents: Sanitize workspace paths before LLM prompts (prevent instruction injection via malicious directory names)
- Skills: Restrict download installer targetDir to per-skill tools directory (prevent arbitrary file writes)
- Web Fetch: Cap downloaded response body size before parsing (prevent memory exhaustion)

**Telegram-Specific Fixes:**
- Media handling: Retry getFile calls with backoff; fallback gracefully on transient errors
- Replace inbound media placeholders with successful voice transcripts
- Omit message_thread_id for DM sends (fix "400 Bad Request: message thread not found")
- Finalize streaming preview replies in-place (prevent duplicate outputs)
- Disable block streaming when streamMode is off

**Gateway/Cron Infrastructure:**
- Cron/Gateway: Add webhook delivery toggle (notify) + dedicated webhook auth token support
- Gateway/Control UI: Preserve operator scopes for bypass modes when device identity unavailable
- Gateway/Send: Return actionable error when targeting internal-only webchat

**Additional:**
- Slack/Discord/Telegram: Per-channel ack reaction overrides support
- Subagents: Nested sub-agents (sub-sub-agents) with configurable spawn depth

Recommendation: **UPDATE**

Rationale: Major security hardening across gateway, session handling, credential management, and Telegram operations. Includes critical sandbox/Docker escape prevention and credential leakage fixes. No breaking changes in release notes.
