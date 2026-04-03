## OpenClaw Update Available

**Version:** 2026.4.1 (current: 2026.2.6)  
**Released:** April 1, 2026  

### Relevant Changes

**Exec Approvals (Security):**
- `allow-always` now persists as durable user-approved trust (not one-time)
- Static allowlist entries no longer silently bypass `ask:"always"` security policy
- Explicit approval required on Windows when allowlist execution plan cannot be built
- Honor `exec-approvals.json` security defaults when inline tool policy is unset
- Slack/Discord native approval handling aligned with inferred approvers

**Telegram:**
- Configurable `errorPolicy` and `errorCooldownMs` per account/chat/topic to suppress repeated delivery errors
- Topic-aware exec approval routing (stays in originating forum topic, not root chat)
- Retry safe-send path with `429`/`retry_after` backoff handling
- Preserve media MIME types for local Bot API downloads (fixes transcription)

**Gateway:**
- Session conversation grammar moved to plugin-owned session-key surfaces
- Preserves Telegram topic routing and Feishu scoped inheritance across bootstrap/restart/tool-policy
- Config reload ignores startup writes to prevent restart loops
- HTTP request failure isolation (one broken facade doesn't crash all endpoints)
- Node command execution stays disabled until pairing approval (reduced attack surface)

**Sessions & Routing:**
- `/model` changes queued behind busy runs instead of interrupting active turn
- Session recovery improved (dead-session queue-owner repair with fallback)
- Provider-specific session conversation grammar now plugin-owned

**Anthropic:**
- Preserve thinking blocks and signatures across replay, cache-control patching, context pruning

**Auth & Credentials:**
- OAuth refresh tokens persisted before return (prevents `refresh_token_reused` loops)
- SecretRef handling fixed for agents without ACP runtime

### Recommendation

**UPDATE** — Multiple security improvements (exec approvals overhaul, gateway node policies) and critical infrastructure fixes (session routing, Telegram reliability, auth token persistence). Exec approval changes are particularly important for security posture.

---
*Briefing generated: 2026-04-02 05:50 CT*
