## OpenClaw Update Available
Version: 2026.4.9 (current: 2026.2.6)
Released: April 9, 2026 at 02:25 UTC

Relevant changes:

- **Browser/Security**: SSRF quarantine hardening—re-run blocked-destination safety checks after interaction-driven main-frame navigations so browser interactions cannot bypass SSRF quarantine when landing on forbidden URLs. (#63226)
- **Security/dotenv**: Block runtime-control env vars and browser-control override from untrusted workspace `.env` files; reject unsafe URL-style browser control specifiers before lazy loading. (#62660, #62663)
- **Gateway/node exec events**: Mark remote node `exec.started`, `exec.finished`, `exec.denied` summaries as untrusted and sanitize node-provided command/output/reason text before enqueueing—prevents remote node output from injecting trusted `System:` content. (#62659)
- **Security/dependency audit**: Force `basic-ftp` to `5.2.1` for CRLF command-injection fix; bump Hono and `@hono/node-server`.
- **Sessions/routing**: Preserve established external routes on inter-session announce traffic—`sessions_send` follow-ups no longer steal delivery from Telegram or other external channels. (#58013)
- **Config/credential handling**: Resolve reply-run SecretRefs before preflight helpers touch config; persist explicit auth-profile upserts directly without stale external credential state.

Recommendation: **UPDATE**

Multiple security fixes including SSRF hardening, dotenv controls, and gateway node event sanitization address infrastructure integrity.
