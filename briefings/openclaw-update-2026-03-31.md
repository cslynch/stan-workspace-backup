## OpenClaw Update Available
**Version:** 2026.3.28 (current: 2026.2.6)  
**Released:** March 29, 2026  
**Status:** Ready for update

### Relevant Changes

**Exec Approval System**
- Add async `requireApproval` to `before_tool_call` hooks with Telegram button support
- `/approve` command now handles both exec and plugin approvals with fallback

**Telegram Improvements** (4 critical fixes)
- Message splitting: word boundary detection instead of mid-word splits
- Delivery: skip empty/whitespace-only text to prevent GrammyError 400 crashes
- ReplyId validation: reject non-numeric, NaN, and mixed-content strings at all API sinks
- Forum topics: verbose tool summaries now work in threaded topic sessions

**Security Enhancement**
- Extended web search key audit to recognize Gemini, Grok/xAI, Kimi, Moonshot, and OpenRouter

**Anthropic Provider**
- Recover unhandled stop reasons (`sensitive`, etc.) as structured errors instead of crashes

**Config Management**
- Sensitive raw config hidden by default; explicit reveal-to-edit state
- Legacy config migration cleanup: drop migrations older than 2 months; very old keys now fail validation

**Gateway & Infrastructure**
- MCP channel bridge with Gateway backing for Codex/Claude conversations
- New `openclaw config schema` command for JSON schema export

### Recommendation
**UPDATE** — Multiple critical Telegram fixes (delivery, splitting, validation), exec approval system, security improvements, and Anthropic robustness justify immediate upgrade.
