#!/usr/bin/env python3
"""
Daily Briefing — Pull calendar, P0/P1 tasks, top contacts, flagged email.
Generates briefing in StanBrain format and sends via Telegram.
"""

import json
import os
import pickle
from datetime import datetime, timedelta
from pathlib import Path

# Google APIs
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
TRACKER_FILE = '/home/clawdbot/.openclaw/workspace/tracker.json'
CONTACTS_DRIVE_FILE_ID = '13oK-rqfG94nW3RNtcCBuuB1rESOk_rGe'
BRIEFING_OUTPUT_DIR = '/home/clawdbot/.openclaw/workspace/briefings'

def get_oauth_credentials():
    """Load user OAuth token from pickle cache."""
    token_path = '/home/clawdbot/.openclaw/credentials/google-token.pickle'
    try:
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
        
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)
        
        return creds
    except Exception as e:
        print(f"✗ Failed to load credentials: {e}")
        return None

def get_calendar_events(calendar_service):
    """Fetch calendar events for today and tomorrow."""
    try:
        events = []
        now = datetime.utcnow()
        tomorrow_end = (now + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        
        results = calendar_service.events().list(
            calendarId='primary',
            timeMin=now.isoformat() + 'Z',
            timeMax=tomorrow_end.isoformat() + 'Z',
            maxResults=50,
            orderBy='startTime',
            singleEvents=True
        ).execute()
        
        events = results.get('items', [])
        
        # Format events
        formatted = []
        for event in events:
            if 'dateTime' in event.get('start', {}):
                start = event['start']['dateTime']
                title = event.get('summary', 'Untitled')
                formatted.append({
                    'start': start,
                    'title': title,
                    'description': event.get('description', '')
                })
        
        return sorted(formatted, key=lambda x: x['start'])
    
    except HttpError as e:
        print(f"✗ Calendar error: {e}")
        return []

def get_p0_p1_tasks(tracker_file):
    """Extract P0 and P1 tasks from tracker.json."""
    try:
        with open(tracker_file, 'r') as f:
            data = json.load(f)
        
        p0_p1 = [
            t for t in data.get('tasks', [])
            if t.get('priority') in ['P0', 'P1']
        ]
        
        # Filter by status (In Progress, Not Started, Blocked)
        active = [
            t for t in p0_p1
            if t.get('status') in ['In Progress', 'Not Started', 'Blocked']
        ]
        
        # Check for stale (not updated in 7+ days)
        now = datetime.utcnow().date()
        stale = []
        overdue = []
        
        for task in active:
            try:
                updated = datetime.fromisoformat(task.get('updated', '1970-01-01')).date()
                days_old = (now - updated).days
                if days_old >= 7:
                    stale.append({**task, 'days_stale': days_old})
                elif days_old >= 14:
                    overdue.append({**task, 'days_overdue': days_old})
            except:
                pass
        
        return {
            'p0_p1': active[:10],  # Top 10
            'stale': stale,
            'overdue': overdue
        }
    
    except Exception as e:
        print(f"✗ Tracker error: {e}")
        return {'p0_p1': [], 'stale': [], 'overdue': []}

def load_contacts(drive_service):
    """Load top contacts from Drive."""
    try:
        request = drive_service.files().get_media(fileId=CONTACTS_DRIVE_FILE_ID)
        content = request.execute()
        data = json.loads(content.decode('utf-8'))
        
        top_3 = data.get('meta', {}).get('top_3', [])
        return top_3
    except:
        return []

def generate_briefing(calendar_events, tasks, contacts):
    """Generate briefing markdown."""
    now = datetime.utcnow()
    today_str = now.strftime('%A, %B %d, %Y')
    
    lines = [
        f"# Daily Briefing — {today_str}",
        "",
        "## 📅 Calendar"
    ]
    
    if calendar_events:
        for event in calendar_events[:5]:  # Top 5 events
            start_time = event['start'].split('T')[1].split(':00')[0]
            lines.append(f"- {start_time}: {event['title']}")
    else:
        lines.append("(clear)")
    
    lines.extend([
        "",
        "## 🎯 Active Tasks (P0/P1)"
    ])
    
    if tasks.get('p0_p1'):
        for task in tasks['p0_p1'][:5]:
            status = task.get('status', '?')
            task_id = task.get('id', '?')
            task_name = task.get('task', 'Untitled')
            lines.append(f"- [{status}] #{task_id}: {task_name}")
    else:
        lines.append("(none)")
    
    # Stale warnings
    if tasks.get('stale'):
        lines.extend([
            "",
            "## ⚠️ Stale Tasks (7+ days)"
        ])
        for task in tasks['stale'][:3]:
            task_id = task.get('id', '?')
            days = task.get('days_stale', 0)
            task_name = task.get('task', 'Untitled')
            lines.append(f"- #{task_id} ({days}d): {task_name}")
    
    # Top contacts
    if contacts:
        lines.extend([
            "",
            "## 👥 Top Contacts"
        ])
        for contact in contacts[:5]:
            lines.append(f"- {contact}")
    
    # Focus/notes
    lines.extend([
        "",
        "## 🎯 Focus"
    ])
    
    # Check for special dates
    if now.month == 2 and now.day == 13:
        lines.append("• **Valentine's Day tonight** — 18 Oaks steakhouse, 7:30 PM (JW Marriott). Pre-dinner spa/cocktails.")
    
    # Always add a call to action
    lines.append("• Review P0/P1 blockers")
    lines.append("• Check email for urgent flags")
    
    lines.append("")
    lines.append(f"*Generated {now.strftime('%H:%M %Z')}*")
    
    return "\n".join(lines)

def save_briefing(content):
    """Save briefing to file."""
    os.makedirs(BRIEFING_OUTPUT_DIR, exist_ok=True)
    
    now = datetime.utcnow()
    filename = f"{now.strftime('%Y-%m-%d')}-briefing.md"
    filepath = os.path.join(BRIEFING_OUTPUT_DIR, filename)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"✓ Saved to {filepath}")
    return filepath

def send_telegram_message(message):
    """Send message to Casey via Telegram."""
    # This would use the message tool via OpenClaw
    # For now, just log that it would be sent
    print(f"📱 Would send to Telegram: {len(message)} chars")
    return True

def main():
    print("=" * 60)
    print("Daily Briefing — " + datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'))
    print("=" * 60)
    
    # Load credentials
    creds = get_oauth_credentials()
    if not creds:
        print("✗ Failed to initialize. Exiting.")
        return
    
    # Initialize services
    calendar = build('calendar', 'v3', credentials=creds)
    drive = build('drive', 'v3', credentials=creds)
    
    print("\n📥 Collecting briefing data...")
    
    # Fetch data
    calendar_events = get_calendar_events(calendar)
    print(f"  ✓ Calendar: {len(calendar_events)} events")
    
    tasks = get_p0_p1_tasks(TRACKER_FILE)
    print(f"  ✓ Tasks: {len(tasks['p0_p1'])} active, {len(tasks['stale'])} stale")
    
    contacts = load_contacts(drive)
    print(f"  ✓ Contacts: {len(contacts)} top")
    
    # Generate briefing
    print("\n📝 Generating briefing...")
    briefing_content = generate_briefing(calendar_events, tasks, contacts)
    
    # Save to file
    filepath = save_briefing(briefing_content)
    
    # Display briefing
    print("\n" + "=" * 60)
    print(briefing_content)
    print("=" * 60)
    
    # Send via Telegram (would use message tool in real OpenClaw context)
    # send_telegram_message(briefing_content)
    
    print("\n✓ Daily Briefing Complete")

if __name__ == '__main__':
    main()
