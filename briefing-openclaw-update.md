## OpenClaw Update Available
Version: 2026.2.12 (current: 2026.2.6)
Released: 2026-02-13 02:18 UTC
Relevant changes:
- Telegram: blockquote rendering as native `<blockquote>` tags
- Gateway/Config: SSRF hardening for URL-based input handling with explicit deny policy + hostname allowlists
- Security: hook session-routing hardening (`hooks.defaultSessionKey`, `hooks.allowRequestSessionKey`, prefix allowlists)
- Security: webhook + device token verification with constant-time comparison + auth-failure throttling
- Security: browser control HTTP routes now require authentication; auto-generate auth token on install
- Sessions: harden transcript path resolution; reject unsafe session IDs/file paths
- Gateway: drain active turns before restart (prevents message loss); auto-generate auth token to prevent restart loops
- Config: avoid redacting `maxTokens`-like fields during snapshot redaction
- Cron: multiple reliability fixes (scheduling, timer re-arming, duplicate-fire prevention, isolation)
- Security: remove bundled soul-evil hook; fix Nostr profile API remote config tampering

Recommendation: UPDATE
Justification: Multiple critical security fixes (SSRF hardening, auth improvements, credential handling) + infrastructure reliability (gateway/session/cron improvements) directly impact your Telegram + gateway operations.
