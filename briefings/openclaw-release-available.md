## OpenClaw Update Available

**Version:** v2026.5.19-beta.1 (current: 2026.2.6)  
**Released:** May 18, 2026  
**Status:** Beta

### Relevant Changes

**Gateway & Configuration:**
- Gateway/config: expose config lookup reload metadata to distinguish restart-required, hot-reloadable, and no-op fields before applying edits (#81612)
- Gateway/sessions: clear stored CLI provider resume bindings on non-subagent `/reset` for fresh provider conversation (#83448)
- Gateway/sessions: rotate failed agent sessions when transcript file is missing (#83553)
- Gateway performance: added restart readiness benchmark tooling
- Gateway startup: overlap plugin-service startup with channel sidecars to reduce restart latency (#83301)

**Session & Routing:**
- Agents/subagents: improved collect-mode announce queues with compatible same-route batching (#83577)
- Plugins/subagents: store channel delivery routes as canonical session metadata (deprecates ad hoc hook delivery-origin fields)
- Sessions: link isolated scheduled task runs to their stable cron session for status tracking (#83606)

**Telegram Enhancements:**
- Add allowlisted native DM draft previews for transient tool progress (#83622)
- Preserve topic IDs across requester-agent handoff for forum topic delivery (#83556)
- Log successful outbound text/media with operation metadata (#83247)
- Keep tool progress visible without duplicating into transcripts (#83631)

**Infrastructure:**
- Anthropic: preserve native image input for current Claude model rows (#83756)
- Proxy: support HTTPS managed forward-proxy endpoints with scoped CA trust (`proxy.tls.caFile`) (#79171)
- Browser: enforce URL allowlist checks for `/act` evaluate/batch actions and `/highlight` routes (#78523)
- CLI: enforce documented Node.js 22.19 runtime floor

**Other Notable Fixes:**
- Memory/search: bounded rowid batches prevent main-thread pinning on large chunk tables (#81172)
- Multiple Anthropic provider, Discord integration, and media handling fixes

### Recommendation: **UPDATE**

**Rationale:** Infrastructure-level improvements to gateway config handling, session management, and routing are relevant for stability and reliability. Gateway config reload metadata (#81612) is particularly valuable for avoiding unnecessary restarts during configuration updates. Beta status is acceptable for infrastructure improvements.

---
*Updated by Release Monitor at 2026-05-19 05:50 CT*
