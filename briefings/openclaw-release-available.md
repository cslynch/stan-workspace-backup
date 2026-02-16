## OpenClaw Update Available
Version: 2026.2.14 (current: 2026.2.6)
Released: February 15, 2026 at 03:18 UTC

Relevant changes:
- **Security Hardening:** SSRF protections against private/internal hosts and metadata endpoints; local file disclosure prevention; webhook signature verification enforcement (Telnyx, Twilio); TLS pin protection from Bonjour record overrides; base64 media input size limits before decoding
- **Gateway/Routing:** Gateway restart state cleanup (command queue, heartbeat) to prevent zombie behavior; improved guild id logging for Discord; proper handling of empty channel allowlists
- **Session Management:** Fixed session transcript path resolution for mismatched agent contexts; embedded run compaction timeouts; proper handling of reset state with queued work
- **Telegram:** Poll sending support; numeric sender ID security requirement with username auto-resolve in doctor mode; webhook secret validation (prevents unauthenticated forgery)
- **Exec Approvals:** Discord channel/DM targeting for approval prompts; safeBins allowlist bypass prevention (shell expansion hardening); PATH handling improvements
- **Config:** `dmPolicy` and `allowFrom` aliases for Slack/Discord DM access control; legacy `dm.policy`/`dm.allowFrom` migration support via `openclaw doctor --fix`

Recommendation: **UPDATE**
Critical security fixes (SSRF, webhook auth, TLS) + gateway stability improvements warrant prompt deployment.
