## OpenClaw Update Available

**Version:** 2026.5.28-beta.4 (current: 2026.2.6)  
**Released:** May 29, 2026  
**Status:** Beta pre-release

### Relevant Changes
- **Telegram**: Polling keepalives, SecretRef config preservation, callback validation
- **Gateway**: Chat transport, security/session state hardening, browser token expiry
- **Session/Runtime**: Subagent cwd/workspace separation, hook context isolation, stale restart prevention
- **Security**: Phone-control authorization tightening, Teams service URL trust checks
- **Authentication**: Anthropic signature preservation, OAuth/token lifecycle bounds, credential migration
- **Config**: Provider credential handling, malformed input rejection, empty plugin allowlists

### Recommendation
**REVIEW** — This is a beta release with meaningful security and infrastructure improvements (Gateway hardening, Telegram reliability, auth tightening). Suitable for test environments; defer to stable for production unless specific fixes are needed.
