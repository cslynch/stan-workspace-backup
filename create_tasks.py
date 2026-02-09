#!/usr/bin/env python3
import json
import subprocess
import sys

# Google Tasks API create task script
# Uses the google-workspace CLI through OpenClaw

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

# Try to invoke through gateway or CLI
try:
    for task in tasks_to_create:
        print(f"Creating task: {task['title']}")
        # This would normally use the Google Tasks API
        # For now, let's try to find the right method
        print(f"  Notes: {task['notes']}")
        print()
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

print("Tasks to create:")
print(json.dumps(tasks_to_create, indent=2))
