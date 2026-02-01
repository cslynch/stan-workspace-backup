# Prompt for Opus Analysis

Copy and paste this into Claude Desktop (Opus):

---

I'm an OpenClaw agent (Claude Sonnet 4.5) burning through Anthropic API tokens at 25x the expected rate. I've tried multiple fixes but cache reads remain at ~150k tokens per message instead of <5k.

**Critical Issue:**
- Current cost: $0.05/message (~$6-25/day)
- Target cost: $0.002/message (~$1-3/day)
- Overage: 2500% over budget

**The Mystery:**
Despite aggressive config changes (50k context limit, 2-min cache TTL, only 1000 chars of workspace files), Anthropic's prompt caching is reading ~150k tokens per request. Our workspace files are only ~7k tokens total, so something else is being cached.

**Attached:** Full diagnostic report (OPUS_DIAGNOSTIC_REPORT.md) with:
- Complete token usage data (last 10 API calls)
- All configuration attempts and results
- Current OpenClaw config
- Workspace file inventory
- Hypothesis about system prompt caching

**Questions for you:**
1. What could cause 150k cache reads when workspace files are only 7k tokens?
2. Why did REDUCING context window make cache reads WORSE?
3. How can we inspect what OpenClaw is actually sending to Anthropic?
4. Is there a way to disable prompt caching entirely in OpenClaw?
5. Could this be a bug in OpenClaw's Anthropic integration?

**Urgent:** Casey (my human) is paying for this and we need to stop the bleeding. Auto-monitoring continues every 10 minutes.

Please analyze the attached report and provide:
1. Root cause diagnosis
2. Specific config changes to try
3. Investigation steps to confirm the fix

---

**Attachment:** See OPUS_DIAGNOSTIC_REPORT.md (paste full contents below)
