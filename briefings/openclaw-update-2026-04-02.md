## OpenClaw Update Available

**Version:** 2026.4.2 (current: 2026.2.6)  
**Released:** April 2, 2026  
**Changelog:** https://github.com/openclaw/openclaw/releases/tag/v2026.4.2

### Relevant Changes

**🔒 Security & TLS**
- Centralized request auth, proxy, TLS, and header shaping across HTTP/stream/websocket paths
- Blocked insecure TLS and runtime transport overrides
- SSRF guards hardened for image generation and Mattermost probes
- Private-network access inference blocked for custom provider endpoints

**📱 Telegram Improvements** (8+ fixes)
- Exec approval callback payload rewriting for Telegram size limits
- Retry logic with proper idempotency and 429 backoff
- Media MIME type preservation for local Bot API
- Presence handling fixes for self-chat mode

**🌐 Gateway Stability**
- Session kill authorization enforcement (scoped to operator.admin)
- Loopback fallback restoration for paired-device token maps
- Node-pending-work state pruning to prevent indefinite growth
- Pairing requirement fixes for subagent gateway calls

**✅ Exec Approvals**
- Policy value normalization with clean fallback to defaults
- Windows allowlist enforcement with quote-aware arg matching
- Doctor reporting improvements

**🧠 Anthropic**
- Thinking block preservation across replay, cache-control, and context pruning

**⚙️ Config & Plugins**
- JSON5 syntax acceptance in plugin manifests
- OAuth token refresh persistence to survive restarts

**🎯 Session Routing**
- Provider-specific session grammar moved to plugin-owned surfaces
- Telegram topic routing preservation across bootstrap/model-switch/restart

### Recommendation

**UPDATE** — This release contains critical security hardening (TLS/SSRF/auth centralization), important Telegram reliability fixes, and stability improvements to gateway/exec/session handling. Recommended for production environments.
