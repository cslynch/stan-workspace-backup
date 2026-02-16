#!/usr/bin/env python3
"""
Verification script for search logging + Job Scout integration
Tests that everything is working correctly
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

WORKSPACE = Path(__file__).parent
RESEARCH_DIR = WORKSPACE / "research"
SEARCH_LOG_PATH = RESEARCH_DIR / "search-log.jsonl"

def verify_search_logger_exists():
    """Verify search-logger.js wrapper exists"""
    lib_file = WORKSPACE / "lib" / "search-logger.js"
    if lib_file.exists():
        print("✅ search-logger.js exists")
        print(f"   Path: {lib_file}")
        return True
    else:
        print("❌ search-logger.js NOT FOUND")
        return False

def verify_research_directory():
    """Verify research directory exists"""
    if RESEARCH_DIR.exists():
        print("✅ research/ directory exists")
        print(f"   Path: {RESEARCH_DIR}")
        return True
    else:
        print("❌ research/ directory NOT FOUND")
        return False

def verify_search_log_exists():
    """Verify search-log.jsonl exists"""
    if SEARCH_LOG_PATH.exists():
        print("✅ search-log.jsonl exists")
        print(f"   Path: {SEARCH_LOG_PATH}")
        return True
    else:
        print("❌ search-log.jsonl NOT FOUND")
        return False

def analyze_search_log():
    """Analyze search log contents and verify structure"""
    if not SEARCH_LOG_PATH.exists():
        return False
    
    try:
        entries = []
        with open(SEARCH_LOG_PATH, 'r') as f:
            for line in f:
                if line.strip():
                    entries.append(json.loads(line))
        
        if not entries:
            print("⚠️  search-log.jsonl is empty")
            return False
        
        print(f"✅ search-log.jsonl contains {len(entries)} entries")
        
        # Analyze today's entries
        today = datetime.now().strftime('%Y-%m-%d')
        today_entries = [e for e in entries if e.get('timestamp', '').startswith(today)]
        
        if today_entries:
            print(f"   Today's searches: {len(today_entries)}")
            
            # Check for required fields
            required_fields = ['timestamp', 'provider', 'action', 'source']
            sample = today_entries[0]
            missing = [f for f in required_fields if f not in sample]
            
            if missing:
                print(f"   ⚠️  Missing fields in log: {missing}")
                return False
            else:
                print(f"   ✅ All required fields present: {', '.join(required_fields)}")
            
            # Check for rate limiting (2-second delays)
            initiated_entries = [e for e in today_entries if e.get('action') == 'initiated']
            if len(initiated_entries) > 1:
                times = [datetime.fromisoformat(e['timestamp'].replace('Z', '+00:00')) 
                        for e in initiated_entries]
                times.sort()
                
                delays = []
                for i in range(len(times) - 1):
                    delay_ms = (times[i+1] - times[i]).total_seconds() * 1000
                    delays.append(delay_ms)
                
                if delays:
                    avg_delay = sum(delays) / len(delays)
                    min_delay = min(delays)
                    
                    if min_delay >= 1900:  # Allow small variance
                        print(f"   ✅ Rate limiting verified: avg delay {avg_delay:.0f}ms, min {min_delay:.0f}ms")
                    else:
                        print(f"   ⚠️  Rate limiting may not be working: min delay {min_delay:.0f}ms (should be ~2000ms)")
        else:
            print("   ⚠️  No entries from today found")
        
        return True
    except Exception as e:
        print(f"❌ Error analyzing search-log.jsonl: {e}")
        return False

def verify_job_scout_scripts():
    """Verify Job Scout scripts exist"""
    scripts = [
        "job-scout.py",
        "job-scout-runner.py"
    ]
    
    all_exist = True
    for script in scripts:
        script_path = WORKSPACE / script
        if script_path.exists():
            print(f"✅ {script} exists")
        else:
            print(f"❌ {script} NOT FOUND")
            all_exist = False
    
    return all_exist

def verify_cron_config():
    """Verify cron job configuration"""
    cron_file = Path("/home/clawdbot/.openclaw/cron/jobs.json")
    
    if not cron_file.exists():
        print("❌ cron/jobs.json NOT FOUND")
        return False
    
    try:
        with open(cron_file, 'r') as f:
            config = json.load(f)
        
        # Find Job Scout job
        job_scout = None
        for job in config.get('jobs', []):
            if job.get('name') == 'Job Scout (6:45 AM CT)':
                job_scout = job
                break
        
        if not job_scout:
            print("❌ Job Scout cron job NOT FOUND in config")
            return False
        
        print("✅ Job Scout cron job found")
        
        # Verify it's calling the runner script
        payload_msg = job_scout.get('payload', {}).get('message', '')
        if 'job-scout-runner.py' in payload_msg:
            print("   ✅ Cron is calling job-scout-runner.py")
        else:
            print(f"   ⚠️  Cron message doesn't reference job-scout-runner.py")
            print(f"      Current message: {payload_msg[:100]}...")
        
        # Check if enabled
        if job_scout.get('enabled'):
            print("   ✅ Cron job is ENABLED")
        else:
            print("   ⚠️  Cron job is DISABLED")
        
        return True
    except Exception as e:
        print(f"❌ Error reading cron config: {e}")
        return False

def main():
    """Run all verification checks"""
    print("=" * 70)
    print("SEARCH LOGGING + JOB SCOUT VERIFICATION")
    print("=" * 70)
    print()
    
    checks = [
        ("Search Logger Library", verify_search_logger_exists),
        ("Research Directory", verify_research_directory),
        ("Search Log File", verify_search_log_exists),
        ("Search Log Analysis", analyze_search_log),
        ("Job Scout Scripts", verify_job_scout_scripts),
        ("Cron Configuration", verify_cron_config),
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        print("-" * 70)
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            results.append((check_name, False))
    
    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for check_name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {check_name}")
    
    print()
    print(f"Result: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 All systems ready! Job Scout will execute tomorrow at 6:45 AM CT")
        return 0
    else:
        print(f"\n⚠️  {total - passed} checks failed. Review above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
