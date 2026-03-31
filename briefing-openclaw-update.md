## OpenClaw Update Available

Version: 2026.3.28 (current: 2026.2.6)
Released: March 29, 2026

### Relevant Changes

**Security:**
- Extended web search key audit to recognize Gemini, Grok/xAI, Kimi, Moonshot, and OpenRouter credentials (#56540)
- Security/sandbox media dispatch: closed `mediaUrl`/`fileUrl` alias bypass preventing tool/message actions from escaping media-root restrictions (#54034)

**Telegram (Core Channel):**
- Telegram/splitting: replaced proportional text estimate with verified HTML-length search for word-boundary splits (#56595)
- Telegram/delivery: skip whitespace-only and hook-blanked text replies to prevent GrammyError 400 crashes (#56620)
- Telegram/send: validate `replyToMessageId` at all four API sinks with shared normalizer (#56587)
- Telegram/pairing: ignore self-authored DM updates and render codes as Telegram-only code blocks (#54530, #52784)
- Telegram/photos: preflight dimension/aspect-ratio rules with fallback to document sends (#52545)
- Telegram/forum topics: recover `#General` topic `1` routing when metadata omitted (#53699)
- Telegram/native commands: run slash-command execution against resolved runtime snapshot (#53179)

**Gateway & Infrastructure:**
- Gateway/OpenAI compatibility: added `/v1/models`, `/v1/embeddings`, and explicit model override forwarding (#v2026.3.28)
- Gateway/restart sentinel: wake interrupted sessions via heartbeat with proper thread/topic routing (#53940)
- Gateway/channels: keep channel startup sequential while isolating per-channel failures (#54215)
- Gateway/plugins: reuse session workspace for `/tools/invoke` tool lists (#56101)

**Config & Runtime:**
- Config/Doctor: drop automatic migrations older than two months; legacy keys now fail validation (#v2026.3.28)
- Config/web fetch: allow documented `tools.web.fetch.maxResponseBytes` setting in schema validation (#53401)
- Plugins/hooks: added async `requireApproval` to `before_tool_call` hooks for exec approval overlay, Telegram buttons, Discord interactions (#55339)

**Credentials & Session Management:**
- Agents/Anthropic: recover unhandled provider stop reasons as structured assistant errors (#56639)
- Agents/status: use provider-aware context window lookup for fresh Anthropic 4.6 model overrides (#54796)
- Embedded runs/secrets: stop unresolved `SecretRef` config from crashing embedded agent runs (#45838)

**Other Relevant Changes:**
- Slack/tool actions: added explicit `upload-file` action with file upload transport (#v2026.3.28)
- Message actions/files: unified file-first sends with `upload-file` support for Teams, Google Chat, BlueBubbles (#v2026.3.28)
- Agents/sandbox: honor `tools.sandbox.tools.alsoAllow` for explicit sandbox re-allows (#54492)

---

### Recommendation: **UPDATE**

**Rationale:** Security fixes (web search audit, media-root bypass closure), critical Telegram reliability fixes (splitting, delivery, forum routing), gateway infrastructure improvements, and session/credential handling enhancements. These are production-quality fixes with broad relevance to channel stability and security posture.
