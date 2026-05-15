#!/usr/bin/env python3
"""SupaBrain API client for Stan.
Usage from exec tool:
    from brain_api import brain
    
    # Get client bundle (profile + captures + tasks + expenses)
    result = brain('get_client', client_name='Jeff Fries')
    
    # Search by meaning
    result = brain('search', query='irrigation pricing')
    
    # Capture a thought
    result = brain('capture', text='Jeff confirmed markup', source='telegram', agent='stan')
    
    # Log a completed quote
    result = brain('log_quote', client_name='Jeff Fries', job_description='Irrigation repair', total=500)
    
    # Capture an expense from receipt OCR
    result = brain('capture_expense', client_name='Jeff', vendor='Home Depot', date='2026-05-14', total=52.70)
    
    # List recent captures
    result = brain('recent', n=10)
    
    # List tasks
    result = brain('tasks', filter_status='in_progress')
"""
import json
import urllib.request

BRAIN_API_URL = 'https://olmaksvjanknqzndalzv.supabase.co/functions/v1/brain-api'
BRAIN_API_SECRET = 'ThisIsMySecret'

def brain(action, **kwargs):
    kwargs['action'] = action
    data = json.dumps(kwargs).encode()
    req = urllib.request.Request(
        BRAIN_API_URL,
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {BRAIN_API_SECRET}',
        },
        method='POST',
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python3 brain_api.py <action> [key=value ...]')
        sys.exit(1)
    action = sys.argv[1]
    kwargs = {}
    for arg in sys.argv[2:]:
        k, v = arg.split('=', 1)
        try:
            v = json.loads(v)
        except (json.JSONDecodeError, ValueError):
            pass
        kwargs[k] = v
    result = brain(action, **kwargs)
    print(json.dumps(result, indent=2))
