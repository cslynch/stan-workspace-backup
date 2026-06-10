## OpenClaw Update Available

**Version:** 2026.6.5-beta.6 (current: 2026.2.6)  
**Released:** 2026-06-09 08:43:04Z  
**Status:** Beta

### Relevant Changes

**Telegram (QQBot):**
- QQBot now strips model reasoning/thinking scaffolding before native delivery, preventing raw `<thinking>` content from leaking into channel replies

**Anthropic:**
- Anthropic extended-thinking sessions recover after prompt-cache expiry or Gateway restart
- Improved handling of Anthropic 400s and poisoned session history

**Gateway & Security:**
- Auth profiles now live in SQLite (more durable auth state)
- Owner-only HTTP tools are gated
- MCP HTTP redirects are guarded
- Gateway/config patches preserve explicit array replacement semantics, preventing accidental merge of stale entries
- Improved macOS node mode Gateway session stability

**Session & Config:**
- Session metadata migration deferred to later release for stability
- Session env planning skips unresolved placeholders that would mask state-dir `.env` values
- Stalled MCP response bodies time out instead of tying up Gateway workers

**Credentials & Auth:**
- Official npm plugin install records keep their trusted pins
- Prerelease fallback integrity checks avoid carrying stale integrity forward
- Legacy agent registry and Codex model metadata migrate safely

**Infrastructure:**
- MCP tool results coercion prevents poisoned session history after tool returns richer MCP content
- Agent, tool, and provider loops stricter around MCP lease timestamps and prompt-cache tool names
- Inline image payload redaction catches data URLs before they leak raw image bytes into transcripts

### Recommendation

**REVIEW** — This is a beta release with substantial infrastructure and security improvements relevant to Telegram, Anthropic, Gateway, auth, and session stability. Deployment in production should await the stable 2026.6.5 release, but review the changes for your update timeline.
