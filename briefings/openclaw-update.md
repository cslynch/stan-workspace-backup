## OpenClaw Update Available

**Version:** 2026.4.9 (current: 2026.2.6)
**Released:** April 9, 2026
**Status:** SECURITY + INFRASTRUCTURE

### Relevant Changes

**Security Fixes:**
- Browser/security: Re-run blocked-destination safety checks after interaction-driven navigations so browser interactions cannot bypass SSRF quarantine when landing on forbidden URLs. (#63226)
- Security/dotenv: Block runtime-control env vars from untrusted workspace `.env` files; reject unsafe URL-style browser control overrides before lazy loading. (#62660, #62663)
- Gateway/node exec events: Mark remote node exec summaries as untrusted and sanitize node-provided command/output text so remote output cannot inject trusted content into later turns. (#62659)
- Security/dependency: Force `basic-ftp` to 5.2.1 for CRLF command-injection fix; bump Hono security dependencies.
- Plugins/onboarding: Prevent untrusted workspace plugins from colliding with bundled auth-choice ids during setup. (#62368)

**Gateway & Session Infrastructure:**
- Sessions/routing: Preserve established external routes on inter-session announce traffic so `sessions_send` follow-ups don't steal delivery from Telegram/Discord. (#58013)
- Gateway/sessions: Clear auto-fallback-pinned model overrides on `/reset` and `/new` while preserving explicit user selections. (#63155)
- Gateway/chat: Suppress internal `ANNOUNCE_SKIP`/`REPLY_SKIP` control tokens from user-facing surfaces. (#51739)
- Auto-reply/NO_REPLY: Strip glued leading `NO_REPLY` tokens before reply normalization so silent sentinels don't leak into user replies. 

**Exec & Credential Management:**
- Slack/actions: Pass resolved read token into `downloadFile` so SecretRef-backed bot tokens no longer fail. (#62097)
- Reply/doctor: Resolve reply-run SecretRefs before preflight helpers touch config; surface gateway OAuth reauth failures. (#62693, #63217)
- Agents/exec: Keep `/exec` reporting aligned with real runtime behavior for `host=auto` fallback policy. 

**Other Changes:**
- Config/provider-auth: Let provider manifests declare `providerAuthAliases` for shared env vars and auth profiles.
- Android/pairing: Clear stale setup-code auth on new QR scans; bootstrap sessions from fresh pairing.
- Matrix/gateway: Wait for Matrix sync readiness before marking startup successful.
- Control UI: Guard stale session-history reloads during fast session switches.

### Recommendation

**UPDATE** — Multiple security fixes (SSRF quarantine bypass prevention, dotenv hardening, node output sanitization) and critical gateway/session infrastructure improvements warrant prompt deployment.
