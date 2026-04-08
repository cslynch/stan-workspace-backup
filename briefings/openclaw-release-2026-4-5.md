## OpenClaw Update Available
Version: 2026.4.5 (current: 2026.2.6)
Released: April 6, 2026
Relevant changes:
- **Security:** Plugin allowlist enforcement, SSRF bypass blocking, inherited env override cleanup (Claude CLI), device pairing scope fixes
- **Config:** Legacy public config alias removal (talk.voiceId, browser.ssrfPolicy, etc.) with migration support
- **Gateway:** Startup improvements (PID recycling detection, mode defaults), device auth scope binding, plugin route security
- **Telegram:** Model picker fixes, voice transcription restore, reasoning preview control, native command menu updates
- **Anthropic:** Claude CLI backend removed from new onboarding, legacy profiles kept runnable
- **Exec Approvals:** APNs/iOS support, Matrix-native prompts, reusable allow-always approvals
- **Session/Routing:** Reply lifecycle ownership unification, live model switching fixes, session rotation handling
- **Providers:** Shared request transport overrides (auth, proxy, TLS controls), device-token scope reuse fixes
- **Other:** Prompt caching improvements, memory/dreaming enhancements, multi-language control UI
Recommendation: UPDATE