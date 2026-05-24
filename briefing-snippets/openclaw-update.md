## OpenClaw Update Available

**Version:** 2026.5.22-beta.1 (current: 2026.2.6)  
**Released:** 2026-05-23 09:59:56 UTC  
**Status:** Beta prerelease (v2026.5.22-beta.1)

### Relevant Changes

**Security & Infrastructure:**
- Release/security: npm shrinkwrap for root package and OpenClaw plugins; locked dependency graphs for public installs
- Provider auth-state prewarm optimizations (~4,100× faster model listing: 20s → 5ms)
- Gateway startup plugin registry reuse to avoid redundant loading

**Telegram & Messaging:**
- Telegram multi-agent groups support
- Slack and Telegram ack reactions
- Telegram markdown table mode fix for chunked sends

**Session & Gateway Reliability:**
- Session transcript archive failure visibility during `/new` rotation
- Parallel OpenAI-compatible tool-call deltas fix (corrupted streamed arguments)
- Fresh session overrides & metadata preservation during concurrent writes
- Sub-agent bootstrap context limited to `AGENTS.md` + `TOOLS.md` for delegation workers
- TUI message-tool reply mirroring for internal-ui agents

**Credentials & Configuration:**
- Custom provider API key handling for media/image/video/music generation tools
- SecretRef setup guidance for password-store
- Per-model `api` and `baseUrl` override support

**Exec & Process:**
- Codex code-mode boundary clarification
- `/exec host=node` routing for node-targeted commands
- OpenClaw exec/process availability on node hosts

**Performance Improvements:**
- File-descriptor exhaustion fix (EMFILE) on multi-agent gateways
- Bounded session-picker search with Load More pagination
- Auto-compaction write-lock watchdog timeout binding
- Cron network retry support (EAI_AGAIN, EHOSTUNREACH, ENETUNREACH)

### Recommendation: **REVIEW**

This is a beta release with **significant infrastructure improvements** (security/auth, performance, reliability) that affect gateway stability, session management, and provider integrations. However, beta status and version distance from stable 2026.2.6 require testing before production deployment. Suitable for staging/testing environments now; defer main production upgrade until stable release is published.
