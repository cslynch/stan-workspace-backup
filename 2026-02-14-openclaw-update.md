## OpenClaw Update Available

**Version:** 2026.2.13 (current: 2026.2.6)  
**Released:** February 14, 2026 03:32 UTC  
**Recommendation:** UPDATE

### Relevant Changes

**Security Hardening:**
- Block high-risk tools (sessions_spawn, sessions_send, gateway, whatsapp_login) from HTTP `/tools/invoke` by default with configurable ACP overrides
- Breaking change: Canvas IP-based auth fallback now restricts to machine-scoped addresses (RFC1918, link-local, ULA IPv6, CGNAT); public IPs require bearer token
- SSRF bypass closure: Block loopback/internal host patterns and private/mapped IPv6 addresses in link handling
- WebSocket header sanitization in pre-handshake logs
- Enforce 0o600 on credential files (WhatsApp creds.json)
- Hardened node exec approval decision handling with proper closed-failure semantics
- Config env-snapshot race condition fix (preserves ${VAR} refs safely under concurrent mutations)
- Config audit logging for file overwrites

**Gateway & Infrastructure:**
- Outbound delivery queue with crash-recovery retries (prevents lost messages after restart)
- Auto-reply threading support without requiring model-emitted [[reply_to_current]]
- Pass replyTo/threadId through core outbound send path
- Image-only inbound messages now reach agent (not dropped)
- Proper thread routing in auto-replies
- Ollama provider normalization for model discovery

**Telegram & Routing:**
- MP3/M4A (including audio/mp4) treated as voice-compatible for asVoice routing
- Bot command registration capped to Telegram's 100-command limit with overflow warning
- Skill commands scoped per agent (fixes duplicate BOT_COMMANDS_TOO_MUCH errors)
- Numeric guild allowlist entries now prefix with 'guild:' to prevent misrouting

**Session & Config:**
- Pass agentId through transcript resolution for non-default agents
- Archive previous transcript files on session reset/new
- Context usage reporting improvements (stop clamping to context window)
- Multiple agent-level configuration resolution fixes

### Why Update Now
- Multiple security fixes with real attack surface coverage (SSRF, TOCTOU, IP spoofing)
- Gateway stability improvements (message delivery, thread routing, provider compatibility)
- Config safety improvements (env var preservation, race condition fix)
- Telegrambot reliability fixes (command limit handling, agent scoping)
