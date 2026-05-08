## OpenClaw Update Available

**Version:** v2026.5.6 (current: 2026.2.6)  
**Released:** May 6, 2026  
**Status:** Ready for review

### Relevant Changes

- **Telegram/Codex**: Message-tool progress rendering fixes; drafts now stay visible and tool progress renders once per tool instead of duplicating
- **Gateway/Web Fetch**: Bounded dispatcher cleanup after request timeouts; timed-out fetches now return tool errors cleanly instead of leaving Gateway tool lanes active
- **Exec Approvals**: Windows compatibility fix for rename-overwrite on `exec-approvals.json`; falls back to guarded copy while preserving symlink and permission safeguards
- **Config/Routing Revert**: OAuth route changes from v2026.5.5 reverted; if your default model changed, run `openclaw models set openai-codex/gpt-5.5 && openclaw config validate` to restore Codex OAuth routing

### Recommendation

**REVIEW** — Changes touch Telegram channel functionality, Gateway infrastructure reliability, credential handling, and config routing. The OAuth revert indicates the prior patch may have affected some setups; check your current routing if you're on 2026.5.5.

**Next steps:**
- Review the [recovery docs](https://docs.openclaw.ai/providers/openai#check-and-recover-codex-oauth-routing) if needed
- Test in non-production first if actively using Codex routes
