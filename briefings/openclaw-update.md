## OpenClaw Update Available

**Version:** 2026.4.11 (current: 2026.2.6)
**Released:** April 12, 2026

### Relevant Changes

**Security Hardening (CRITICAL)**
- Browser/security: SSRF defenses across navigation, hostname allowlists, subframes, CDP discovery, tabs, and Docker CDP ranges
- Security/tools: exec preflight hardening, node output boundaries, host-media reads, plugin dependency scanning, WebSocket frame handling
- Telegram/security: tightened sender validation in allowlist checks

**Gateway & Infrastructure**
- Gateway startup: WebSocket RPC availability during channel/sidecar startup; prevents lockout on startup stalls
- Gateway thread routing: preserves Slack, Telegram, Mattermost, Matrix routing across restarts
- Gateway pairing: prefers explicit QR bootstrap over stale Tailscale auth

**Session & Routing**
- Telegram/sessions: fixed topic-scoped session initialization when MessageThreadId omitted
- Thread routing: preserves agent announce delivery targets across threads
- Session model persistence: survives catalog-backed reloads without provider prefix corruption

**Config & Credentials**
- Config validation: surfaces actual offending fields for union schema failures
- Token redaction: improved in Gmail watcher and other auth paths
- OpenAI/Codex OAuth: fixed scope rewriting that broke sign-ins

**Exec Approval & Agent Control**
- CLI/exec policy: new `openclaw exec-policy` command for local approvals management
- Agents/strict agentic: opt-in execution contract for GPT-5 family

### Recommendation

**UPDATE**

Reason: Multiple security keywords (SSRF, security hardening) + critical infrastructure fixes (gateway startup, session routing, Telegram support) warrant immediate upgrade.

---

*Monitored by OpenClaw Release Monitor • Daily Briefing at 6:15 AM*
