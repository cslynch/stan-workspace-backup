#!/usr/bin/env python3
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/tasks',
]

CREDENTIALS_PATH = 'google-credentials.json'
TOKEN_PICKLE = os.path.expanduser('~/.openclaw/credentials/google-token.pickle')

tasks_to_create = [
    {
        "title": "Get Rosa's Telegram user ID and add her to group chat",
        "notes": "Find Rosa's Telegram ID and add her to the main group chat"
    },
    {
        "title": "Send Rosa Trello board invite link",
        "notes": "Share the Trello board invite link with Rosa"
    },
    {
        "title": "Set up Rosa with Google Workspace account",
        "notes": "Create and configure Google Workspace account for Rosa"
    }
]

tasklist_id = "NU5VRWVOZmNkT1FTYy1zVw"

def get_credentials():
    creds = None
    
    # Try to load from pickle
    if os.path.exists(TOKEN_PICKLE):
        print(f"Loading credentials from {TOKEN_PICKLE}")
        try:
            with open(TOKEN_PICKLE, 'rb') as token:
                creds = pickle.load(token)
        except Exception as e:
            print(f"Failed to load token: {e}")
            creds = None
    
    # If no valid creds, try OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            print(f"Creating new OAuth flow from {CREDENTIALS_PATH}")
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials
        os.makedirs(os.path.dirname(TOKEN_PICKLE), exist_ok=True)
        with open(TOKEN_PICKLE, 'wb') as token:
            pickle.dump(creds, token)
            print(f"Credentials saved to {TOKEN_PICKLE}")
    
    return creds

def create_tasks():
    creds = get_credentials()
    service = build('tasks', 'v1', credentials=creds)
    
    print(f"Creating {len(tasks_to_create)} tasks in list: {tasklist_id}\n")
    
    success_count = 0
    error_count = 0
    
    for task in tasks_to_create:
        try:
            result = service.tasks().insert(
                tasklist=tasklist_id,
                body={
                    'title': task['title'],
                    'notes': task['notes'],
                }
            ).execute()
            
            print(f"✓ Created: \"{task['title']}\"")
            print(f"  ID: {result.get('id')}")
            success_count += 1
        except Exception as error:
            print(f"✗ Failed to create: \"{task['title']}\"")
            print(f"  Error: {error}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {success_count} created, {error_count} failed")
    print(f"{'='*60}")
    
    return success_count

if __name__ == '__main__':
    try:
        created = create_tasks()
        exit(0 if created > 0 else 1)
    except Exception as error:
        print(f"Fatal error: {error}")
        exit(1)
