#!/usr/bin/env python3
"""
Contact CRM Daily Update — Pull emails from last 24h, extract contacts, score, merge.
Uses service account (stan-chat-app-key.json) with Gmail, Calendar, Drive scopes.
"""

import json
import os
import pickle
from datetime import datetime, timedelta
from email.utils import parseaddr
from collections import defaultdict

# Google APIs
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
SERVICE_ACCOUNT_FILE = '/home/clawdbot/.openclaw/credentials/fleetbrain-stan-prod-534550cd7a84.json'
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/drive',
]

GMAIL_ACCOUNTS = [
    'casey@fleetbrain.ai',
    'cslynch@gmail.com',
]

CONTACTS_DRIVE_FILE_ID = '13oK-rqfG94nW3RNtcCBuuB1rESOk_rGe'

# Contact exclusions (regex patterns)
EXCLUDE_PATTERNS = [
    'noreply@',
    'notifications@',
    'newsletters@',
    'receipts@',
    'shipping@',
    'promotional@',
    'facebook',
    'no-reply',
]

def get_oauth_credentials():
    """Load user OAuth token from pickle cache."""
    token_path = '/home/clawdbot/.openclaw/credentials/google-token.pickle'
    try:
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
        
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            # Save refreshed token
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)
            print(f"✓ Refreshed and loaded OAuth token from {token_path}")
        else:
            print(f"✓ Loaded OAuth token from {token_path}")
        
        return creds
    except Exception as e:
        print(f"✗ Failed to load credentials: {e}")
        return None

def should_exclude_contact(email):
    """Check if contact should be excluded."""
    email_lower = email.lower()
    for pattern in EXCLUDE_PATTERNS:
        if pattern in email_lower:
            return True
    return False

def extract_emails_from_headers(headers):
    """Extract email addresses from message headers."""
    emails = set()
    for header_name in ['From', 'To', 'Cc', 'Bcc']:
        if header_name in headers:
            addresses = headers[header_name].split(',')
            for addr in addresses:
                name, email = parseaddr(addr.strip())
                if email and not should_exclude_contact(email):
                    emails.add(email.lower())
    return emails

def fetch_emails_last_24h(gmail_service, account_email):
    """Fetch emails from last 24 hours for a given Gmail account."""
    try:
        # Calculate 24h ago timestamp
        twenty_four_hours_ago = datetime.utcnow() - timedelta(hours=24)
        query_date = twenty_four_hours_ago.strftime('%Y/%m/%d')
        query = f'after:{query_date}'
        
        print(f"\n📧 Fetching emails from {account_email} (last 24h)...")
        
        results = gmail_service.users().messages().list(
            userId='me',
            q=query,
            maxResults=50
        ).execute()
        
        messages = results.get('messages', [])
        print(f"  Found {len(messages)} messages")
        
        contacts = set()
        for msg in messages:
            try:
                msg_data = gmail_service.users().messages().get(
                    userId='me',
                    id=msg['id'],
                    format='metadata'
                ).execute()
                
                headers = {h['name']: h['value'] for h in msg_data.get('payload', {}).get('headers', [])}
                extracted = extract_emails_from_headers(headers)
                contacts.update(extracted)
                
            except Exception as e:
                print(f"  ⚠ Error processing message {msg['id']}: {e}")
                continue
        
        print(f"  Extracted {len(contacts)} unique contacts")
        return contacts
        
    except HttpError as e:
        print(f"  ✗ Gmail API error: {e}")
        return set()

def fetch_calendar_contacts(calendar_service):
    """Extract contacts from calendar events (organizers, attendees)."""
    try:
        print(f"\n📅 Fetching calendar contacts...")
        
        # Get events from today and tomorrow
        now = datetime.utcnow().isoformat() + 'Z'
        tomorrow = (datetime.utcnow() + timedelta(days=1)).isoformat() + 'Z'
        
        results = calendar_service.events().list(
            calendarId='primary',
            timeMin=now,
            timeMax=tomorrow,
            maxResults=50
        ).execute()
        
        events = results.get('items', [])
        print(f"  Found {len(events)} events")
        
        contacts = set()
        for event in events:
            # Get organizer
            if 'organizer' in event:
                email = event['organizer'].get('email', '')
                if email and not should_exclude_contact(email):
                    contacts.add(email.lower())
            
            # Get attendees
            for attendee in event.get('attendees', []):
                email = attendee.get('email', '')
                if email and not should_exclude_contact(email):
                    contacts.add(email.lower())
        
        print(f"  Extracted {len(contacts)} unique contacts")
        return contacts
        
    except HttpError as e:
        print(f"  ⚠ Calendar API not available or error: {e}")
        return set()

def load_contacts_from_drive(drive_service):
    """Download contacts.json from Drive."""
    try:
        print(f"\n☁️  Loading contacts.json from Drive...")
        
        request = drive_service.files().get_media(fileId=CONTACTS_DRIVE_FILE_ID)
        content = request.execute()
        contacts_data = json.loads(content.decode('utf-8'))
        
        print(f"  ✓ Loaded {len(contacts_data.get('contacts', []))} existing contacts")
        return contacts_data
        
    except HttpError as e:
        print(f"  ⚠ Could not load from Drive: {e}")
        print(f"  Creating new contacts database...")
        return {
            'meta': {
                'created': datetime.utcnow().isoformat(),
                'last_updated': datetime.utcnow().isoformat(),
            },
            'contacts': []
        }

