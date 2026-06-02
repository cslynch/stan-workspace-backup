## OpenClaw Update Available

**Version:** v2026.6.1-beta.1 (current: 2026.2.6)  
**Released:** June 1, 2026  
**Status:** Beta - Under Review

### Relevant Changes

**Infrastructure & Reliability:**
- Gateway/Web Fetch: Bounded dispatcher cleanup after request timeouts; timed-out fetches now return tool errors cleanly
- Gateway/session state: Harden MCP loopback tool schemas, carry session UUIDs on interactive dispatch events
- Agents/TUI: Restore in-flight TUI run switch-back behavior, guard vanished workspaces, keep lightweight isolated subagents lightweight

**Telegram & Channels:**
- Telegram: Message-tool progress rendering fixes; drafts now stay visible
- Telegram: Cap Telegram request/retry timers for more stable mobile delivery
- Channels: Store inbound queues in SQLite; migrate iMessage monitor state to SQLite-backed tracking
- Channels: Preserve long Feishu streaming replies, preserve colon-prefixed slash commands in mention parsing

**Session & Config Management:**
- Sessions: Accept hidden `sessions_send` body aliases before validation
- Config: Skip unresolved shell references in state-dir dotenv files; keep post-upgrade JSON stable
- Config/auth: Write auth profiles atomically, add force re-login recovery

**Security & Credentials:**
- Security/Config: Reject unsafe OAuth/token lifetimes, retry-after delays, response body sizes, sandbox observer token TTLs
- Agents/auth: Preserve workspaces during state-only uninstall, compact before oversized turns for recovery
- Skills: Skip disabled skill env overrides from stale persisted snapshots so disabled skill `apiKey` SecretRefs cannot abort turns

**Exec & Approval:**
- Agents/Codex: Stream app-server final-answer partials to live reply previews; prefer real tool results over synthetic repair output

### Keyword Match Summary
- ✓ Telegram (Codex, channels, mobile, delivery)
- ✓ Gateway (dispatcher, runtime state, chat failures, WebSocket)
- ✓ Session (metadata, bindings, routing, `sessions_send`)
- ✓ Config (parsing, behavior, auth profiles, routing)
- ✓ Security (OAuth/token lifetimes, sandbox token TTLs, unsafe config rejection)
- ✓ Credential (auth profiles, SecretRef plugin manifests, OAuth endpoints)
- ✓ Exec approval (app-server tool result handling; prefer real tools over repair output)

### Recommendation

**REVIEW** — This is a beta release with infrastructure, security, and Telegram/session/credential changes. Key updates touch:
- Gateway infrastructure reliability (timeouts, SQLite state persistence)
- Telegram message rendering and request timers
- Session metadata and auth profile handling
- Security-relevant config parsing (OAuth lifetimes, token bounds)
- Credential/SecretRef safety (disabled skill env overrides)

**Next steps:**
- This is a pre-release; test in non-production first
- Verify security config changes align with your deployment
- Monitor Telegram delivery if actively used
