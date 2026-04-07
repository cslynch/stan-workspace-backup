## OpenClaw Update Available
Version: 2026.4.5 (current: 2026.2.6)
Released: April 6, 2026 03:04 UTC
Days behind: ~30

Relevant changes:
- **SECURITY**: Block browser SSRF redirect bypasses, preserve restrictive plugin-only tool allowlists, fail closed on hook crashes
- **SECURITY/Gateway**: Require owner access for `/allowlist add` and `/allowlist remove`, scope loopback browser-origin auth throttling
- **SECURITY/Device pairing**: Require non-admin paired-device sessions to manage only their own device for token rotate/revoke
- **SECURITY/Plugin routes**: Keep gateway-auth plugin runtime routes on write-only fallback scopes unless trusted-proxy explicitly declares narrower scopes
- **SECURITY/Mobile pairing**: Fail closed for internal `/pair` setup-code issuance/cleanup, keep QR bootstrap tokens bounded to mobile-safe contract
- **SECURITY/Telegram**: Honor `channels.telegram.trustedLocalFileRoots` before reading absolute Bot API `file_path` values, add `dangerouslyAllowPrivateNetwork` flag
- **SECURITY/TLS**: Synology Chat defaults HTTPS TLS verification to on, explicit `allowInsecureSsl: true` required to opt out
- **SECURITY/Exec approvals**: Remove heuristic command-obfuscation gating from host exec, rely on explicit policy/allowlist only
- **BREAKING**: Config: remove legacy public config aliases (`talk.voiceId`, `talk.apiKey`, `agents.*.sandbox.perSession`, `browser.ssrfPolicy.allowPrivateNetwork`, `hooks.internal.handlers`, channel `allow` toggles) — keep load-time compatibility + `openclaw doctor --fix` migration support
- **Gateway/startup**: Default `gateway.mode` to `local` when unset, detect PID recycling in lock files on Windows/macOS
- **Gateway/macOS**: LaunchAgent improvements, re-bootstrap if `launchctl kickstart` unloads during restart
- **Gateway/Windows**: Preserve Task Scheduler settings on reinstall, fix restart detection
- **Telegram**: Fix DM voice-note preflight transcription, reasoning preview handling, native command menu trimming, model picker checks
- **Session routing**: Matrix DM sessions add `channels.matrix.dm.sessionScope` for distinct context per room, fix shared-session collision
- **Anthropic**: Preserve native `toolu_*` replay ids on direct Anthropic/Vertex paths for cache stability
- **Credential auth**: Clear inherited Claude Code config/plugin/provider-routing env overrides in Claude CLI runs, force host-managed mode
- **Anthropic Vertex**: Honor `cacheRetention: "long"` with 1-hour prompt-cache TTL, default cache retention like direct Anthropic
- **Config/schema**: Enrich exported schema with field titles/descriptions for editors and agents

Recommendation: **UPDATE**

Rationale: Security-critical fixes (SSRF bypass, plugin allowlists, device pairing scopes, TLS defaults, exec approval hardening) + gateway startup stability + Anthropic/Vertex cache improvements + Telegram fixes + breaking config migration (requires `openclaw doctor --fix` for existing configs). Major release with infrastructure hardening.
