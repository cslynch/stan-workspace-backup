#!/usr/bin/env python3
"""
Daily Briefing — Pull calendar, P0/P1 tasks, top contacts, flagged email.
Generates briefing and sends via Telegram.

v2.2 — Tasks now sourced from SupaBrain (brain-api) instead of tracker.json.
        Removes last live consumer of tracker.json.
        Falls back to tracker.json if brain-api is unreachable.
"""

import json
import os
import pickle
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Google APIs
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
TRACKER_FILE = '/home/clawdbot/.openclaw/workspace/tracker.json'  # fallback only
CONTACTS_DRIVE_FILE_ID = '13oK-rqfG94nW3RNtcCBuuB1rESOk_rGe'
BRIEFING_OUTPUT_DIR = '/home/clawdbot/.openclaw/workspace/briefings'
BRAIN_API_URL = os.environ.get('BRAIN_API_URL', 'https://olmaksvjanknqzndalzv.supabase.co/functions/v1/brain-api')
BRAIN_API_SECRET = os.environ.get('BRAIN_API_SECRET', '')

# SupaBrain status values → display labels
STATUS_DISPLAY = {
    'not_started': 'Not Started',
    'in_progress': 'In Progress',
    'blocked': 'Blocked',
    'done': 'Done',
    'closed': 'Closed',
    'parked': 'Parked',
}

ACTIVE_STATUSES_SUPABRAIN = ('not_started', 'in_progress', 'blocked')
ACTIVE_STATUSES_TRACKER = ('Not Started', 'In Progress', 'Blocked')


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


def _fetch_supabrain_tasks(priority):
    """Fetch tasks from brain-api for a given priority. Returns list or None on failure."""
    import requests as req_lib

    try:
        resp = req_lib.post(
            BRAIN_API_URL,
            json={
                "action": "tasks",
                "filter_priority": priority,
                "count": 25,
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {BRAIN_API_SECRET}",
            },
            timeout=15,
        )
        if resp.status_code != 200:
            print(f"  ⚠ brain-api tasks returned {resp.status_code} for {priority}")
            return None

        data = resp.json()
        return data.get("tasks", [])
    except Exception as e:
        print(f"  ⚠ brain-api tasks error for {priority}: {e}")
        return None


def _normalize_supabrain_task(task):
    """Normalize a SupaBrain task dict to the format generate_briefing() expects."""
    display_id = task.get('tracker_id') or task.get('id', '?')[:8]
    return {
        'id': display_id,
        'task': task.get('task', 'Untitled'),
        'status': STATUS_DISPLAY.get(task.get('status', ''), task.get('status', '?')),
        'priority': task.get('priority', '?'),
        'owner': task.get('owner', ''),
        'project_name': task.get('project_name', ''),
        'notes': task.get('notes', ''),
        'updated_at': task.get('updated_at', ''),
    }


def get_p0_p1_tasks():
    """
    Fetch P0 and P1 active tasks from SupaBrain brain-api.
    Falls back to tracker.json if brain-api is unavailable.
    """
    if not BRAIN_API_SECRET:
        print("  ⚠ BRAIN_API_SECRET not set, falling back to tracker.json")
        return _get_p0_p1_tasks_from_tracker()

    all_tasks = []
    for priority in ('P0', 'P1'):
        raw = _fetch_supabrain_tasks(priority)
        if raw is None:
            # API failed — fall back entirely to tracker.json
            print(f"  ⚠ brain-api failed for {priority}, falling back to tracker.json")
            return _get_p0_p1_tasks_from_tracker()
        all_tasks.extend(raw)

    # Filter to active statuses
    active = [
        _normalize_supabrain_task(t)
        for t in all_tasks
        if t.get('status') in ACTIVE_STATUSES_SUPABRAIN
    ]

    # Sort: P0 first, then by updated_at desc
    active.sort(key=lambda t: (0 if t['priority'] == 'P0' else 1, t.get('updated_at', '') or ''), reverse=False)
    # Re-sort: P0 first, within priority most-recently-updated first
    active.sort(key=lambda t: (0 if t['priority'] == 'P0' else 1))

    # Check for stale (not updated in 7+ days)
    now = datetime.utcnow().date()
    stale = []
    overdue = []

    for task in active:
        try:
            updated_str = task.get('updated_at', '')
            if not updated_str:
                continue
            # Handle ISO format with timezone
            updated = datetime.fromisoformat(updated_str.replace('Z', '+00:00')).date()
            days_old = (now - updated).days
            if days_old >= 14:
                overdue.append({**task, 'days_overdue': days_old})
            elif days_old >= 7:
                stale.append({**task, 'days_stale': days_old})
        except Exception:
            pass

    return {
        'p0_p1': active[:10],
        'stale': stale,
        'overdue': overdue,
        'source': 'supabrain',
    }


def _get_p0_p1_tasks_from_tracker():
    """Legacy fallback: Extract P0 and P1 tasks from tracker.json."""
    try:
        with open(TRACKER_FILE, 'r') as f:
            data = json.load(f)

        p0_p1 = [
            t for t in data.get('tasks', [])
            if t.get('priority') in ['P0', 'P1']
        ]

        active = [
            t for t in p0_p1
            if t.get('status') in ACTIVE_STATUSES_TRACKER
        ]

        now = datetime.utcnow().date()
        stale = []
        overdue = []

        for task in active:
            try:
                updated = datetime.fromisoformat(task.get('updated', '1970-01-01')).date()
                days_old = (now - updated).days
                if days_old >= 14:
                    overdue.append({**task, 'days_overdue': days_old})
                elif days_old >= 7:
                    stale.append({**task, 'days_stale': days_old})
            except Exception:
                pass

        return {
            'p0_p1': active[:10],
            'stale': stale,
            'overdue': overdue,
            'source': 'tracker.json',
        }

    except Exception as e:
        print(f"✗ Tracker fallback error: {e}")
        return {'p0_p1': [], 'stale': [], 'overdue': [], 'source': 'error'}


