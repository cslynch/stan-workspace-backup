## OpenClaw Update Available

**Version:** 2026.3.24 (current: 2026.2.6)
**Released:** March 25, 2026
**Recommendation:** UPDATE

### Relevant Changes

- **Security:** Close mediaUrl/fileUrl alias bypass so outbound tool/message actions cannot escape media-root restrictions (#54034)
- **Gateway/OpenAI compatibility:** Add `/v1/models` and `/v1/embeddings`; forward model overrides through `/v1/chat/completions` and `/v1/responses` for broader client and RAG compatibility
- **Gateway/restart sentinel:** Wake interrupted agent session via heartbeat after restart; retry outbound delivery once on transient failure; preserve thread/topic routing through wake path (#53940)
- **Gateway/channels:** Keep channel startup sequential while isolating per-channel boot failures (#54215)
- **Telegram fixes:** Forum topic recovery (#53699), native command routing, outbound error handling (preserve 403 membership/block/kick details), photo dimension preflight + fallback to document sends (#52545)

### Rationale

Security fix (#54034) + critical gateway infrastructure improvements warrant immediate update.
