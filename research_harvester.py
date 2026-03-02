#!/usr/bin/env python3
import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle
import googleapiclient.discovery as discovery
from googleapiclient.errors import HttpError

# Load credentials
creds_path = '/home/clawdbot/.openclaw/credentials/google-token-casey-business.pickle'
if os.path.exists(creds_path):
    with open(creds_path, 'rb') as f:
        creds = pickle.load(f)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
else:
    print("ERROR: Credentials not found")
    sys.exit(1)

# Build Drive service
drive = discovery.build('drive', 'v3', credentials=creds)
docs = discovery.build('docs', 'v1', credentials=creds)

# Folder ID for StanleyBot
FOLDER_ID = '1_zJLQo6RGkjesTLbIxOaTPvoGXnYQnYT'
RESEARCH_DIR = Path('/home/clawdbot/.openclaw/workspace/research')
LOG_PATH = Path('/home/clawdbot/.openclaw/workspace/research-log.json')

RESEARCH_DIR.mkdir(exist_ok=True)

# Load existing log
log_data = {}
if LOG_PATH.exists():
    with open(LOG_PATH, 'r') as f:
        log_data = json.load(f)

processed_docs = []
errors = []

try:
    # Query for perplexity-research-* documents in folder
    query = f"'{FOLDER_ID}' in parents and name contains 'perplexity-research-' and trashed=false"
    results = drive.files().list(
        q=query,
        spaces='drive',
        fields='files(id, name, mimeType)',
        pageSize=100
    ).execute()
    
    files = results.get('files', [])
    
    if not files:
        print("No perplexity-research-* documents found.")
        sys.exit(0)
    
    for file in files:
        doc_id = file['id']
        doc_name = file['name']
        
        # Skip if already processed (dedup)
        if doc_id in log_data:
            print(f"Skipping {doc_name} (already processed)")
            continue
        
        try:
            # Extract slug from document name
            slug = doc_name.replace('perplexity-research-', '').replace(' ', '-').lower()
            slug = re.sub(r'[^a-z0-9-]', '', slug)
            
            # Read Google Doc
            doc = docs.documents().get(documentId=doc_id).execute()
            
            # Convert doc to markdown
            content = []
            if 'body' in doc and 'content' in doc['body']:
                for element in doc['body']['content']:
                    if 'paragraph' in element:
                        para = element['paragraph']
                        text = ''
                        if 'elements' in para:
                            for el in para['elements']:
                                if 'textRun' in el:
                                    text += el['textRun'].get('content', '')
                        if text.strip():
                            content.append(text.strip())
            
            markdown = '\n\n'.join(content)
            
            # Write markdown file
            output_path = RESEARCH_DIR / f"{slug}.md"
            with open(output_path, 'w') as f:
                f.write(f"# {doc_name}\n\n")
                f.write(f"Source: [Google Doc]({doc_id})\n\n")
                f.write(markdown)
            
            # Append to log
            log_data[doc_id] = {
                'original_doc_id': doc_id,
                'doc_name': doc_name,
                'slug': slug,
                'processed_at': datetime.now().isoformat(),
                'output_file': str(output_path)
            }
            
            # Save log
            with open(LOG_PATH, 'w') as f:
                json.dump(log_data, f, indent=2)
            
            # Trash the original doc
            drive.files().update(
                fileId=doc_id,
                body={'trashed': True}
            ).execute()
            
            processed_docs.append({
                'name': doc_name,
                'slug': slug,
                'output': str(output_path)
            })
            print(f"✓ Processed: {doc_name}")
            
        except Exception as e:
            error_msg = f"Error processing {doc_name}: {str(e)}"
            errors.append(error_msg)
            print(f"✗ {error_msg}")
    
    # Print summary
    if processed_docs:
        print(f"\n📊 Research Harvester Complete")
        print(f"Processed: {len(processed_docs)} document(s)")
        for doc in processed_docs:
            print(f"  • {doc['name']} → {doc['slug']}.md")
        if errors:
            print(f"\nWarnings: {len(errors)}")
            for err in errors:
                print(f"  ⚠ {err}")
    else:
        print("No new documents to process.")

except HttpError as error:
    print(f'API Error: {error}')
    sys.exit(1)

