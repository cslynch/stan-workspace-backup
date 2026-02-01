# API Cost Analysis - 2026-02-01

## Hard Data from Actual Usage

**Session:** 21 API calls from today (2026-02-01 10:05 - 11:18 CST)

### Averages Per Message
- Input tokens:       5.5
- Output tokens:      82.7
- Cache read tokens:  4,756.3
- Cache write tokens: 750.7
- **Cost per message: $0.0140**

### Today's Totals (So Far)
- Total input:        116 tokens
- Total output:       1,737 tokens
- Total cache read:   99,883 tokens
- Total cache write:  15,764 tokens
- **Total cost:       $0.29**

## Cost Projections

Based on actual $0.0140 per message:

| Messages/Day | Daily Cost | Monthly Cost |
|--------------|------------|--------------|
| 20           | $0.28      | $8.40        |
| 30           | $0.42      | $12.59       |
| 40           | $0.56      | $16.79       |
| 50           | $0.70      | $20.99       |
| 75           | $1.05      | $31.49       |
| 100          | $1.40      | $41.98       |

## Context Health Check

✓ **HEALTHY**

- Current avg cache read: **4,756 tokens**
- Target: <30,000 tokens
- Under target by: **25,244 tokens**
- No signs of session bloat

## Comparison to Previous Estimate

**Previous estimate:** $1-2/day ($30-60/month)
**Actual data shows:** $0.42-0.70/day at 30-50 messages/day = **$12-21/month**

**Result: We're tracking BETTER than estimated.**

## Analysis

The token crisis fix (disabling bundled Skills) worked perfectly:
- Cache reads went from 150k/message → 4.8k/message (97% reduction)
- Cost per message: $0.014 (very reasonable for Sonnet)
- Context staying lean and healthy

At our current usage pattern (~30-40 messages/day), we're looking at:
- **~$15/month** for full Sonnet reasoning power
- Well within budget for business value delivered

## 24-Hour Monitoring Plan

Will track until 2026-02-02 11:18 CST:
- Total messages sent
- Total cost accumulated
- Average cache read size
- Any signs of context bloat (>30k cache reads)

---

*Analysis generated from /home/clawdbot/.openclaw/agents/main/sessions/21979c5e-92eb-45ef-af0f-99028d8d0976.jsonl*
