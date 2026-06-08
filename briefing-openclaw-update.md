## OpenClaw Update Available
Version: 2026.6.5-beta.2 (current: 2026.2.6)
Released: 2026-06-07

Relevant changes:
- **Telegram**: QQBot now strips model reasoning/thinking before native delivery, preventing raw scaffold content from leaking into channel replies
- **Security/Config**: Guard MCP HTTP redirects (SSRF protection); protect global agent config defaults
- **Anthropic**: Extended-thinking sessions recover after prompt-cache expiry or Gateway restart; better error handling prevents poisoned session history
- **Session/Credential**: Auth profiles now live in SQLite for durability; session transcript consistency improved
- **Gateway**: Duplicate Gateway probe warnings reduced; reliability improvements for node pairing and direct sessions

Recommendation: REVIEW
*Note: This is a beta release. Relevant for security (config/credential durability) and Telegram reliability. Defer production deployment until 2026.6.5 stable is available.*
