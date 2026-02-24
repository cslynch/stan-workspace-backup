## OpenClaw Update Available

**Version:** 2026.2.22 (current: 2026.2.6)  
**Released:** February 23, 2026 @ 04:09 UTC  
**Recommendation:** UPDATE

### Critical Security Fixes
- Credential redaction in CLI config output (prevents terminal history leakage)
- Exec approval: Absolute path pinning (blocks binary-shadowing bypass)
- Elevated auth: Sender-only identity matching (closes recipient-token bypass)
- Shell wrapper hardening: HOME/ZDOTDIR/SHELLOPTS blocked; env whitelist enforced
- Slack token security: CSPRNG tokens, shape validation, user-identity requirements
- Memory/SSRF: 8k input cap + consistent policy enforcement across batch paths

### Gateway & Infrastructure
- Auth: Unified credential precedence; shared-token priority restored for remote gateways
- Pairing: Loopback scope-upgrade auto-approval; operator.admin privilege parity
- Restart stability: Fixed edge cases; gateway-port reachability for stale-lock detection
- Cron: Parallel execution support; timeout guards for manual + startup runs
- Delivery: Text-only announces route via direct delivery for explicit thread targets

### Telegram Enhancements
- Media: User-facing failure replies (instead of silent drop)
- Webhook: Monitor lifecycle fixes; webhook cleanup before long-poll
- Polling: Network retry logic; update-offset watermark persistence
- WSL2 + DNS: IPv6 auto-select disabled; memoized detection; ipv4first default
- Replies: Target-scoped dedupe; normalized file:// paths; forwarded-origin preservation

### Config + Session Management
- Built-in channel auto-enable via channels.&lt;id&gt;.enabled
- Session routing preservation; label persistence across resets
- Slack threading: Parent-session context beyond first turn
- Token pattern redaction in sessions_history output

**Action:** Review release notes at https://github.com/openclaw/openclaw/releases/tag/v2026.2.22, then schedule update during maintenance window.
