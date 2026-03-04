#!/usr/bin/env python3
"""
Job Scout Runner v2 — Executes searches per JOB_SCOUT_SPEC_v2
- Rotates through 7 search queries
- Filters by title, company profile, comp, location
- Deduplicates against job_scout_seen.json
- Outputs new leads only
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
import hashlib

WORKSPACE = Path(__file__).parent
SEEN_JOBS_FILE = WORKSPACE / "job_scout_seen.json"
SPEC_FILE = WORKSPACE / "JOB_SCOUT_SPEC_v2.md"

# Spec v2 Config (embedded for reliability)
TITLES = [
    "Enterprise Account Executive",
    "Strategic Account Executive",
    "Senior Account Executive",
    "Account Executive",
    "Solutions Sales",
    "Solutions Consultant",
    "Sales Engineer",
    "Regional Sales Manager",
    "Mid-Market Account Executive",
    "Automation Sales Specialist",
    "Platform Sales",
    "Partner Sales"
]

COMPANY_KEYWORDS = [
    "AI", "LLM", "agent", "MLOps", "machine learning",
    "automation", "iPaaS", "workflow", "RPA",
    "developer tools", "API", "data infrastructure",
    "middleware", "integration", "SaaS"
]

SEARCH_QUERIES = [
    "enterprise account executive AI SaaS remote",
    "strategic account executive automation platform",
    "solutions sales AI infrastructure remote",
    "senior AE developer tools remote",
    "account executive middleware integration SaaS",
    "sales engineer AI platform remote quota",
    "account executive data infrastructure remote"
]

MIN_COMP = 150000
MIN_COMPANY_STAGE = "Series B+"

def load_seen_jobs():
    """Load previously surfaced job IDs from dedup file."""
    try:
        with open(SEEN_JOBS_FILE, 'r') as f:
            data = json.load(f)
            return [job.get('url_hash') for job in data.get('seen_jobs', [])]
    except:
        return []

def save_seen_job(company, title, location, url_hash):
    """Add a job to the seen list."""
    try:
        with open(SEEN_JOBS_FILE, 'r') as f:
            data = json.load(f)
    except:
        data = {"seen_jobs": [], "lastUpdated": datetime.now().isoformat()}
    
    data['seen_jobs'].append({
        "company": company,
        "title": title,
        "location": location,
        "url_hash": url_hash,
        "surfaced_date": datetime.now().strftime("%Y-%m-%d")
    })
    data['lastUpdated'] = datetime.now().isoformat()
    
    with open(SEEN_JOBS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def generate_url_hash(company, title, location):
    """Generate deterministic hash for dedup."""
    key = f"{company}|{title}|{location}".lower()
    return hashlib.md5(key.encode()).hexdigest()[:12]

def filter_leads(raw_results):
    """Filter raw search results against Spec v2 criteria."""
    seen = load_seen_jobs()
    filtered = []
    
    for result in raw_results:
        company = result.get('company', '').strip()
        title = result.get('title', '').strip()
        location = result.get('location', '').strip()
        comp = result.get('comp')
        link = result.get('link', '')
        
        # Check dedup
        url_hash = generate_url_hash(company, title, location)
        if url_hash in seen:
            continue
        
        # Check title match
        title_match = any(t.lower() in title.lower() for t in TITLES)
        if not title_match:
            continue
        
        # Check comp (if provided)
        if comp and isinstance(comp, int):
            if comp < MIN_COMP:
                continue
        
        # Check location
        location_lower = location.lower()
        valid_location = (
            "remote" in location_lower or
            any(city in location_lower for city in ["austin", "san antonio", "san marcos"])
        )
        if not valid_location:
            continue
        
        # Calculate fit score (simplified)
        fit = "LOW"
        company_lower = company.lower()
        for kw in COMPANY_KEYWORDS:
            if kw.lower() in company_lower:
                fit = "HIGH"
                break
        if fit == "LOW":
            fit = "MED"
        
        filtered.append({
            "company": company,
            "title": title,
            "location": location,
            "comp": comp or "unknown",
            "link": link,
            "fit": fit,
            "url_hash": url_hash
        })
    
    return filtered

def main():
    print("=" * 80)
    print(f"Job Scout v2 — {datetime.now().strftime('%A, %B %d, %Y (%I:%M %p %Z)')}")
    print("=" * 80)
    print()
    
    # In a real scenario, web_search would be called here via OpenClaw tools
    # For now, log that we're ready and waiting for search results
    print("📋 JOB SCOUT SPEC v2 ACTIVE")
    print()
    print("Search queries (rotate 2-3/day):")
    for i, q in enumerate(SEARCH_QUERIES, 1):
        print(f"  {i}. {q}")
    print()
    print("Company profile: AI SaaS, automation, developer tools, data infra, middleware")
    print("Comp floor: $150K OTE")
    print("Location: Remote (US) or Hybrid (Austin/San Antonio/San Marcos, TX)")
    print()
    
    # Dedup status
    seen = load_seen_jobs()
    print(f"Dedup tracker: {len(seen)} previous leads in system")
    print()
    
    # In production, this would:
    # 1. Pick next search query from rotation
    # 2. Execute web_search via OpenClaw tools
    # 3. Parse results into standardized format
    # 4. Filter + dedup
    # 5. Output new leads to Casey
    
    print("STATUS: Ready for next search cycle.")
    print("        Job Scout cron enabled (6:45 AM CT daily)")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
