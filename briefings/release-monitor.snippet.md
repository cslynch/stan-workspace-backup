## OpenClaw Update Available

**Version:** v2026.5.20 (current: 2026.2.6)  
**Released:** May 21, 2026  
**Status:** Review recommended

### Relevant Changes

**Security & Credentials:**
- **Doctor**: Now warns when `openclaw.json` stores plaintext secret-bearing config fields, including model provider API keys and sensitive provider headers — audit your config file
- **Infra/Secrets**: Restored fail-closed contract for credential loaders so symlinked credential files are now rejected (Telegram, LINE, Zalo, IRC, Nextcloud Talk tokens)

**Exec Approvals & Session Management:**
- **Exec Approvals**: Changed approval allowlist compatibility; skill files must be loaded with the read tool and only the real skill executable is auto-allowed
- **Session/Agents**: Improved message-tool turn handling and session status reporting; fixed stale transcript artifact pollution

**Gateway & Config:**
- **Gateway/Agents**: Use agent's `identity.name` in Gateway summaries when `agents.list[].name` is unset
- **Config/Routing**: OpenRouter now honors provider-level `params.provider` routing policy; added `agents.list[].experimental.localModelLean` for per-agent lean mode
- **CLI/Update**: Fixed protocol skew handling during updates when multiple Node binaries are present

**Infrastructure:**
- **Cron**: Separated main-session scheduled work onto a cron-owned wake lane so background tasks no longer block human chat
- **Doctor**: Enhanced validation warnings for MCP server tools and stale provider model config

### Recommendation

**REVIEW** — Security-relevant warning about plaintext secrets in config, improved credential handling, and changes to exec approval mechanics. Recommended actions:

1. Run `openclaw doctor` to check for plaintext secrets in your `openclaw.json`
2. Verify symlinked credential files if using Telegram or other supported channels
3. Review exec approval changes if you have custom approval scripts
4. Test in non-production if actively managing provider routing or config

**Installation:** `npm install -g openclaw@2026.5.20` (or `pnpm up openclaw`)
