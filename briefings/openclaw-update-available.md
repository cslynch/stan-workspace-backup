## OpenClaw Update Available
Version: 2026.4.24 (current: 2026.2.6)
Released: April 25, 2026

Relevant changes:
- **Telegram**: Agent response fallback suppression (#70623), polling offset persistence, channel config schema metadata, model display names in picker
- **Gateway Security**: Realtime WebSocket endpoint with auth gating (#70938), node pairing auto-approve CIDR option (disabled by default), tool invoke bridge for plugin-backed catalog tools
- **Session Management**: Oversized sessions.json rotation backup, recovery of main-agent turns interrupted by gateway restart (#70555)
- **Browser Security**: Require `operator.admin` for `browser.request` gateway method, SSRF policy propagation to sandbox bridges, proxy environment variable isolation
- **Exec Approvals**: Allow bare command-name allowlist patterns to match PATH-resolved binaries (#71315)
- **Gateway Config**: Skip false full restarts when `${VAR}` env refs are unchanged on disk (#71208)

Recommendation: **UPDATE**

Security improvements include auth gating on new realtime endpoints, tightened browser control authorization, and SSRF policy enforcement. Session recovery and Telegram reliability are stable. No breaking changes impacting Telegram or core credential flow.
