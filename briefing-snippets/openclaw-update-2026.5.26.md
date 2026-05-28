## OpenClaw Update Available
Version: 2026.5.26-beta.2 (current: 2026.2.6)
Released: May 27, 2026
Relevant changes:
- **Security:** SSRF policy enforcement for Browser snapshots, prompt injection filtering, auth rate limiter hardening, content boundary validation (external content wrapping, system-event spoofing prevention)
- **Gateway:** Startup optimization (reduced plugin/channel/session scans), session caching improvements, performance traces for secret preparation
- **Exec Approvals:** Durable approval actions now hidden when unavailable, approval tokens kept local-only to prevent stale-prompt exploits
- **Telegram:** Typing/progress context preservation, improved forum topic handling
- **Session Management:** Better fallback handling in `sessions_send`, improved lifecycle cleanup
- **Credentials:** Named auth profiles and credential migration support for Hermes, OpenCode, Codex

Recommendation: UPDATE
