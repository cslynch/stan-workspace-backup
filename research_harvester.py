#!/usr/bin/env python3
"""
Research Harvester: Process perplexity-research-* documents from Drive
"""
import json
import os
import sys
import pickle
from pathlib import Path
from datetime import datetime
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents'
]

def get_credentials():
    """Get or refresh OAuth credentials"""
    creds = None
    token_path = Path.home() / '.openclaw' / 'credentials' / 'google-token-casey-business.pickle'
    creds_path = Path.home() / '.openclaw' / 'workspace' / 'credentials.json'
    
    # Try to load token
    if token_path.exists():
        try:
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)
        except Exception as e:
            print(f"Warning: Could not load token: {e}")
            creds = None
    
    # Refresh if needed
    if creds:
        try:
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
        except Exception as e:
            print(f"Warning: Could not refresh token: {e}")
            creds = None
    
    if not creds or not creds.valid:
        print("Error: No valid credentials found. Exiting.", file=sys.stderr)
        sys.exit(1)
    
    return creds

def list_research_docs(drive_service, parent_folder_id):
    """List all perplexity-research-* documents in a folder"""
    query = f"'{parent_folder_id}' in parents and name contains 'perplexity-research-' and trashed=false"
    results = drive_service.files().list(
        q=query,
        spaces='drive',
        fields='files(id, name, webViewLink)',
        pageSize=100
    ).execute()
    
    return results.get('files', [])

def read_google_doc(docs_service, doc_id):
    """Read content from a Google Doc"""
    doc = docs_service.documents().get(documentId=doc_id).execute()
    content = doc.get('body', {}).get('content', [])
    
    text = []
    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            for text_run in para.get('elements', []):
                if 'textRun' in text_run:
                    text.append(text_run['textRun']['content'])
        elif 'table' in element:
            # Basic table support
            table = element['table']
            for row in table.get('tableRows', []):
                row_cells = []
                for cell in row.get('tableCells', []):
                    cell_text = []
                    for cell_element in cell.get('content', []):
                        if 'paragraph' in cell_element:
                            for text_run in cell_element['paragraph'].get('elements', []):
                                if 'textRun' in text_run:
                                    cell_text.append(text_run['textRun']['content'])
                    row_cells.append(''.join(cell_text).strip())
                text.append(' | '.join(row_cells) + '\n')
    
    return ''.join(text).strip()

def slug_from_name(doc_name):
    """Convert document name to slug for filename"""
    # Remove 'perplexity-research-' prefix
    slug = doc_name.replace('perplexity-research-', '').strip()
    # Convert to lowercase, replace spaces/special chars with hyphens
    slug = slug.lower()
    slug = ''.join(c if c.isalnum() or c == '-' else '-' for c in slug)
    # Remove multiple consecutive hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')
    slug = slug.strip('-')
    return slug or 'research'

def main():
    try:
        creds = get_credentials()
        drive_service = build('drive', 'v3', credentials=creds)
        docs_service = build('docs', 'v1', credentials=creds)
        
        # Find the StanleyBot shared folder (search by name)
        query = "name='StanleyBot' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        folder_results = drive_service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name)',
            pageSize=1
        ).execute()
        
        folders = folder_results.get('files', [])
        if not folders:
            print("Error: StanleyBot folder not found in Drive")
            sys.exit(1)
        
        stanleybot_folder_id = folders[0]['id']
        print(f"Found StanleyBot folder: {stanleybot_folder_id}")
        
        # List research documents
        docs = list_research_docs(drive_service, stanleybot_folder_id)
        
        if not docs:
            print("No perplexity-research-* documents found. Silent exit.")
            sys.exit(0)
        
        # Load existing research-log.json
        research_log_path = Path('/home/clawdbot/.openclaw/workspace') / 'research-log.json'
        if research_log_path.exists():
            with open(research_log_path, 'r') as f:
                research_log = json.load(f)
        else:
            research_log = []
        
        # Extract existing doc IDs for dedup
        existing_doc_ids = {entry.get('original_doc_id') for entry in research_log}
        
        # Create research directory if it doesn't exist
        research_dir = Path('/home/clawdbot/.openclaw/workspace/research')
        research_dir.mkdir(exist_ok=True)
        
        processed = []
        failed = []
        
        for doc_info in docs:
            doc_id = doc_info['id']
            doc_name = doc_info['name']
            
            # Check for dedup
            if doc_id in existing_doc_ids:
                print(f"Skipping {doc_name} (already processed)")
                continue
            
            print(f"\nProcessing: {doc_name}")
            
            try:
                # Read document content
                content = read_google_doc(docs_service, doc_id)
                
                # Generate slug and markdown path
                slug = slug_from_name(doc_name)
                md_path = research_dir / f"{slug}.md"
                
                # Write markdown file
                with open(md_path, 'w') as f:
                    f.write(f"# {doc_name.replace('perplexity-research-', '').strip()}\n\n")
                    f.write(f"*Harvested: {datetime.now().isoformat()}*\n\n")
                    f.write(content)
                
                print(f"  ✓ Wrote: {md_path}")
                
                # Append to research log
                log_entry = {
                    'original_doc_id': doc_id,
                    'doc_name': doc_name,
                    'slug': slug,
                    'markdown_path': str(md_path),
                    'harvested_at': datetime.now().isoformat(),
                    'source_url': doc_info.get('webViewLink')
                }
                research_log.append(log_entry)
                
                # Write updated log
                with open(research_log_path, 'w') as f:
                    json.dump(research_log, f, indent=2)
                
                print(f"  ✓ Logged entry")
                
                # Only trash after BOTH markdown and log succeeded
                drive_service.files().update(
                    fileId=doc_id,
                    body={'trashed': True}
                ).execute()
                
                print(f"  ✓ Trashed original Doc")
                processed.append(doc_name)
                
            except Exception as e:
                print(f"  ✗ Error: {str(e)}")
                failed.append((doc_name, str(e)))
                # Do NOT trash if processing failed
        
        # Summary
        print("\n" + "="*60)
        print(f"Research Harvester completed at {datetime.now().isoformat()}")
        print(f"Processed: {len(processed)} documents")
        if failed:
            print(f"Failed: {len(failed)} documents")
            for name, error in failed:
                print(f"  - {name}: {error}")
        
        # Return summary for Telegram
        if processed:
            summary = f"✅ Research Harvester: {len(processed)} doc(s) processed.\n\n"
            for doc_name in processed:
                summary += f"• {doc_name}\n"
            if failed:
                summary += f"\n⚠️ {len(failed)} doc(s) failed (not deleted)"
            print("\nTELEGRAM_SUMMARY:")
            print(summary)
            return summary
        else:
            return None  # Silent skip if no docs processed

    except Exception as e:
        print(f"Fatal error: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    result = main()
    if result:
        print(result)
