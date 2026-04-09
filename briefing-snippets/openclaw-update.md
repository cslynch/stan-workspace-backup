## OpenClaw Update Available
Version: 2026.4.8 (current: 2026.2.6)
Released: April 8, 2026 @ 5:59 AM UTC

Relevant changes:
- Telegram/setup: gateway sidecar loading fix for secret contracts during startup
- Bundled channels: shared secret contract loading across packaged top-level sidecars
- Network/fetch guard: DNS pinning and env-proxy mode handling for SSRF-guarded fetches
- Slack: HTTP(S) proxy settings honored for Socket Mode WebSocket connections (#62878)
- Slack: SecretRef-backed bot token resolution for action reads (#62097)
- Gateway/config: exec approval paths (safeBins, strictInlineEval) blocked from model-facing config writes (#62001)
- Host exec/env sanitization: dangerous credential/config/repo env overrides blocked (#59119, #62002, #62291)
- Browser/SSRF: private-network blocking for main-frame document redirect hops (#62355)
- Gateway/auth: shared-token and password WebSocket sessions invalidated on secret rotation (#62350)
- Media/base64: byte limits enforced before decoding for Teams, Signal, QQ Bot payloads (#62007)

Recommendation: UPDATE
