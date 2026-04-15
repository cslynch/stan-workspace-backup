## OpenClaw Update Available
Version: 2026.4.12 (current: 2026.2.6)
Released: April 13, 2026

Relevant changes:
- **Security (7 fixes):** SSRF policy enforcement on browser snapshot/screenshot, config redaction, approval allowlist checks, shell injection hardening, busybox removal
- **Telegram:** Forum topic name surfacing, credential leasing, heartbeat topic isolation, gateway callback routing
- **Gateway:** New `commands.list` RPC, startup/runtime lifecycle separation, auth hardening (redacted example credentials), session routing fixes, WebSocket keepalive, cron persistence
- **Anthropic:** Agent replay with signing, thinking-only recovery, tool call retry improvements
- **Exec Policy:** New `openclaw exec-policy` CLI for config synchronization and approval management
- **Config/Auth:** Placeholder token validation, credential redaction, auth config improvements
- **Sessions:** Cron isolation, transcript routing, heartbeat routing

Recommendation: **UPDATE**

Rationale: Multiple security fixes (SSRF, auth, injection), critical gateway infrastructure improvements, and Telegram credential/routing enhancements warrant immediate update.
