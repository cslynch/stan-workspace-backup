## OpenClaw Update Available
Version: 2026.2.19 (current: 2026.2.6)
Released: February 19, 2026
Relevant changes:
- Telegram: Unified message deduping, topic routing fix for cron/heartbeat, exec warnings behind verbose mode
- Gateway security audit: Add findings for open HTTP APIs (gateway.auth.mode="none"), auto-generation of gateway.auth.token, rate-limit control-plane writes to 3/min per device+IP with 30-second restart cooldown
- SSRF protection: Cron webhooks guarded, browser navigation validated, exec safeBins require trusted directories
- Websocket security: Block plaintext ws:// to non-loopback hosts
- Exec approval: Backtick escaping in Discord embeds, safeBins file-oracle removal, output/recursive flag blocking
- Session routing: Main-session-key alias support for Chat UI consistency
- Auth hardening: Reject gateway/hooks token reuse at startup
- Credentials: Forward TMPDIR for SQLite reliability in service environments
Recommendation: UPDATE