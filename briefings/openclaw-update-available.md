## OpenClaw Update Available
**Version:** 2026.5.9-beta.1 (current: 2026.2.6)
**Released:** 2026-05-09 13:32 UTC
**Status:** Beta — pre-release testing

### Relevant Changes
- **Telegram:** Fixed grammY API throttler sharing (prevents draft preview quota conflicts), reasoning preview defaults, poll cap handling, streaming message continuity
- **Gateway:** Task ledger RPC stabilization, atomic session-store writes (reduces starvation on slow filesystems), restart deferral skip option, improved reload handling
- **Sessions:** Performance optimizations (avoid full-array sorting), transcript-backed historical lineage tracking, ACPX lease selection
- **Exec Approval:** ACP bridge now relays Gateway exec approval prompts to ACP client session handlers before resolving approval (improves approval workflow)
- **Config/Models:** Model catalog registration unification, Qwen thinking format support, Amazon Bedrock service tier parameter support
- **Routing:** Slack implicit-conversation channel routing to thread-scoped sessions, Discord voice realtime modes (agent-proxy, STT/TTS, bidi consult)

### Notable Omissions (filtered)
- Discord voice/streaming (extensive, but not core infrastructure)
- Feishu external plugin (moving to ClawHub)
- Windows-specific fixes (not applicable here)

### Recommendation
**REVIEW** — This is a beta release with no explicit security vulnerabilities, but includes significant Gateway/session/approval-flow infrastructure changes. Worth testing in staging before production push, especially if you rely on:
- Exec approval workflows (ACP relaying changes)
- High-volume Telegram draft previews
- Session roster performance on slow storage

Safe to defer to stable release unless you need specific telegram/gateway fixes.
