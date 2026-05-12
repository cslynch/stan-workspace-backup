#!/usr/bin/env python3
import requests
import json
import os

BRAIN_API_SECRET = os.getenv("BRAIN_API_SECRET")
BRAIN_API_URL = "https://olmaksvjanknqzndalzv.supabase.co/functions/v1/brain-api"

project_payload = {
    "action": "task_create",
    "task": {
        "title": "Upscale Properties - Managed Lead Intake & Qualification",
        "description": "FleetBrain first live deployment: managed AI ops for residential contracting. Jeff (JF Contracting LLC, Kansas) as initial customer. Agent-driven lead qualification, crew scheduling, customer intake automation.",
        "context": {
            "client": {
                "name": "Jeff",
                "company": "JF Contracting and Consulting LLC",
                "dba": "Upscale Properties",
                "location": "Kansas"
            },
            "business_model": {
                "type": "Residential Contracting",
                "services": ["Concrete flatwork", "Tear out/replace", "Driveways", "Patios", "Remodeling"],
                "margin_model": "Jeff 10-20% margin on crew labor"
            },
            "fleetbrain_stack": {
                "strategy": "SuperStan (business rules definition)",
                "circuit_breaker": "Casey (exception approval)",
                "execution": "Stan (lead intake, qualification, scheduling)"
            },
            "scope": [
                "Automated lead qualification against defined business rules",
                "Inbound inquiry routing and immediate response",
                "Estimate scheduling coordination",
                "Crew capacity tracking and conflict resolution",
                "Exception escalation to Jeff/Casey"
            ]
        },
        "status": "scoping",
        "priority": "P0",
        "owner": "Casey",
        "assigned_to": "Stan",
        "due_date": "2026-05-25",
        "next_steps": [
            "Collect current lead tracking baseline (texts, spreadsheet, notebook format)",
            "Obtain 3-5 recent real customer inquiries for qualification modeling",
            "Define business rules: min job size, service radius, project preferences, crew availability calendar"
        ],
        "timeline_note": "Initial deployment within days of rule finalization. No platform build required.",
        "thesis": "Proves FleetBrain agent ops model for small contractors. Success with Upscale Properties = replicable pattern for any contractor in any geography."
    }
}

headers = {
    "Authorization": f"Bearer {BRAIN_API_SECRET}",
    "Content-Type": "application/json"
}

try:
    response = requests.post(BRAIN_API_URL, json=project_payload, headers=headers, timeout=15)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")
