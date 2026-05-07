## OpenClaw Update Available

**Version:** 2026.5.6 (current: 2026.2.6)  
**Released:** May 6, 2026  
**Status:** Stable Release

### Relevant Changes

#### Security & SSRF Hardening
- **Browser/SSRF:** Enforce current-tab URL navigation policy before debug/export/read routes to prevent blocked-tab reads (#75731)
- **OpenAI Codex:** SSRF-guarded provider requests now inherit OpenClaw's undici IPv4/IPv6 fallback policy for better DNS resilience (#76857)
- **Network Proxy:** Preserve target TLS hostname validation for Node HTTPS through managed HTTP proxy; Discord-style CONNECT traffic now validates against real certificate host (#74809)

#### Gateway & Infrastructure
- **Gateway/startup:** Log canvas host mount only after HTTP server has bound; prevent premature mount reporting
- **Canvas host:** Preserve Gateway TLS scheme in browser canvas host URLs and startup logs; prevent insecure canvas links on HTTPS gateways
- **Gateway/validation:** Isolate validation files, ignore unrelated startup logs in request-trace coverage; reduce false CI failures
- **Gateway/sessions:** Bound default `sessions.list` RPC responses and report truncation metadata; prevent large Slack-heavy stores from forcing unbounded row construction (#77062)
- **Gateway/performance:** Multiple startup optimizations: lazy-load discovery, defer timers until after readiness, fast-path bundled plugin metadata

#### Credential & Authentication
- **Google Chat:** Create isolated Google auth transport per client; prevent interceptor mutations from accumulating across webhook verification and token clients
- **WhatsApp:** Route login QR output through injected runtime; capture all login output instead of losing QR behind stdout writes (#76213)
- **Telegram:** Keep status checks pointed at active chat; prevent reporting stale DM conversation (#76708)

#### Telegram Channel
- **Forum topics:** Accept plugin-owned numeric forum-topic targets in message tool; support Telegram forum-topic metadata (#77137)
- **Media optimization:** Send in-limit original images when optional image optimization unavailable; Telegram MEDIA replies no longer fail without Sharp (#77081)
- **Media groups:** New tunable `channels.telegram.mediaGroupFlushMs` for album buffering (default 500ms)

#### Configuration
- **Config validation:** Gateway startup and hot reload now fail closed on invalid config; `openclaw doctor --fix` owns repair
- **Doctor/config:** Apply safe legacy migrations even when unrelated validation issues exist (#76800)

### Recommendation

**UPDATE** — Multiple security hardening improvements (SSRF, TLS validation, auth isolation) plus significant gateway stability and performance enhancements. Recommended for production environments.

---
