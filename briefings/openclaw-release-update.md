## OpenClaw Update Available

**Version:** 2026.3.2 (current: 2026.2.6)  
**Released:** March 3, 2026

**Relevant changes:**
- SSRF guards for web_fetch with proxy env vars
- Webhook request hardening (auth-before-body, pre-auth budgets)
- Gateway/Subagent TLS pairing improvements (allows authenticated local self-connections)
- WS security: plaintext `ws://` loopback-only by default
- Telegram streaming defaults, DM streaming, voice mention gating
- Sessions/Attachments: inline file support for sessions_spawn
- Config validation command, heartbeat model reload
- ACP sandbox inheritance security (reject bypasses)
- Node exec approval hardening

**Recommendation:** **UPDATE**

Justification: Critical security fixes (SSRF guards, webhook hardening, sandbox bypass prevention, prompt spoofing), essential gateway infrastructure improvements (TLS, auth enforcement), and production-ready Telegram enhancements.
