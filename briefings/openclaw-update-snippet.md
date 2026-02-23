## OpenClaw Update Available
Version: 2026.2.21 (current: 2026.2.6)
Released: February 21, 2026
Relevant changes:
- Security/Infra: gateway lock and tool-call synthetic IDs upgraded from SHA-1 to SHA-256 (stronger hash basis)
- Security/Agents: cap embedded Pi runner outer retry loop with explicit retry-limit error payload (prevents unbounded retries)
- Telegram/Streaming: simplify preview streaming config to boolean, auto-map legacy streamMode values
- Channels/CLI: add per-account/channel `defaultTo` outbound routing fallback (allows send without explicit reply-to)
- Discord/Streaming: add stream preview mode for live draft replies with partial/block options
- Discord/Telegram: add configurable lifecycle status reactions for queued/thinking/tool/done/error phases
- Memory/QMD: prevent automatic sync races with manager shutdown, skip post-close sync starts
- Gateway/Auth: allow trusted-proxy mode with loopback bind for same-host reverse-proxy deployments
- WhatsApp/Security: enforce allowlist JID authorization for reaction actions (prevent non-allowlisted chat targeting)
- Multiple SSRF/credential/exec-approval security hardening fixes (heredoc bypass, safe-bin allowlist, exec host PATH injection)
Recommendation: UPDATE
