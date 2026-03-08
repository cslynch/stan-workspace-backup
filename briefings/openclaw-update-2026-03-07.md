## OpenClaw Update Available

**Version:** 2026.3.2 (current: 2026.2.6)  
**Released:** March 3, 2026

### Relevant Changes

**Security & Infrastructure:**
- Security/Web tools SSRF guard: DNS pinning for untrusted web_fetch; env-proxy bypass requires explicit opt-in
- Security/ACP sandbox inheritance: Reject ACP spawns from sandboxed requesters; prevent sandbox-boundary bypass
- Security/Node exec approvals: Validate approval-bound cwd immediately before execution; escape regex metacharacters in path patterns
- Secrets/SecretRef coverage: Expand SecretRef support across 64 credential targets including runtime collectors, secret planning/apply/audit flows
- Webhook request hardening: Auth-before-body parsing for BlueBubbles/Google Chat; pre-auth body/time budgets; prevent DoS patterns
- Gateway/WS security: Keep plaintext ws:// loopback-only; explicit break-glass opt-in for private networks
- Gateway/Plugin HTTP hardening: Require explicit auth for plugin routes; add route ownership guards; centralize path matching/auth logic
- Config backups hardening: Enforce owner-only (0600) permissions on rotated backups; clean orphan files

**Telegram Enhancements:**
- Default streaming to `partial` (from `off`) for new setups
- Use sendMessageDraft for private preview streaming
- Add disableAudioPreflight for group/topic mention-detection
- Improve models picker callbacks (handle long buttons via compact payloads)
- Guard implicit mention forum handling (exclude system messages)

**Gateway & Config:**
- TLS pairing: Allow authenticated local gateway-client backend self-connections to skip device pairing in Docker/LAN
- Config validation: New `openclaw config validate` command with detailed error paths
- Control UI basePath: Fix webhook passthrough for non-read methods

**Session & Routing:**
- Sessions/Attachments: Add inline file attachment support for sessions_spawn (subagent runtime)
- Slack/session routing: Keep top-level channel messages in shared session when replyToMode=off
- Feishu/topic session routing: Use thread_id as fallback when root_id absent; force thread replies

**Critical Fixes:**
- ACP dispatch now defaults to enabled (previously required opt-in)
- Sandbox workspace mount permissions: Make primary /workspace read-only when workspaceAccess ≠ rw
- Sandbox path validation: Map container workdir paths back to host workspace

### Recommendation

**UPDATE** — Multiple security patches, credential handling improvements, and critical sandbox/SSRF hardening. Essential for production deployments.
