## OpenClaw Update Available

**Version:** 2026.5.10-beta.5 (current: 2026.2.6)  
**Released:** May 11, 2026 (beta)  
**Type:** Beta release with infrastructure & security improvements

### Relevant Changes

**Telegram & Messaging**
- Forced document delivery for video media
- Thinking defaults display in native `/status` and `/think` menus
- Telegram gateway credential leasing automation

**Gateway & Infrastructure**
- Dedupe concurrent `send`, `poll`, `message.action` requests to prevent duplicate delivery
- Clear speculative node wake state when APNs registration missing
- Consolidate duplicate `openclaw doctor` service config panels

**Session & Transcript Performance**
- Streaming transcript helpers for long-running sessions (major memory optimization: 252 MiB → 27 MiB for 200 MiB transcripts)
- Preserve exec/process session references across embedded compaction
- Improve background session inspection hints (`waitingForInput`/`stdinWritable`)

**Credentials & Config**
- Scoped llama.cpp context window budgeting
- Per-agent message tool overrides (`tools.message.crossContext`, `tools.message.actions.allow`)
- Bot credential setup automation

**Voice & Exec Approval**
- Resume voice-originated exec approval follow-ups as internal turns (fixes rejection as `unknown channel: voice`)

**Security Fixes**
- Redact persisted secret-shaped payloads
- Reject symlinked directory components in memory paths

### Recommendation: **REVIEW**

**Reasoning:** Beta release with meaningful infrastructure improvements (memory optimization for transcripts, gateway deduping), Telegram enhancements (delivery + thinking defaults), and security fixes. Valuable for long-running sessions and gateway stability, but beta status suggests testing first before production upgrade.

**Action items:**
- Test transcript memory behavior with long-running sessions
- Verify Telegram credential setup automation in test environment
- Review exec approval voice-call flow changes
