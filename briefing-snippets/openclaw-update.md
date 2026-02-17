## OpenClaw Update Available

**Version:** 2026.2.15 (current: 2026.2.6)
**Released:** February 16, 2026, 4:43 AM UTC
**Days behind:** 10 days

### Relevant Changes

**Security (Critical):**
- Replace deprecated SHA-1 sandbox config hashing with SHA-256 for deterministic sandbox cache and recreation checks
- Redact Telegram bot tokens from error messages and stack traces (prevent secret leakage to logs)
- Block dangerous sandbox Docker config (bind mounts, host networking, unconfined seccomp/apparmor) to prevent container escape
- Redact sensitive session/path details from `status` responses for non-admin clients
- Sanitize workspace paths before embedding into LLM prompts (prevent instruction injection)
- Cap downloaded response body size before HTML parsing (prevent memory exhaustion)

**Gateway & Credential Management:**
- Dedicated webhook auth token support (`cron.webhookToken`) for outbound cron webhook posts
- Improved `status` response security with session/path redaction
- Reject malformed `agent:` session keys to prevent accidental cross-session routing
- Harden `chat.send` inbound message handling (reject null bytes, normalize Unicode to NFC)
- Preserve operator scope for Control UI bypass modes when device identity unavailable

**Telegram Fixes:**
- Omit `message_thread_id` for DM sends (fix 400 errors on forum topics)
- Replace inbound `<media:audio>` placeholder with voice transcript
- Retry media `getFile` calls with backoff, graceful fallback on transient failures
- Finalize streaming preview replies in-place (prevent duplicate outputs)
- Disable block streaming when `streamMode` is `off`
- Add poll sending via `openclaw message poll`

**Configuration & Routing:**
- Per-channel ack reaction overrides for platform-specific emoji formats
- Nested sub-agents (sub-sub-agents) with configurable depth
- Improved group chat context injection (every turn, not just first)
- Proper announce chain routing for nested subagent runs

### Recommendation

**UPDATE** — Multiple security fixes (SHA-256 hashing, token redaction, Docker escape prevention) and critical gateway/session hardening warrant immediate adoption. Telegram improvements provide stability for your primary channel.

**Risk Level:** Low (security & stability focused, no breaking changes noted)
