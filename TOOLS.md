# TOOLS.md - Stan's Environment

## How to Access External Services

You have an `exec` tool. Use it to run Python scripts in your workspace.
When Casey asks about email, calendar, or Drive — don't say you can't see them.
Run the Python to go get the data.

Calendar example:
```python
from google_auth import get_credentials
from googleapiclient.discovery import build
creds = get_credentials()
service = build('calendar', 'v3', credentials=creds)
events = service.events().list(calendarId='primary', maxResults=5).execute()
for e in events.get('items', []):
    print(e.get('summary'), e.get('start', {}).get('dateTime'))
```

Gmail example:
```python
from google_auth import get_credentials
from googleapiclient.discovery import build
creds = get_credentials()
service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(userId='me', maxResults=5).execute()
for msg in results.get('messages', []):
    m = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
    headers = {h['name']: h['value'] for h in m['payload']['headers']}
    print(headers.get('From'), headers.get('Subject'))
```

This is how you access Gmail, Calendar, and Drive. You have auth tokens. Use them.

## Google API Access
- **Auth tokens:** /home/clawdbot/.openclaw/credentials/
  - google-token.pickle (stan@fleetbrain.ai)
  - google-token-casey-business.pickle (casey@fleetbrain.ai)
  - google-credentials.json (OAuth client)
- **Token refresh:** Always load → check expiry → refresh + resave before any API call
- **Library:** googleapiclient + google_auth.py in workspace
- **Use exec tool** to run Python scripts for all Google API operations

### Gmail
- stan@fleetbrain.ai: Full R/W
- casey@fleetbrain.ai: Read for briefings, send requires Casey approval

### Calendar
- stan@fleetbrain.ai: Full R/W
- casey@fleetbrain.ai: Full R/W
- cslynch@gmail.com: Read-only

### Drive
- StanleyBot folder (ID: 1_zJLQo6RGkjesTLbIxOaTPvoGXnYQnYT) on casey@fleetbrain.ai
- Stan has Editor access
- Local copies of tracker.json, contacts.json, research-log.json also in workspace

## TTS
- Provider: ElevenLabs (via openclaw config talk section)
- Voice changes: `openclaw config set talk.voiceId "ID"`

## Key Workspace Paths
- Skills: ./skills/
- Briefings: ./briefings/
- Memory: ./memory/
- Credentials: symlinked from /home/clawdbot/.openclaw/credentials/
