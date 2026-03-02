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

# Find research folder
PARENT_ID = '1_zJLQo6RGkjesTLbIxOaTPvoGXnYQnYT'

results = drive.files().list(
    q=f"'{PARENT_ID}' in parents and name='research' and trashed=false",
    spaces='drive',
    fields='files(id, name)',
    pageSize=10
).execute()

files = results.get('files', [])
if files:
    research_folder_id = files[0]['id']
    print(f"Found research folder: {research_folder_id}")
    
    # Now list contents
    contents = drive.files().list(
        q=f"'{research_folder_id}' in parents and trashed=false",
        spaces='drive',
        fields='files(id, name, mimeType)',
        pageSize=100
    ).execute()
    
    items = contents.get('files', [])
    print(f"Contents: {len(items)}")
    for item in items:
        print(f"  {item['name']} ({item['mimeType']})")
else:
    print("Research folder not found")

