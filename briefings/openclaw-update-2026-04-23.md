## OpenClaw Update Available

**Version:** 2026.4.21 (current: 2026.2.6)  
**Released:** April 22, 2026

### Relevant Changes

- **Security/SSRF:** Added SSRF guards to qqbot, BlueBubbles, and Slack channels; blocked MINIMAX_API_HOST env injection; hardened workspace `.env` loading to block OPENCLAW_* key exposure
- **Security/Auth:** Stricter owner identity enforcement for owner-enforced commands; device pairing scope/role restrictions; credential SecretRef resolution fixes
- **Gateway/TLS:** Extended config mutation guards to prevent rewrite of operator-trusted paths (auth, TLS, plugin trust, SSRF policy)
- **Telegram:** Raised polling watchdog threshold from 90s to 120s for long-running operations; improved polling stall detection with client-side timeouts
- **Config/Routing:** Session key enforcement, message delivery routing precision, allowlisting hot-reload improvements
- **Credentials/Session:** SecretRef resolution for bundled providers (Exa, Gemini, Kimi, Perplexity, Tavily, Grok); session override handling improvements
- **Exec/Plugins:** MCP env hardening (NODE_OPTIONS blocking), plugin dependency repair for packaged installs

### Recommendation

**UPDATE** — Security-focused release with SSRF guards, credential handling improvements, and critical gateway auth/TLS hardening. High relevance to Telegram integration and infrastructure stability.

