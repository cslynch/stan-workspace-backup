## OpenClaw Update Available
Version: 2026.5.14-beta.1 (current: 2026.2.6)
Released: May 14, 2026

Relevant changes:
- **Telegram**: Mini App web_app buttons, isolated polling concurrency, IPv4 transport health checks, native command resolution
- **Gateway**: Owner-level startup tracing, HTTP/2 session recovery, undici HTTP/1.1 persistence, token-mismatch reconnect fixes
- **Security**: SSRF prevention via Host header validation on API endpoints, malformed base64 rejection in file/media transfer, JSON parser error isolation
- **Config**: OPENCLAW_HEAVY_CHECK_LOCK_SCOPE worktree support, root proxy agent routing consolidation
- **Sessions**: Codex CLI session binding, session kill/history route fixes

Note: This is a beta release. Substantial infrastructure improvements and security fixes, but recommend validation before production deployment.

Recommendation: REVIEW