def load_contacts(drive_service):
    """Load top contacts from Drive."""
    try:
        request = drive_service.files().get_media(fileId=CONTACTS_DRIVE_FILE_ID)
        content = request.execute()
        data = json.loads(content.decode('utf-8'))

        top_3 = data.get('meta', {}).get('top_3', [])
        return top_3
    except Exception:
        return []


def get_weekly_review():
    """
    Search SupaBrain for the most recent WEEKLY REVIEW capture.
    Only returns content on Saturdays and Mondays.
    """
    now = datetime.now()
    # 5 = Saturday, 0 = Monday
    if now.weekday() not in (5, 0):
        return None

    if not BRAIN_API_SECRET:
        print("  ⚠ BRAIN_API_SECRET not set, skipping weekly review")
        return None

    try:
        import requests as req_lib
        resp = req_lib.post(
            BRAIN_API_URL,
            json={
                "action": "search",
                "query": "WEEKLY REVIEW",
                "match_count": 1
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {BRAIN_API_SECRET}"
            },
            timeout=15
        )

        if resp.status_code != 200:
            print(f"  ⚠ brain-api search returned {resp.status_code}, trying recent fallback")
            return _weekly_review_fallback()

        data = resp.json()
        results = data.get("results", [])
        if not results:
            return _weekly_review_fallback()

        capture = results[0]
        created = capture.get("created_at", "")
        if created:
            capture_date = datetime.fromisoformat(created.replace("Z", "+00:00"))
            age_days = (datetime.now(capture_date.tzinfo) - capture_date).days
            if age_days > 7:
                return None

        return capture.get("content", capture.get("raw_text", ""))

    except Exception as e:
        print(f"  ⚠ Weekly review fetch error: {e}")
        return _weekly_review_fallback()


def _weekly_review_fallback():
    """Fall back to reading the review file directly."""
    now = datetime.now()
    days_since_friday = (now.weekday() - 4) % 7
    last_friday = now - timedelta(days=days_since_friday)
    review_path = f"/home/clawdbot/weekly-reviews/review-{last_friday.strftime('%Y-%m-%d')}.md"

    try:
        if os.path.exists(review_path):
            with open(review_path, 'r') as f:
                content = f.read()
            if content.strip():
                print(f"  ✓ Loaded weekly review from {review_path}")
                return content
    except Exception as e:
        print(f"  ⚠ Review file fallback error: {e}")

    return None


def generate_briefing(calendar_events, tasks, contacts, weekly_review=None):
    """Generate briefing markdown."""
    now = datetime.utcnow()
    today_str = now.strftime('%A, %B %d, %Y')
    task_source = tasks.get('source', '?')

    lines = [
        f"# Daily Briefing — {today_str}",
        "",
        "## 📅 Calendar"
    ]

    if calendar_events:
        for event in calendar_events[:5]:
            start_time = event['start'].split('T')[1].split(':00')[0]
            lines.append(f"- {start_time}: {event['title']}")
    else:
        lines.append("(clear)")

    lines.extend([
        "",
        f"## 🎯 Active Tasks (P0/P1) [{task_source}]"
    ])

    if tasks.get('p0_p1'):
        for task in tasks['p0_p1'][:5]:
            status = task.get('status', '?')
            task_id = task.get('id', '?')
            task_name = task.get('task', 'Untitled')
            project = task.get('project_name', '')
            project_tag = f" ({project})" if project else ""
            lines.append(f"- [{status}] #{task_id}: {task_name}{project_tag}")
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

    # Overdue warnings
    if tasks.get('overdue'):
        lines.extend([
            "",
            "## 🚨 Overdue Tasks (14+ days)"
        ])
        for task in tasks['overdue'][:3]:
            task_id = task.get('id', '?')
            days = task.get('days_overdue', 0)
            task_name = task.get('task', 'Untitled')
            lines.append(f"- #{task_id} ({days}d): {task_name}")

    # Weekly review (Saturday and Monday only)
    if weekly_review:
        lines.extend([
            "",
            "## 📊 Weekly Review",
            weekly_review
        ])

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

    lines.append("• Review P0/P1 blockers")
    lines.append("• Check email for urgent flags")

    lines.append("")
    lines.append(f"*Generated {now.strftime('%H:%M %Z')} — tasks from {task_source}*")

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
    print(f"📱 Would send to Telegram: {len(message)} chars")
    return True


def main():
    print("=" * 60)
    print("Daily Briefing v2.2 — " + datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'))
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

    tasks = get_p0_p1_tasks()
    source = tasks.get('source', '?')
    print(f"  ✓ Tasks: {len(tasks['p0_p1'])} active, {len(tasks['stale'])} stale [{source}]")

    contacts = load_contacts(drive)
    print(f"  ✓ Contacts: {len(contacts)} top")

    # Weekly review (Saturday and Monday only)
    weekly_review = get_weekly_review()
    if weekly_review:
        print(f"  ✓ Weekly review: {len(weekly_review)} chars")
    else:
        dow = datetime.now().strftime('%A')
        if dow in ('Saturday', 'Monday'):
            print(f"  ℹ No weekly review found for {dow}")

    # Generate briefing
    print("\n📝 Generating briefing...")
    briefing_content = generate_briefing(calendar_events, tasks, contacts, weekly_review=weekly_review)

    # Save to file
    filepath = save_briefing(briefing_content)

    # Display briefing
    print("\n" + "=" * 60)
    print(briefing_content)
    print("=" * 60)

    print("\n✓ Daily Briefing Complete")


if __name__ == '__main__':
    main()