def score_contact(email, existing_contacts):
    """Calculate interaction score for a contact."""
    # Base score: 1 per interaction
    # Multipliers:
    # - 1.5x if domain is @fleetbrain.ai (internal)
    # - 1.0x for other domains
    # - Decay: -0.1 per week since last interaction
    
    base_score = 1.0
    
    if email.endswith('@fleetbrain.ai'):
        base_score *= 1.5
    
    # Find existing contact entry
    for contact in existing_contacts.get('contacts', []):
        if contact.get('email') == email:
            # Has previous interactions; boost score
            base_score *= 1.2
            break
    
    return base_score

def merge_and_save_contacts(drive_service, new_emails, existing_contacts):
    """Merge new emails into existing contacts and update Drive."""
    
    print(f"\n🔄 Merging {len(new_emails)} new emails with existing contacts...")
    
    # Create a map of existing contacts by email
    contact_map = {c['email']: c for c in existing_contacts.get('contacts', [])}
    
    # Add/update contacts
    added = 0
    updated = 0
    for email in new_emails:
        score = score_contact(email, existing_contacts)
        
        if email in contact_map:
            # Update existing
            contact_map[email]['last_interaction'] = datetime.utcnow().isoformat()
            contact_map[email]['interaction_count'] = contact_map[email].get('interaction_count', 0) + 1
            contact_map[email]['score'] = contact_map[email].get('score', 0) + score
            updated += 1
        else:
            # Add new
            contact_map[email] = {
                'email': email,
                'first_interaction': datetime.utcnow().isoformat(),
                'last_interaction': datetime.utcnow().isoformat(),
                'interaction_count': 1,
                'score': score,
                'tags': []
            }
            added += 1
    
    # Sort by score descending and keep top 3
    sorted_contacts = sorted(contact_map.values(), key=lambda x: x.get('score', 0), reverse=True)
    top_3 = sorted_contacts[:3]
    
    # Update metadata
    existing_contacts['contacts'] = list(contact_map.values())
    existing_contacts['meta']['last_updated'] = datetime.utcnow().isoformat()
    existing_contacts['meta']['last_update_added'] = added
    existing_contacts['meta']['last_update_updated'] = updated
    existing_contacts['meta']['top_3'] = [c['email'] for c in top_3]
    
    print(f"  Added: {added} | Updated: {updated} | Total: {len(contact_map)}")
    print(f"  Top 3 by score: {[c['email'] for c in top_3]}")
    
    # Save back to Drive
    try:
        file_metadata = {'name': 'contacts.json'}
        media = drive_service.files().update(
            fileId=CONTACTS_DRIVE_FILE_ID,
            media_body=None,
            body={
                'mimeType': 'application/json',
            },
            fields='id'
        ).execute()
        
        # Actually upload content
        from googleapiclient.http import MediaFileUpload
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(existing_contacts, f, indent=2)
            temp_file = f.name
        
        media = MediaFileUpload(temp_file, mimetype='application/json')
        drive_service.files().update(
            fileId=CONTACTS_DRIVE_FILE_ID,
            media_body=media
        ).execute()
        
        os.unlink(temp_file)
        
        print(f"  ✓ Saved to Drive")
        
    except HttpError as e:
        print(f"  ✗ Failed to save to Drive: {e}")
        return False
    
    return existing_contacts

def main():
    print("=" * 60)
    print("Contact CRM Daily Update — " + datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'))
    print("=" * 60)
    
    # Get credentials
    creds = get_oauth_credentials()
    if not creds:
        print("✗ Failed to initialize. Exiting.")
        return
    
    # Initialize services
    gmail_service = build('gmail', 'v1', credentials=creds)
    calendar_service = build('calendar', 'v3', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
    # Collect all contacts from all sources
    all_contacts = set()
    
    # Gmail accounts
    for account in GMAIL_ACCOUNTS:
        try:
            # For service account, we can only access our own email
            # This script assumes running as stan@fleetbrain.ai
            emails = fetch_emails_last_24h(gmail_service, account)
            all_contacts.update(emails)
        except Exception as e:
            print(f"✗ Error fetching {account}: {e}")
    
    # Calendar
    cal_contacts = fetch_calendar_contacts(calendar_service)
    all_contacts.update(cal_contacts)
    
    # Load existing contacts from Drive
    existing = load_contacts_from_drive(drive_service)
    
    # Merge and save
    if all_contacts:
        updated = merge_and_save_contacts(drive_service, all_contacts, existing)
        
        print("\n" + "=" * 60)
        print("✓ Contact CRM Daily Update Complete")
        print("=" * 60)
        print(f"Total contacts: {len(updated['contacts'])}")
        print(f"Top 3 by score: {updated['meta'].get('top_3', [])}")
        
    else:
        print("\n⚠ No contacts found to process.")

if __name__ == '__main__':
    main()
