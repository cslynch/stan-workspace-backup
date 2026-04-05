## OpenClaw Update Available

**Version:** 2026.4.2 (current: 2026.2.6)  
**Released:** April 2, 2026  
**Release Page:** https://github.com/openclaw/openclaw/releases/tag/v2026.4.2

### Relevant Changes

**Security & Infrastructure:**
- TLS/transport policy centralization—request auth, proxy, TLS, and header shaping now unified across HTTP, stream, and websocket paths; blocks insecure TLS/runtime overrides
- SSRF guard enforcement—status probes, image generation, and private-network routing hardened with shared guard validation
- Anthropic routing hardening—native-vs-proxy endpoint classification centralized to prevent spoofed host defaults

**Exec Approvals & Gateway:**
- Gateway/node exec now defaults to YOLO mode (`security=full`, `ask=off`) with approval-file fallbacks aligned
- Windows exec allowlist enforcement restored with quote-aware argument matching
- Exec approvals config validation—invalid `security`, `ask`, `askFallback` values stripped during normalization
- Telegram exec approval button rewrites—`allow-always` callback compaction for Telegram's `callback_data` limits
- Gateway loopback fallback restored; subagent calls pinned to `operator.admin` scope

**Session & Routing:**
- Provider-specific session conversation grammar moved to plugin-owned surfaces; preserves Telegram topic routing and Feishu scoped inheritance
- Subagent/task lifecycle—managed child spawning, sticky cancel intent, bound `api.runtime.taskFlow` seam for trusted authoring

**Configuration:**
- Plugin config migration—Firecrawl `web_fetch` and xAI `x_search` settings moved from legacy core paths to plugin-owned paths; `openclaw doctor --fix` available

### Recommendation
**UPDATE** — Security-critical TLS/transport hardening, SSRF closure, and exec approval infrastructure changes with no breaking changes for your setup.

---
*Briefing generated: 2026-04-04 05:50 CT*
