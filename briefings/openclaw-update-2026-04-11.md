## OpenClaw Update Available

**Version:** 2026.4.10 (current: 2026.2.6)  
**Released:** April 11, 2026, 02:43 UTC  
**Recommendation:** UPDATE

### Relevant Changes

**Security Hardening:**
- Browser/security: strict SSRF defaults, hostname allowlists, interaction-driven redirects, subframes, CDP discovery
- Security/tools: exec preflight reads, host env denylisting, node output boundaries, plugin install scanning, Gmail token redaction
- Telegram/security: tighten `allowFrom` sender validation, keep `/whoami` allowlist in sync

**Exec & Approval:**
- CLI/exec policy: new `openclaw exec-policy` command (show/preset/set) for synchronizing `tools.exec.*` config with local approval files

**Gateway & Routing:**
- commands.list RPC: remote gateway clients can discover runtime-native, text, skill, and plugin commands
- Thread routing: preserve Slack, Telegram, Mattermost, Matrix, ACP, restart-sentinel, and agent announce delivery targets

**Session Management:**
- Session fallback: preserve model selection across transient failures
- Model selection: preserve catalog-backed labels, provider-qualified context limits
- Auth profiles: resolve consistently for isolated cron jobs

**Telegram:**
- QA lane: live `openclaw qa telegram` for private-group bot checks
- Security hardening: sender validation, command auth sync

### Why Update

Multiple security hardening passes (SSRF, exec policy enforcement, auth tightening) + critical routing fixes ensure delivery stability across channels (especially Telegram) and proper exec approval policy control. No breaking changes in release notes.
