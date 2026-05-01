## OpenClaw Update Available

**Version:** v2026.4.29-beta.1 (current: 2026.2.6)

**Released:** April 30, 2026 (9:33 AM UTC)

**Type:** Beta release with significant infrastructure and security improvements

### Relevant Changes

**Security & Credential Handling:**
- OpenGrep scanning and GHSA triage policy improvements
- Secrets comparison with timing-safe buffer comparisons (CVE-class fix)
- QQBot debug log sanitization to prevent payload log injection
- HTML tag sanitization in plain-text output handling
- Web-fetch SSRF policy with IPv6 ULA opt-in for trusted proxy stacks

**Telegram Reliability:**
- Proxy/webhook/polling/send resilience improvements
- Retry logic for `setWebhook`, `deleteWebhook` transient failures
- Raw host/network-unreachable Bot API handling
- Quote reply fallback for `QUOTE_TEXT_INVALID` responses
- Long-polling liveness warnings in channel status

**Gateway & Infrastructure:**
- Slow-host startup diagnostics and timeline recording
- Model catalog caching and event-loop readiness checks
- Session recovery and stuck-session diagnostics
- Plugin runtime dependency repairs and cache management
- Packaged plugin reliability improvements

**Credential & Auth Security:**
- OAuth credential handling with per-agent isolation
- Secrets in channel/provider configs kept out of status/doctor paths
- Exec elevated command `messageProvider` routing fix

**Config & Model Management:**
- Model alias resolution in security audits
- Provider-prefixed model ID handling improvements
- Per-model extra params preservation

### Assessment

**Recommendation:** REVIEW

**Rationale:**
- Beta release (prerelease: true) — stable 2026.x versions recommended for production
- Multiple security-class fixes warrant review before deployment
- Telegram reliability improvements are substantial if you rely on Telegram
- Gateway infrastructure improvements may affect performance characteristics

**Action Items:**
1. Review security fixes, especially timing-safe secrets comparison
2. If using Telegram heavily, consider updating for reliability improvements
3. If on older 2026.2.6, defer to next stable release (2026.4.x final) unless security fixes are critical for your setup
4. Check `/exec approval` workflows—Telegram/Discord handling was revised

---

*Checked: April 30, 2026 @ 5:50 AM CT*
