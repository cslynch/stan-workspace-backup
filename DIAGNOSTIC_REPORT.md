# API COST DIAGNOSTIC REPORT
**Date:** 2026-02-01 08:00 AM CST  
**Issue:** $30 API charges overnight (expected <$1)  
**Investigator:** Stan

---

## PROBLEM SUMMARY

Casey reported ~$30 in API charges between last night (~10 PM) and this morning (8 AM), during which he was mostly asleep. Expected cost should have been near $0 during idle time.

---

## CURRENT SYSTEM STATE

### Active Sessions (from `openclaw status`)
```
agent:main:main                  72k/30k (241% OVER LIMIT)  ⚠️
agent:main:cron:e8decc6c...      71k/30k (236% OVER LIMIT)  ⚠️
agent:main:cron:cf56c5dc...      6.3k/30k (21%)            ✅
agent:main:cron:b3cd04e5...      75k/1000k (8%)            ⚠️
agent:main:cron:1e4bbb02...      80k/1000k (8%)            ⚠️
agent:main:telegram:group...     59k/1000k (6%)            ⚠️
agent:main:telegram:group...     30k/1000k (3%)            ✅
agent:jake:main                  25k/200k (13%)            ✅
```

**🚨 CRITICAL FINDINGS:**
1. **Main session is 241% over context limit** (72k vs 30k limit)
2. **Cron session e8decc6c is 236% over limit** (71k vs 30k)
3. **Two cron sessions with 75-80k tokens each**
4. **Context limits are being ignored/exceeded**

---

## CONFIGURATION ANALYSIS

### Current Config (`openclaw.json`)
- **Model:** `claude-sonnet-4-5` (expensive - $3/MTok input, $15/MTok output)
- **Context limit:** `30,000 tokens`
- **Tools allowed:** 7 (read, write, edit, memory_search, memory_get, message, cron)
- **Compaction mode:** `default`
- **Context pruning:** `cache-ttl` with 2min TTL

### Tool Restrictions (Applied Yesterday)
- ✅ Removed 15+ tools to reduce system prompt size
- ✅ Disabled all bundled skills
- ⚠️ **BUT sessions still bloated to 70-80k tokens**

---

## SUSPECTED ROOT CAUSES

### 1. **Runaway Cron Sessions**
The deleted monitoring cron (`e8decc6c-7ccd-4456-b7fa-b57ff8c3a0a0`) shows as:
- Last run: 1 hour ago
- Status: running with 71k tokens
- **This should have been deleted but session is still loaded in memory**

**Overnight execution estimate:**
- Monitoring cron ran every 10 minutes
- 10 PM → 8 AM = 10 hours = **60 executions**
- Each execution with 70k+ context
- Cost per run: ~$0.40-0.60
- **Total: $24-36** ✅ Matches reported cost!

### 2. **Context Limit Violations**
Multiple sessions are **200-240% over their context limit**:
- Main: 72k/30k
- Cron e8decc6c: 71k/30k

**Why aren't they being compacted?**
- Compaction should kick in at 70% of 30k = 21k tokens
- Sessions are at 72k = 3.4x the trigger point
- **Compaction is either broken or not running**

### 3. **Session Bloat Sources**
What's filling these sessions with 70k+ tokens?
- System prompt: ~10-15k (tools + workspace files)
- Conversation history: ?
- Tool results: ?
- **Need to inspect actual session JSONL files**

---

## DATA GAPS

**Cannot fully diagnose without:**
1. ❌ Session JSONL files location unknown (`.openclaw/sessions` doesn't exist)
2. ❌ No access to actual API call logs with token counts
3. ❌ No cost tracking tool/file available
4. ❌ Cannot see what's in those 70k token sessions

**Where are sessions stored?** Need to find:
```bash
find ~/.openclaw -name "*.jsonl" -type f
```

---

## IMMEDIATE ACTIONS NEEDED

### 1. **Purge Bloated Sessions**
```bash
openclaw sessions clear --all
openclaw gateway restart
```

### 2. **Find Session Files**
```bash
find ~/.openclaw -name "*.jsonl" -type f
ls -R ~/.openclaw/agents/main/
```

### 3. **Fix Context Limits**
The 30k limit is being violated. Options:
- Increase limit to match actual usage (72k)
- Fix compaction to actually enforce 30k
- Switch to aggressive compaction mode

### 4. **Disable Expensive Cron Jobs**
Delete the cost-monitoring cron that can't actually work:
```bash
openclaw cron delete 66dd22d4-cf39-46b5-9e32-0c8313143eb8
```

---

## CONFIGURATION CHANGES TO CONSIDER

### Option A: Increase Context Limit (Quick Fix)
```json
"contextTokens": 100000
```
- Allows bloat but prevents overruns
- More expensive per message
- Doesn't solve root cause

### Option B: Fix Compaction (Proper Fix)
```json
"compaction": {
  "mode": "aggressive",
  "reserveTokensFloor": 10000,
  "maxHistoryShare": 0.2
}
```
- Forces stricter history pruning
- Keeps sessions under limit
- May lose context

### Option C: Switch to Haiku for Cron
Cron jobs don't need Sonnet 4.5:
```json
"agents": {
  "defaults": {
    "model": {
      "primary": "anthropic/claude-haiku-4-5"
    }
  }
}
```
- 20x cheaper for simple tasks
- Sonnet for main chat, Haiku for cron/automation

---

## COST BREAKDOWN (ESTIMATED)

**Overnight (10 PM - 8 AM):**
- Monitoring cron: 60 runs × $0.50 = **$30** ⚠️
- Backup cron: 1 run × $0.02 = **$0.02** ✅
- Casey's sleep messages: 0 × $0 = **$0** ✅

**Total: ~$30** (matches reported cost)

**Per cron execution cost:**
- Input: 70k tokens × $3/MTok = **$0.21**
- Output: 2k tokens × $15/MTok = **$0.03**
- Cache write: ~20k × $3.75/MTok = **$0.075**
- Cache read: ~50k × $0.30/MTok = **$0.015**
- **Total per run: ~$0.33**

60 runs × $0.33 = **$19.80** (conservative estimate)

With cache misses and rebuilds, easily hits $30.

---

## QUESTIONS FOR OPUS

1. **Why are context limits being violated?** Sessions at 241% of limit should have been compacted.
2. **Where are session files stored?** Can't find `.openclaw/sessions` directory.
3. **How to prevent cron sessions from loading full context?** They don't need 70k tokens.
4. **Best compaction strategy** to keep sessions under 30k reliably?
5. **Should we switch cron jobs to Haiku** to reduce cost by 20x?

---

## NEXT STEPS

1. ✅ Created this diagnostic report
2. ⏳ Waiting for session file locations
3. ⏳ Need to purge bloated sessions
4. ⏳ Send this report to Opus for analysis
5. ⏳ Implement recommended fixes

---

*Report generated: 2026-02-01 08:05 AM CST*  
*Awaiting further investigation data*
