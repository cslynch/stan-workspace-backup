## OpenClaw Update Available
Version: 2026.6.2-beta.1 (current: 2026.2.6)
Released: June 3, 2026
Prerelease: beta.1

Relevant changes:
- **Telegram/Channels**: safer duplicate transcript mirrors, admin writeback, exec approval allowlists fixes (ask:off support)
- **Security/Config**: reject corrupt shell snapshots, suspicious gateway startup configs, unsafe exec precheck env, malformed script limits
- **Gateway/Session**: recover session write-lock release failures, gateway health auth diagnostics, stream-to-parent ACP spawns
- **Anthropic integration**: strip Kimi-incompatible Anthropic cache markers
- **Plugin/Install policy**: operator install policy replaces dangerous-code scanner (security improvement)

Recommendation: **UPDATE**

Rationale: Security hardening (corrupt snapshot rejection, gateway config validation), critical infrastructure improvements (session recovery, gateway diagnostics), and Telegram integration fixes (approval allowlists, admin writeback).
