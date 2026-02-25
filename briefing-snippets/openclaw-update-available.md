## OpenClaw Update Available
Version: 2026.2.23 (current: 2026.2.6)
Released: February 24, 2026, 5:41 AM CT

### Relevant Changes

**Security (6 fixes):**
- Config key redaction in `config.get` snapshots (env.*, skills.entries.*.env.*)
- Exec: Detect and require approval for obfuscated commands
- ACP: Require trusted core tool IDs, scope read auto-approval to working directory
- Skills: XSS prevention in openai-image-gen HTML gallery + symlink hardening
- OTEL: Redact API keys, tokens, credentials from logs before export
- CI: Pre-commit security hooks (private-key detection, dependency auditing)

**Infrastructure:**
- **BREAKING:** browser.ssrfPolicy defaults to `dangerouslyAllowPrivateNetwork=true` (migrate with `openclaw doctor --fix`)
- Gateway: Strict-Transport-Security header support for HTTPS deployments
- Gateway: WebSocket DoS protection (close repeated post-handshake floods, sample logs)
- Gateway: Restart health checks (avoid false stale-process kills on launchd/systemd)
- Sessions: Cron maintenance hardening + disk-budget controls
- Sessions: Canonicalize mixed-case session keys + migrate legacy variants

**Telegram (3 fixes):**
- Reactions: Soft-fail on policy/token/emoji/API errors, snake_case message_id
- Polling: Scope persisted offsets to bot identity, prevent cross-token bleed
- Reasoning: Suppress reasoning-only delivery when `/reasoning off` active, block text leakage

**Other Relevant:**
- Anthropic: Skip context-1m beta for OAuth tokens to prevent 401 auth failures
- Agents: Per-agent `params` overrides for cache behavior tuning
- Agents: Bootstrap file snapshot caching to reduce prompt-cache invalidations
- Config: Path traversal hardening (reject prototype-key segments)

### Recommendation
**UPDATE** — Ship immediately.

Rationale: 6 security fixes + BREAKING SSRF policy change + critical infrastructure hardening (gateway, session store, Telegram polling). No blocking ignore-list items.
