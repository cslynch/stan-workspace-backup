# OpenClaw Token Usage Crisis - Diagnostic Report for Opus Analysis

**Date:** 2026-01-31 19:31 CST
**Reporter:** Stan (Claude Sonnet 4.5)
**Severity:** CRITICAL - $6-25/day burn rate

---

## EXECUTIVE SUMMARY

OpenClaw is burning through Anthropic API tokens at 25x the expected rate. Despite multiple aggressive configuration changes, cache reads remain at ~150k tokens per message instead of the target <5k.

**Cost Impact:**
- Current: ~$0.05/message = $6-25/day
- Target: ~$0.002/message = $1-3/day
- Overage: **2500% over budget**

---

## CURRENT CONFIGURATION

```json
{
  "agents": {
    "defaults": {
      "contextTokens": 50000,
      "bootstrapMaxChars": 1000,
      "compaction": {
        "mode": "default",
        "reserveTokensFloor": 20000,
        "maxHistoryShare": 0.3
      },
      "contextPruning": {
        "mode": "cache-ttl",
        "ttl": "2m",
        "keepLastAssistants": 2,
        "softTrimRatio": 0.5,
        "hardClearRatio": 0.7
      }
    }
  }
}
```

---

## TOKEN USAGE DATA (Last 10 API Calls)

| Call | Input | Output | Cache Read | Cache Write | Cost |
|------|-------|--------|------------|-------------|------|
| 1 | 11 | 197 | 146,942 | 564 | $0.0492 |
| 2 | 10 | 90 | 147,506 | 252 | $0.0466 |
| 3 | 9 | 433 | 147,758 | 737 | $0.0536 |
| 4 | 0 | 0 | 0 | 0 | $0.0000 |
| 5 | 10 | 167 | 14,413 | 33,847 | $0.1338 |
| 6 | 12 | 169 | 146,576 | 6,264 | $0.0700 |
| 7 | 11 | 155 | 152,840 | 215 | $0.0490 |
| 8 | 10 | 189 | 153,055 | 1,416 | $0.0541 |
| 9 | 9 | 111 | 154,471 | 211 | $0.0488 |
| 10 | 9 | 381 | 154,682 | 176 | $0.0528 |

**Average Cache Reads:** 141,524 tokens/message (target: <5,000)
**Average Cost:** $0.0558/message

---

## SESSION CONTEXT

- **Session Messages:** 690 total lines in transcript
- **Active Sessions:** 3 (Main DM, Rosa group, Jeff group)
- **Model:** anthropic/claude-sonnet-4-5
- **OpenClaw Version:** 2026.1.29
- **Platform:** Hyper-V VM, Ubuntu 24.04

---

## FIXES ATTEMPTED (CHRONOLOGICAL)

### Fix #1: Compaction Mode Change (18:24 CST)
**Action:** Changed from "safeguard" → "default"
**Result:** NO IMPROVEMENT (cache reads stayed at 46k)

### Fix #2: Aggressive Context Pruning (18:50 CST)
**Action:** 
- Enabled cache-ttl pruning (5min TTL)
- Keep only last 3 assistant turns
- Soft trim tool results to 2000 chars
**Result:** SLIGHT IMPROVEMENT (46k → 14k cache reads)

### Fix #3: Nuclear Context Reduction (19:07 CST)
**Action:**
- Context window: 1M → 50k tokens
- maxHistoryShare: 0.3 (only 30% for history)
- reserveTokensFloor: 20k
- Pruning TTL: 5min → 2min
**Result:** WORSE! (14k → 141k cache reads)

### Fix #4: Bootstrap Truncation (19:31 CST - JUST APPLIED)
**Action:** bootstrapMaxChars: 20000 → 1000
**Result:** PENDING (awaiting next monitoring cycle)

---

## HYPOTHESIS

The issue appears to be **Anthropic's prompt caching behavior with OpenClaw's system prompt**, not the history size. Evidence:

1. **Cache reads dwarf actual input** (150k cache reads vs. 10 input tokens)
2. **Reducing context window made it WORSE** (suggesting system prompt is being cached heavily)
3. **Compaction mode had no effect** (history isn't the problem)
4. **One anomaly:** Call #5 had only 14k cache reads with 33k cache write (suggests cache invalidation event)

---

## WORKSPACE FILES (Potentially Being Cached)

```
AGENTS.md (7,848 bytes)
SOUL.md (1,673 bytes)
USER.md (327 bytes)
MEMORY.md (4,447 bytes)
KANBAN.md (1,798 bytes)
IDENTITY.md (430 bytes)
TOOLS.md (858 bytes)
HEARTBEAT.md (167 bytes)
BOOTSTRAP.md (1,465 bytes)
RAPIDKEY_LAUNCH_PLAN.md (8,733 bytes)
```

**Total:** ~28KB of markdown files potentially injected into EVERY system prompt

---

## ANTHROPIC API BEHAVIOR

**Prompt Caching Mechanics:**
- System prompt is cached across requests
- Cache hits cost 10% of full price ($0.03/MTok → $0.003/MTok)
- Cache writes cost 125% of full price ($0.03/MTok → $0.0375/MTok)

**What we're seeing:**
- 150k cache read tokens = ~$0.045/message just for cache
- Suggests a **150k token system prompt** is being cached and reused
- BUT: Our workspace files are only ~7k tokens total

---

## QUESTIONS FOR OPUS

1. **What is OpenClaw actually sending to Anthropic?** Is there a way to intercept/log the full API request to see the exact system prompt size?

2. **Why did reducing context window make it WORSE?** (50k limit should force compaction, but cache reads increased)

3. **Is there a hidden OpenClaw feature injecting massive context?** (Skills? Memory? Project files?)

4. **Should we disable Anthropic prompt caching entirely?** Is there a config for this?

5. **Is this a bug in OpenClaw's caching implementation?** The numbers don't add up.

---

## ADDITIONAL DIAGNOSTICS NEEDED

1. **Full API request inspection** - Need to see what OpenClaw sends to Anthropic
2. **Cache trace analysis** - OpenClaw has `diagnostics.cacheTrace` feature (should we enable it?)
3. **Session reset test** - Would starting a fresh session fix it? (nuclear option)
4. **Haiku comparison** - Does switching to Haiku show similar cache bloat?

---

## RECOMMENDATIONS

1. **Immediate:** Enable `diagnostics.cacheTrace` to log full prompts
2. **Short-term:** Consider session reset (wipes history, confirms if it's session-specific)
3. **Investigation:** Check if OpenClaw is injecting skills/memory data we're not seeing
4. **Nuclear option:** Disable prompt caching if possible (trade lower cache cost for higher input cost)

---

## FILES FOR OPUS REVIEW

**Config:** `/home/clawdbot/.openclaw/openclaw.json` (attached above)
**Session Log:** 690 lines in `~/.openclaw/agents/main/sessions/e9ca3c02-7560-40df-9bbd-21ee906c6e88.jsonl`
**Workspace Files:** Listed above in "Workspace Files" section

---

## CONTACT

**Human:** Casey (Telegram: 8461430130)
**Agent:** Stan (cslynch913@gmail.com)
**Monitoring:** Auto-reporting every 10 minutes via cron

---

**END OF REPORT**

*Generated by Stan (Claude Sonnet 4.5) at 2026-01-31 19:31 CST*
*Awaiting Opus analysis and recommendations*
