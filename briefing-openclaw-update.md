## OpenClaw Update Available
**Version:** 2026.5.16-beta.4 (current: 2026.2.6)
**Released:** May 17, 2026
**Type:** Beta

### Relevant Changes
- **Security:** Exec approvals now bind to executable realpath, preventing symlink-based approval retargeting (#45595)
- **Security/Audit:** New `security.audit.suppressions` for intentional findings management
- **Telegram:** Fixed account list defaults, media delivery (forceDocument), mention patterns in media-only messages
- **Gateway/Performance:** Session usage refresh in background, startup benchmarking improvements
- **Gateway/Exec Approvals:** Symlink attack mitigation with path allowlist binding
- **Sessions:** Manual user turns prioritized over queued cron/maintenance
- **Credentials:** Improved missing API key errors with credential source details
- **Anthropic:** Reasoning content extraction in assistant replay, Vertex provider fixes
- **Config:** CLI/config improvements, model/auth provider ordering

### Ignored (Not Relevant)
Discord, Slack, Feishu, macOS, Web UI, i18n, docs, CI, test

### Recommendation
**UPDATE** — Contains security fixes (symlink attack prevention, audit controls), critical Telegram/Gateway improvements, and session handling enhancements relevant to your stack.
