#!/usr/bin/env python3
import os
import sys
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import googleapiclient.discovery as discovery

# Load credentials
creds_path = '/home/clawdbot/.openclaw/credentials/google-token-casey-business.pickle'
if os.path.exists(creds_path):
    with open(creds_path, 'rb') as f:
        creds = pickle.load(f)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

drive = discovery.build('drive', 'v3', credentials=creds)

# Check what's in StanleyBot folder
FOLDER_ID = '1_zJLQo6RGkjesTLbIxOaTPvoGXnYQnYT'

results = drive.files().list(
    q=f"'{FOLDER_ID}' in parents and trashed=false",
    spaces='drive',
    fields='files(id, name, mimeType)',
    pageSize=50
).execute()

files = results.get('files', [])
print(f"Files in StanleyBot folder: {len(files)}")
for f in files:
    print(f"  {f['name']} ({f['mimeType']})")

