## OpenClaw Update Available
Version: 2026.6.2-beta.1 (current: 2026.2.6)
Released: June 3, 2026
Relevant changes:
- **Security hardening**: Plugin installs now use operator install policy instead of dangerous-code scanner; rejects corrupt shell snapshots, unsafe exec approval precheck environments, and suspicious gateway startup configs
- **Telegram improvements**: Safer delivery paths with admin writeback controls, streamed-final previews, and exec approval allowlists working with ask:off
- **Gateway & session recovery**: Better handling of session write-lock failures, abandoned Codex startups, and stream-to-parent spawns
- **Config validation**: Data-handling conformance checks and rejection of unsupported policy keys
- **Exec approval**: Hardened approval precheck environments and preserved Telegram DM approval allowlists

Recommendation: **UPDATE**
Rationale: Security improvements around exec approval, plugin install policy, and config validation are critical infrastructure changes for our Telegram-based setup.
