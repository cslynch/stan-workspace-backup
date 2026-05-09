## OpenClaw Update Available
Version: 2026.5.7 (current: 2026.2.6)
Released: May 7, 2026

Relevant changes:
- **Telegram** authorization: honor `accessGroup:*` sender allowlists for DMs, groups, native commands, and callback authorization (Fixes #78660)
- **Telegram** polling: polling watchdog now properly tied to `getUpdates` liveness (Fixes #78422)
- **Gateway/sessions**: clear cached skills snapshots on `/new` and `sessions.reset` for visibility after skill changes (Fixes #78873)
- **Gateway/sessions**: persist new generated transcript file on daily session rollover (Fixes #78607)
- **Exec credential security**: Tavily tool credentials now resolved from runtime config, preventing `exec` SecretRef-backed API keys from reaching tools unresolved (Fixes #78610)
- **Config validation**: improved model provider normalization and OAuth route recovery

Recommendation: REVIEW

Key note: Credential handling fix in exec approval paths warrants attention. Telegram auth allowlists fix may affect multi-group deployments.
