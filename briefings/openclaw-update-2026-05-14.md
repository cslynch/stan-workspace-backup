## OpenClaw Update Available

**Version:** 2026.5.12-beta.7 (current: 2026.2.6)  
**Released:** May 14, 2026 @ 09:39 AM CT  
**Status:** Beta

### Relevant Changes

#### 🔒 Security Fixes (High Priority)
- **Credential handling:** Stop inferring provider env-var markers from broad regex patterns; resolve config-backed `apiKey` values only through structured env SecretRefs (`secrets.providers[id]` / `secrets.defaults`). Prevents accidental credential leakage from unrelated env vars.
- **Sandbox hardening:** Include Windows `USERPROFILE` in sandbox blocked home roots, denying credential-bearing binds (`.codex`, `.openclaw`, `.ssh`) even when `HOME` points elsewhere.
- **TLS hardening (macOS/Gateway):** Require system TLS trust before pinning first-use direct `wss://` gateway certificates; honor `gateway.remote.tlsFingerprint` for remote node-mode sessions.

#### 📡 Telegram Plugin Fixes
- Keep Bot API polling alive during event-loop stalls via isolated worker with durable local spool. Fixes polling death on stalls.
- Detect polling stalls from `getUpdates` liveness only (not outbound API calls).
- Discard legacy long-poll offsets tied to old tokens; fixes silent message skips on token rotation.
- Delete tool-progress drafts before final answers; fixes orphaned progress bubbles.

#### 🚪 Gateway & Session Management
- Gateway protocol: Require v4 clients, stream explicit chat `deltaText`/`replace` frames for SDK compatibility.
- Session history: Carry monotonic transcript sequence through live updates; refresh SSE when sequence stale.
- ACP spawn-child sessions: Proper classification in `openclaw sessions` and status output.
- Agent sessions: Create configured main sessions before first `sessions_send` to prevent message failures to agents that haven't started.

#### 🔐 Exec Approval & Device Pairing (Security)
- Require approval for setup-code device pairing.
- Require explicit browser device pairing.
- Require Control UI pairing before proxy-scoped access.
- Reject truncated exec approval commands.
- Enforce inline shell wrapper payload matching.
- Limit hook CLI tool authority; require admin scope for node device token management.
- Harden trusted-proxy source validation.

#### ⚙️ Config & Anthropic
- Config: Serialize and retry semantic mutations centrally (safe concurrent changes).
- Anthropic/Claude: Reseed CLI fresh-session retries from bounded OpenClaw transcript history; prevents conversation amnesia on session rotation.
- Codex: Treat selectable OpenAI models as runtime requirements during plugin auto-enable and startup planning.

#### 📊 Additional Reliability Fixes
- Process execution: Collapse case-insensitive duplicate child env keys on Windows (PATH shadowing).
- Auth: Reclaim dead-owner stale file locks before retrying locked writes (OAuth refresh wedging).
- Media fetch: Skip buffering for bodyless responses (HEAD, 204).
- Browser CLI: Request existing `operator.admin` gateway scope explicitly (avoid unnecessary upgrade loops).

### Recommendation

**UPDATE** — This is a **beta release** with significant **security hardening** (credentials, sandbox, TLS), critical **infrastructure fixes** (gateway session management, Telegram polling reliability), and **exec approval tightening**. Especially important for Telegram-heavy users and production deployments.

⚠️ *Note: Beta tag; test in non-critical environments first if you prefer stable channels.*
