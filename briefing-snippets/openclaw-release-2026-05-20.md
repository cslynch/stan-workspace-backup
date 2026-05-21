## OpenClaw Update Available

**Version:** 2026.5.19-beta.2 (current: 2026.2.6)  
**Released:** 2026-05-19  
**Type:** Prerelease (beta)

### Relevant Changes

**Telegram & Messaging:**
- Native DM draft previews for transient tool progress
- Forum topic routing improvements (prevents sibling topic traffic blocking)
- Message delivery logging with account, chat, message metadata

**Gateway & Config:**
- Config reload metadata exposure (distinguishes restart-required vs hot-reloadable fields)
- Startup probe optimization with reduced ready latency
- WebChat chunk limit overrides

**Security & Infrastructure:**
- HTTPS managed forward-proxy support with scoped TLS CA trust
- Anthropic provider fixes (image capability preservation for Claude models)

**Session & Routing:**
- Improved delivery route metadata storage and deprecation of ad hoc fields
- Forum topic traffic routing serialization fixes

### Recommendation

**REVIEW** — Contains meaningful infrastructure and Telegram improvements, but is a prerelease (beta.2). Suitable for staging evaluation; defer to stable release unless you need specific beta fixes.

---
*Generated: 2026-05-20 05:50 CT*
