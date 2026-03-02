## OpenClaw Update Available

**Version:** 2026.2.26 (current: 2026.2.6)

**Released:** Feb 27, 2026

**Relevant Changes:**

**🔒 Security Fixes:**
- Node exec approvals hardening (structured argv, versioned bindings, forwarding validation)
- Plugin channel HTTP auth (normalized paths, traversal prevention, fail-closed handling)
- Gateway node pairing anti-spoofing (platform/deviceFamily metadata pinning)
- Sandbox/workspace boundary hardening (symlink validation, escape prevention)
- Config includes hardening (verified-open, hardlink rejection, size guardrails)
- SSRF-guarded media fetch paths

**💬 Telegram Improvements:**
- DM allowlist runtime inheritance enforcement
- sendChatAction 401 backoff + typing suppression
- Webhook startup & ephemeral binding
- Inline buttons in groups
- Streaming preview finalization

**⚙️ Gateway & Config:**
- Agents routing CLI (bind/unbind account-scoped routes)
- Gateway TLS probe for LAN binds
- Gateway auth mode CLI parity
- Startup bind visibility warning
- Doctor allowlist safety checks + auto-fix
- Auth profile alias normalization

**Recommendation:** **UPDATE**

*Multiple security fixes + critical infrastructure improvements. This is a substantial release (20 patch versions from 2026.2.6). Plan upgrade at next maintenance window.*
