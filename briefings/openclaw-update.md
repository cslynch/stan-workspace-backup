## OpenClaw Update Available

**Version:** 2026.2.26 (current: 2026.2.6)  
**Released:** February 27, 2026  
**Recommendation:** UPDATE

### Relevant Changes

#### Security (Critical)
- **Node exec approvals:** Require structured `commandArgv` approvals for `host=node`, enforce versioned `systemRunBindingV1` matching for argv/cwd/session/agent/env context with fail-closed behavior on missing/mismatched bindings.
- **Plugin channel HTTP auth:** Normalize protected `/api/channels` path checks against canonicalized request paths (case + percent-decoding + slash normalization), resolve encoded dot-segment traversal variants, fail closed on malformed `%`-encoded channel prefixes.
- **Gateway node pairing:** Pin paired-device `platform`/`deviceFamily` metadata across reconnects and bind those fields into device-auth signatures to prevent reconnect metadata spoofing.
- **Sandbox path alias guard:** Reject broken symlink targets by resolving through existing ancestors, failing closed on out-of-root targets to prevent workspace escapes.
- **Workspace FS boundary aliases:** Harden canonical boundary resolution for non-existent-leaf symlink aliases while preventing first-write workspace escapes via out-of-root symlink targets.
- **Config includes:** Harden `$include` file loading with verified-open reads, reject hardlinked include aliases, enforce file-size guardrails.
- **Exec approvals forwarding:** Prefer turn-source channel/account/thread metadata when resolving approval delivery targets.
- **Pairing multi-account isolation:** Enforce account-scoped pairing allowlists and pending-request storage across core + extension message channels.

#### Gateway & Infrastructure
- **TLS daemon probing:** Use `wss://` and forward local TLS certificate fingerprint for TLS-enabled gateway daemon probes.
- **Gateway bind visibility:** Emit startup warning when binding to non-loopback addresses.
- **Docker/GCP onboarding:** Reduce OOM risk, reuse existing gateway tokens, auto-bootstrap Control UI origins for non-loopback Docker binds.
- **CLI Gateway auth:** Align `gateway run --auth` parsing with supported modes (none, token, password, trusted-proxy).
- **Podman default bind:** Change default gateway bind from `lan` to `loopback` for security.

#### Session & Routing
- **Sessions cleanup:** Add `openclaw sessions cleanup --fix-missing` to prune store entries with missing transcript files.
- **Agents/Routing CLI:** Add `openclaw agents bindings`, `bind`, and `unbind` for account-scoped route management.
- **Cron/Hooks isolated routing:** Preserve canonical `agent:*` session keys in isolated runs to prevent double-prefixing.
- **Channels multi-account config:** Properly migrate existing single-account values into `channels.<channel>.accounts.default` when adding new accounts.

#### Telegram (Channel-Specific)
- **DM allowlist inheritance:** Enforce `dmPolicy: "allowlist"` `allowFrom` requirements with effective account-plus-parent config.
- **sendChatAction retry loops:** Add bounded exponential backoff after repeated 401 failures to prevent bot deletion via abuse enforcement.
- **Webhook startup:** Allow `webhookPort: 0` for ephemeral listener binding with clearer logging.
- **Inline buttons in groups:** Allow callback-query button handling in groups when policy authorizes sender.
- **Streaming preview:** Prime pending preview text with final answer before flush to avoid stale fragments.

#### Config & Credentials
- **Auth profiles:** Normalize `auth-profiles.json` alias fields (`mode -> type`, `apiKey -> key`) before credential validation.
- **Agent-level models:** Preserve agent-level provider `apiKey` and `baseUrl` during merge-mode `models.json` updates.
- **Doctor allowlist safety:** Reject `dmPolicy: "allowlist"` configs with empty `allowFrom`, add Telegram account-level validation.

#### Additional Highlights
- **External Secrets Management:** Full `openclaw secrets` workflow (audit, configure, apply, reload) with runtime snapshot activation.
- **ACP/Thread-bound agents:** Make ACP agents first-class runtimes for thread sessions.
- **Codex WebSocket transport:** Make `openai-codex` WebSocket-first by default.
- **Android nodes:** Add device capability, device.status, device.info commands, and notifications.list support.

### Why Update Now
- **Multiple critical security fixes** affecting node approvals, gateway routing, path traversal, and credential handling.
- **Gateway infrastructure hardening** for TLS, multi-account isolation, and auth.
- **Session/routing stability** improvements for account-scoped management.
- **Telegram reliability** fixes for DM handling and retry loops.

---
*Briefing generated at 5:50 AM CT on February 27, 2026*
