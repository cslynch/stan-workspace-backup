## OpenClaw Update Available
Version: 2026.2.17 (current: 2026.2.6)
Released: February 18, 2026

### Relevant Changes

**Security (CRITICAL):**
- Fixed OC-09 credential-theft path via environment-variable injection in exec
- Hardened `$include` config resolution to prevent directory traversal / symlink attacks
- Added URL allowlists for `web_search` and `web_fetch` (prevents SSRF-adjacent issues)

**Anthropic Support:**
- Added opt-in 1M context beta header support for Opus/Sonnet via `params.context1m: true`
- Support for Anthropic Sonnet 4.6 (`anthropic/claude-sonnet-4-6`) with forward-compat fallback

**Telegram Enhancements:**
- Inline button `style` support (primary|success|danger)
- User message reactions as system events with configurable scope
- DM voice-note transcription with CLI fallback
- Private-chat topic `message_thread_id` preservation for threaded replies
- Improved streaming and draft-preview handling

**Gateway & Config:**
- Separate per-job webhook delivery with dedicated auth token support
- Per-run model/provider usage telemetry in cron logs/webhooks
- Per-model `thinkingDefault` overrides
- `$include` resolution hardened with cross-platform safe path containment
- Discord exec command options exposed (host/security/ask/node) with autocomplete

**Session & Routing:**
- Reply threading preserved across streamed/split chunks (iMessage, Telegram, Discord, Matrix)
- Subagent context preservation (groupId, groupChannel, space)
- Session lock watchdog improvements to prevent force-unlock mid-run

### Recommendation
**UPDATE** — Security fixes (OC-09 + config hardening) are critical. Anthropic 4.6 support + Telegram improvements are significant.
