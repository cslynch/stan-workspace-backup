## OpenClaw Update Available
Version: v2026.4.24-beta.1 (current: 2026.2.6)
Released: 2026-04-25 09:32 UTC

### Relevant Changes

**Security & Infrastructure (HIGH PRIORITY):**
- SSRF policy enforcement: Browser sandbox and media tools now honor configured `browser.ssrfPolicy` and web-fetch SSRF policies
- Credential security: Config doctor rejects legacy `secretref-env:` markers; structured env SecretRefs migration
- Exec approval hardening: Command allowlist patterns match PATH-resolved basenames correctly
- Gateway session durability: `sessions.json` atomic backup; restart continuations durable and recoverable
- Gateway nodes pairing: Optional `gateway.nodes.pairing.autoApproveCidrs` for trusted CIDR first-time pairing

**Telegram Improvements:**
- Phantom response fallback suppressed for agents
- Polling persists accepted offsets before restart
- Channel config schema properly generated

**Gateway & Session Routing:**
- VoiceClaw realtime WebSocket endpoint with owner-auth gating
- Gateway status ~40% faster startup (plugin loading deferred)
- Session recovery after transport failures without stale state
- Loopback auth scoped to active gateway credential
- Safeguard compaction now active for large transcripts

**Config & Recovery:**
- Plugin-scoped config invalidation no longer triggers full rollback
- Reply-run configs protected from stale runtime snapshots
- Gateway config reload comparisons fixed for env refs

### Recommendation: UPDATE

**Rationale:** Multiple security enhancements (SSRF, exec approvals, credentials), critical infrastructure fixes (session durability, restart recovery, gateway auth), and stability improvements across Telegram, routing, and session management. The fixes address operational resilience and security hardening priorities.

**Caveat:** This is a beta release (v2026.4.24-**beta.1**). Verify against stable release schedule before rolling out to production.
