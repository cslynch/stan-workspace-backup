#!/usr/bin/env python3
"""Research Harvester: Process perplexity-research docs from Google Drive"""

import json
import os
import sys
from datetime import datetime
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import pickle

STANLEYBOT_FOLDER_ID = "1_zJLQo6RGkjesTLbIxOaTPvoGXnYQnYT"
RESEARCH_LOG_PATH = "/home/clawdbot/.openclaw/workspace/research-log.json"
RESEARCH_DIR = "/home/clawdbot/.openclaw/workspace/research"
CREDENTIALS_PATH = "/home/clawdbot/.openclaw/credentials"

def get_drive_service():
    """Get authenticated Google Drive service"""
    token_file = os.path.join(CREDENTIALS_PATH, "google-token-casey-business.pickle")
    creds = None
    
    if os.path.exists(token_file):
        with open(token_file, 'rb') as f:
            creds = pickle.load(f)
    
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token_file, 'wb') as f:
            pickle.dump(creds, f)
    
    return build('drive', 'v3', credentials=creds)

def load_research_log():
    """Load existing research log"""
    if os.path.exists(RESEARCH_LOG_PATH):
        with open(RESEARCH_LOG_PATH, 'r') as f:
            return json.load(f)
    return []

def save_research_log(log):
    """Save research log"""
    with open(RESEARCH_LOG_PATH, 'w') as f:
        json.dump(log, f, indent=2)

def get_processed_doc_ids(log):
    """Extract set of already-processed doc IDs"""
    processed = set()
    for entry in log:
        if isinstance(entry, dict) and 'original_doc_id' in entry:
            processed.add(entry['original_doc_id'])
    return processed

def find_research_docs(service):
    """Find all perplexity-research-* docs in StanleyBot folder"""
    query = f"'{STANLEYBOT_FOLDER_ID}' in parents and name contains 'perplexity-research-' and trashed=false"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)', pageSize=100).execute()
    return results.get('files', [])

def read_doc_content(service, doc_id):
    """Read full content from a Google Doc"""
    try:
        doc = service.documents().get(documentId=doc_id).execute()
        text = ""
        if 'body' in doc and 'content' in doc['body']:
            for element in doc['body']['content']:
                if 'paragraph' in element:
                    for run in element['paragraph'].get('elements', []):
                        if 'textRun' in run:
                            text += run['textRun'].get('content', '')
        return text.strip()
    except Exception as e:
        print(f"Error reading doc {doc_id}: {e}")
        return None

def slugify(name):
    """Convert doc name to slug"""
    # Remove 'perplexity-research-' prefix
    slug = name.replace('perplexity-research-', '').lower()
    # Keep alphanumeric and hyphens
    slug = ''.join(c if c.isalnum() or c == '-' else '-' for c in slug)
    # Remove multiple hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug.strip('-')

def trash_doc(service, doc_id):
    """Move doc to trash"""
    try:
        service.files().update(fileId=doc_id, body={'trashed': True}).execute()
        return True
    except Exception as e:
        print(f"Error trashing doc {doc_id}: {e}")
        return False

def main():
    service = get_drive_service()
    research_log = load_research_log()
    processed_ids = get_processed_doc_ids(research_log)
    
    # Ensure research directory exists
    os.makedirs(RESEARCH_DIR, exist_ok=True)
    
    docs = find_research_docs(service)
    new_count = 0
    summary_lines = []
    
    print(f"Found {len(docs)} research docs in Drive")
    
    for doc in docs:
        doc_id = doc['id']
        doc_name = doc['name']
        
        # Skip if already processed
        if doc_id in processed_ids:
            print(f"  [SKIP] {doc_name} (already processed)")
            continue
        
        print(f"  [NEW] {doc_name}")
        
        # Read content
        content = read_doc_content(service, doc_id)
        if not content:
            print(f"    ERROR: Could not read content, skipping")
            continue
        
        # Generate slug and file path
        slug = slugify(doc_name)
        md_path = os.path.join(RESEARCH_DIR, f"{slug}.md")
        
        # Write markdown file
        try:
            with open(md_path, 'w') as f:
                f.write(f"# {doc_name}\n\n")
                f.write(content)
            print(f"    ✓ Wrote markdown to {md_path}")
        except Exception as e:
            print(f"    ERROR writing markdown: {e}")
            continue
        
        # Append to log
        log_entry = {
            "slug": slug,
            "original_doc_id": doc_id,
            "original_name": doc_name,
            "md_path": md_path,
            "imported_at": datetime.now().isoformat()
        }
        research_log.append(log_entry)
        
        # Save log (do this before trashing to ensure entry exists)
        try:
            save_research_log(research_log)
            print(f"    ✓ Appended to research-log.json")
        except Exception as e:
            print(f"    ERROR saving log: {e}")
            continue
        
        # Now safe to trash original doc
        if trash_doc(service, doc_id):
            print(f"    ✓ Trashed original Google Doc")
            new_count += 1
            summary_lines.append(f"• {doc_name}")
        else:
            print(f"    ERROR: Could not trash doc, but markdown and log were saved")
    
    # Summary
    if new_count > 0:
        summary = f"Research Harvester: Processed {new_count} new doc(s)\n\n" + "\n".join(summary_lines)
        print("\n" + "="*60)
        print(summary)
        print("="*60)
        return summary
    else:
        return None

if __name__ == '__main__':
    summary = main()
    if summary:
        print(summary)
    else:
        print("No new research docs to process")
