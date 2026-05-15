# TOOLS.md - Stan's Environment

## External Services
Use `exec` to run Python scripts in workspace for all external access.
Google auth: `from google_auth import get_credentials` then build service.
Tokens at ~/.openclaw/credentials/ — always refresh before API calls.

## Google Access
- Gmail: stan@fleetbrain.ai (full), casey@fleetbrain.ai (read, send needs approval)
- Calendar: stan@ + casey@ full R/W, cslynch@ read-only
- Drive: StanleyBot folder on casey@fleetbrain.ai, Editor access

## SupaBrain
Shared memory system. Use brain_api.py via exec:
- Before any quote: `brain('get_client', client_name='Jeff Fries')`
- After any quote: `brain('log_quote', client_name='...', job_description='...', total=...)`
- Capture expense: `brain('capture_expense', vendor='...', date='YYYY-MM-DD', total=...)`
- Capture fact: `brain('capture', text='...', source='telegram', agent='stan')`
- Search: `brain('search', query='...')`
Import: `from brain_api import brain`
If client profile fields are null, ask the client. Do not guess.

## Key Paths
- Skills: ./skills/
- Credentials: symlinked from ~/.openclaw/credentials/
