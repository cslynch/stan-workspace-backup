## OpenClaw Update Available
Version: 2026.6.5-beta.2 (current: 2026.2.6)
Released: 2026-06-07
Prerelease: Yes (beta.2)

### Relevant Changes
- **Anthropic extended-thinking recovery**: Sessions now recover after prompt-cache expiry or Gateway restart; stream start events wait for `message_start`, triggering existing recovery retry mechanisms (#90667, #90697)
- **MCP tool result security fixes**: Non-text/image blocks coerced at materialize boundary, preventing Anthropic 400s and poisoned session history (#90710, #90728)
- **Telegram/QQBot content boundaries**: Reasoning/thinking tags stripped before delivery, preserving answers while hiding internal narration (#89913, #90132)
- **Auth state durability**: Auth profiles now live in SQLite; plugin install records keep trusted pins; prerelease fallback integrity checks improved (#89102, #88585)
- **Gateway/macOS stability**: Node mode no longer self-reconnects away from healthy direct Gateway sessions, reducing companion app churn (#90668, #90815)
- **Service environment handling**: Cron legacy JSON stores migrate during doctor preflight; service env placeholders no longer mask state-dir secrets (#90072, #90208)

### Recommendation
**UPDATE** — Beta release contains critical security fixes (tool result coercion, prompt injection), infrastructure-critical Anthropic recovery improvements, auth durability enhancements, and Telegram-relevant changes. Anthropic integration stability and auth persistence make this relevant for your stack.

---
*Evaluated at 2026-06-08 05:50 CT*
