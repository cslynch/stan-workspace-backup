## OpenClaw Update Available

**Version:** 2026.5.16-beta.1 (current: 2026.2.6)  
**Released:** 2026-05-16  
**Status:** Prerelease (beta)

### Relevant Changes

**Telegram/Group Chat:**
- Opt-in ambient turns handling with quiet room context + visible message-tool replies
- Fixed partial-stream preview retention (prevents ellipsis-only snapshots)
- Fixed memory recall in direct messages (blocking recall now runs through provider)
- Fixed polling reconnect delivery drainage (prevents stranded replies after network recovery)
- Fixed unhealthy polling detection when DM processing wedges

**Gateway/Config:**
- Extended lifecycle hook wait budgets (5s shutdown, 10s pre-restart)
- Fixed auth profile/cron job/session store entry hydration (malformed entries now ignored)
- Plugin metadata validation during install/discovery/post-update
- Doctor improvements for fallback-enabled channel access

**Session/Delivery:**
- Fixed cron isolated-agent runs from marking successful delivery on failure-only notifications
- Fixed transcript identity rotation in session-bound scheduled runs
- Fixed optimistic image message embedding (prevents browser stack overflow)
- Improved partial-stream preview handling

**Security/Media:**
- MIME type sniffing for input files (rejects spoofed image/zip payloads)
- Malformed response rejection from Runway, BytePlus, Ollama

**Other Infrastructure:**
- Skill snapshot caching for warm gateway turns (reduces redundant rebuilds)
- Subagent model fallback forwarding for isolated scheduled runs
- Local gateway request scope for `openclaw agent --local` runs

### Recommendation

**REVIEW** — Beta release with infrastructure improvements across Telegram (ambient turns, polling recovery), gateway lifecycle, config persistence, and session handling. Includes security-hardened MIME sniffing and plugin metadata validation. Prerelease status warrants testing in non-critical environment first. Relevant for Telegram reliability, gateway stability, and configuration safety.
