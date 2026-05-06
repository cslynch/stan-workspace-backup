## OpenClaw Update Available

**Version:** 2026.5.4 (current: 2026.2.6)  
**Released:** May 5, 2026 at 8:24 AM UTC  
**Days behind:** ~88 days

### Relevant Changes

**Security:**
- Browser: enforce strict SSRF current-URL checks before existing-session screenshots
- TLS scheme preservation in Canvas host URLs

**Telegram (Critical):**
- Forum-topic numeric target support
- Media placeholder derivation from MIME metadata (fixes #69793)
- Streaming: reuse preview as first chunk (eliminates transient bubbles)
- Tool-only draft cleanup to prevent lingering `Surfacing...` bubbles
- Forum-topic `requireMention` override support (fixes #49864)
- Reply-dispatch provider runtime stability

**Gateway (Critical):**
- Windows loopback binding fix (127.0.0.1 only, avoids IPv6 dual-stack wedging) - fixes #69674
- Startup performance: deferred non-readiness sidecars, fast-path trusted plugin metadata
- Model-catalog test helpers moved out of hot startup paths
- Provider discovery honors restrictive `plugins.allow` by default

**Exec Approvals (New):**
- Tree-sitter-backed shell command explainer for approval surfaces
- Detects `env -S` split-string risks when combined with other short options
- Unwraps BSD/macOS `env -P` carrier commands
- Treats POSIX `exec` as command carrier for inline eval detection

**Config/Routing:**
- Doctor migrations for legacy group chat config (WhatsApp, Telegram, iMessage)
- WhatsApp Channel/Newsletter explicit outbound targets
- Config block propagation in inline-evaluation contexts

**Session/State:**
- Active-memory: bounded latest-message search (fixes #65309)
- Session routing state cleanup for stale plugin-owned bindings
- Reply-run guard timing fix (eliminates `ReplyRunAlreadyActiveError`) - fixes #77485

### Other Notable Fixes

- Plugins: official externalized npm migrations treated as trusted source-linked installs
- Discord: IPv4 preference for REST/WebSocket (fixes #77398)
- WhatsApp/Telegram: group mention gates and history settings preserved on upgrade
- Model switching: additive allowlist repair command when runtime blocked
- Slack: suppress silent child completion rows from follow-up findings
- Windows: media file fsync before close (fixes attachment open failures)

### Recommendation

**UPDATE** — Security hardening (SSRF), critical Telegram fixes (media, streaming, draft handling), Gateway Windows loopback binding (fixes edge case), exec approval infrastructure, and config migration coverage warrant upgrade.

---
*Briefing generated: 2026-05-05 05:50 CT*
