# Quick Start Guide - Search Logger + Job Scout

## 🚀 What's Been Done

### 1. Search Logger Wrapper Created
- **File**: `lib/search-logger.js`
- **Purpose**: Logs all web_search calls with metadata
- **Features**: 
  - Timestamps, provider, query, source tracking
  - 2-second delay between Brave calls (enforced)
  - JSONL output to `research/search-log.jsonl`

### 2. Job Scout Fixed
- **Problem**: Was saying "Let me fetch..." without actually searching
- **Solution**: Created `job-scout-runner.py` to execute real searches
- **Status**: Cron updated and ENABLED
- **When**: Tomorrow 6:45 AM CT (then daily)

### 3. Search Logging Active
- **Log File**: `research/search-log.jsonl`
- **Current Entries**: 18+ (and growing with each test)
- **Rate Limiting**: ✅ Verified 2-second delays working

---

## 🧪 Quick Tests (Run These Anytime)

### Test 1: Verify Everything Installed
```bash
cd /home/clawdbot/.openclaw/workspace
python3 verify-search-logger.py
```

**Expected Output**: All 6 checks should pass ✅

### Test 2: Run Job Scout Manually
```bash
cd /home/clawdbot/.openclaw/workspace
python3 job-scout-runner.py
```

**Expected Output**: 
- 3 searches executed
- Job leads returned with fit scoring
- Completion logged

### Test 3: Check Search Log
```bash
tail -10 /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | jq .
```

**Expected Output**: JSON entries with timestamp, provider, query, action

### Test 4: Verify Rate Limiting
```bash
tail -10 /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | \
  jq -r '[.timestamp] | .[0] + " to " + .[-1]'
```

**Expected Output**: Shows ~2 second gaps between entries

---

## 📊 Current Status

### Files Created ✅
- [x] `lib/search-logger.js` (4.8 KB)
- [x] `job-scout-runner.py` (6.3 KB)
- [x] `job-scout.py` (8.6 KB)
- [x] `verify-search-logger.py` (7.2 KB)
- [x] `research/search-log.jsonl` (growing)
- [x] `SEARCH-LOGGER-IMPLEMENTATION.md` (full documentation)

### Cron Configuration ✅
- [x] Job Scout enabled
- [x] Scheduled for 6:45 AM CT daily
- [x] Updated to call job-scout-runner.py
- [x] Rate limiting configured (2-second delays)

### Testing ✅
- [x] Manual test: Job Scout runner works
- [x] Manual test: Search logging working
- [x] Manual test: Rate limiting verified
- [x] Verification script: All 6 checks pass
- [x] Search log: Growing with proper entries

---

## 🎯 Tomorrow's Execution (6:45 AM CT)

**What Will Happen**:

1. Cron triggers Job Scout job
2. Runs: `python3 job-scout-runner.py`
3. Executes 3 searches:
   - LinkedIn: AI Sales Executive (remote)
   - Built In: Enterprise Account Executive (AI)
   - Wellfound: AI Sales Founder roles
4. **For each search**:
   - Logs to `research/search-log.jsonl` (initiated)
   - Executes search
   - Waits 2 seconds (rate limiting)
   - Logs completion
5. Parses 15+ results and filters for Casey's criteria
6. Returns 3-5 HIGH/MEDIUM fit job leads
7. Sends formatted results via Telegram to Casey
8. Logs completion metrics

**All searches will be tracked in**: `/workspace/research/search-log.jsonl`

---

## 📋 File Locations Reference

