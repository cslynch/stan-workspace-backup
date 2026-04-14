## OpenClaw Update Available
Version: 2026.4.11 (current: 2026.2.6)
Released: April 12, 2026

Relevant changes:
- **SECURITY**: Gateway credential hardening — blank example `.env.example`, fail startup with placeholder secrets (#64586)
- Gateway: WebSocket keepalive fix for slow clients, plugin schema validation, cron config isolation
- Telegram: Approval button routing (prevent callback deadlock), topic-scoped sessions, direct DM filtering
- Sessions: Cron subagent config persistence, transcript path fixes, orphaned turn recovery
- Config: AsyncCompletion zod schema fix

Recommendation: UPDATE
Reasoning: Security hardening + critical gateway/session stability fixes for your Telegram-heavy setup.
