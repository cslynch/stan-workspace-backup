## OpenClaw Update Available

**Version:** 2026.5.26 (current: 2026.2.6)  
**Released:** 2026-05-27  
**Type:** Stable release

### Relevant Changes

- **Security hardening:** Group prompt text isolation from system prompts, unsafe Node runtime env override blocking, Tailscale no-auth exposure rejection, node/device-role approval admin enforcement
- **Gateway & session improvements:** Performance optimizations for session metadata reads, auth env snapshots, plugin metadata fingerprinting, stable metadata caching
- **Telegram reliability:** `sendMessage` actions now use durable outbound delivery
- **Anthropic support:** Bare direct model ID support, improved Claude CLI OAuth overlays, thinking param handling
- **Channel delivery:** iMessage approval prompt deduplication, Slack final-reply preservation, Matrix mention handling, Discord guild validation tightening

### Recommendation: **REVIEW**

**Rationale:** Security fixes (content boundaries, approval enforcement, Tailscale) + Gateway/session infrastructure improvements + Telegram delivery stability warrant review before production deployment. Stable release, ready for testing.

---

**Also available:** v2026.5.27-beta.1 (latest beta, contains same fixes + Pixverse video generation provider, DeepInfra catalog improvements)