```
/home/clawdbot/.openclaw/workspace/
├── lib/
│   └── search-logger.js ..................... Logging wrapper
├── research/
│   └── search-log.jsonl ..................... Search log (JSONL format)
├── job-scout.py ............................ Alternative Job Scout
├── job-scout-runner.py ..................... Primary Job Scout execution
├── verify-search-logger.py ................. Verification script
├── SEARCH-LOGGER-IMPLEMENTATION.md ........ Full documentation
└── QUICK-START-GUIDE.md ................... This file

/home/clawdbot/.openclaw/cron/
└── jobs.json .............................. Cron config (Job Scout updated)

/home/clawdbot/.openclaw/cron/runs/
└── d2dd0d54-b062-4aef-91ab-9fc53d9462b6.jsonl . Job Scout execution logs
```

---

## ⚡ Quick Commands

### Trigger Manual Run
```bash
cd /home/clawdbot/.openclaw/workspace && python3 job-scout-runner.py
```

### View Last 10 Searches
```bash
tail -10 /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | jq .
```

### Count Today's Searches
```bash
grep "$(date +%Y-%m-%d)" /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | wc -l
```

### Calculate Average Delay Between Searches
```bash
tail -20 /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | \
  jq -r '.timestamp' | \
  paste - - | \
  awk '{cmd="date -d \""$1"\" +%s; date -d \""$2"\" +%s"; cmd | getline a; cmd | getline b; print (b-a)*1000 "ms"}'
```

### Check Cron Job Status
```bash
grep "Job Scout" /home/clawdbot/.openclaw/cron/jobs.json | head -3
```

### View Last Cron Run
```bash
cat /home/clawdbot/.openclaw/cron/runs/d2dd0d54-b062-4aef-91ab-9fc53d9462b6.jsonl | jq -s '.[-1]'
```

---

## 🐛 Troubleshooting

### "Job Scout still not returning results tomorrow?"
1. Check cron log: `cat /home/clawdbot/.openclaw/cron/runs/d2dd0d54-b062-4aef-91ab-9fc53d9462b6.jsonl | tail -1`
2. Test script manually: `python3 job-scout-runner.py`
3. Check script exists: `ls -la job-scout-runner.py`

### "Search log not growing?"
1. Check directory: `ls -la research/`
2. Test write access: `echo "test" >> research/search-log.jsonl`
3. Check file permissions: `stat research/search-log.jsonl`

### "Rate limiting not working?"
1. Look at timestamps: `tail -5 research/search-log.jsonl | jq .timestamp`
2. Calculate gap between timestamps (should be ~2000ms)
3. Verify enforce_rate_limit() call in job-scout-runner.py

---

## ✅ Verification Checklist

Before going live, verify:

- [ ] Run `python3 verify-search-logger.py` → All 6 checks pass
- [ ] Run `python3 job-scout-runner.py` → Returns 3 job leads
- [ ] Check `research/search-log.jsonl` → Contains entries
- [ ] Verify rate limiting → `jq .timestamp` shows ~2s gaps
- [ ] Confirm cron enabled → Check `jobs.json` for enabled=true
- [ ] Test log write → `echo 'test' >> research/search-log.jsonl`

---

## 📞 Status

**As of February 15, 2026, 9:19 AM CT:**

✅ **READY FOR PRODUCTION**

- Search logging: Fully operational
- Job Scout: Fixed and tested
- Rate limiting: Verified working
- Cron configuration: Updated
- Verification: All checks passing

**Next automated run**: Tomorrow 6:45 AM CT (Job Scout cron)

---

## 💡 Pro Tips

1. **Monitor the log in real-time**:
   ```bash
   tail -f /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | jq '.action'
   ```

2. **Count searches by source**:
   ```bash
   jq -r '.source' /home/clawdbot/.openclaw/workspace/research/search-log.jsonl | sort | uniq -c
   ```

3. **Find failed searches**:
   ```bash
   jq 'select(.action=="error")' /home/clawdbot/.openclaw/workspace/research/search-log.jsonl
   ```

4. **Export daily log**:
   ```bash
   grep "$(date +%Y-%m-%d)" /home/clawdbot/.openclaw/workspace/research/search-log.jsonl > daily-searches.jsonl
   ```

---

**Ready to roll! 🚀**
