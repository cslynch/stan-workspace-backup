## OpenClaw Update Available
Version: 2026.2.26 (current: 2026.2.6)
Released: Feb 27, 2026

Relevant changes:
- **SECURITY (11 fixes):** Node exec approval bypass prevention (frozen plan validation, symlink cwd rejection), SSRF guards for Teams/web tools, config include hardening, workspace boundary escape prevention via symlink validation, pairing metadata spoofing prevention, plugin channel HTTP auth normalization, voice call Twilio webhook replay hardening
- **TELEGRAM:** Webhook startup fix, sendChatAction 401 backoff to prevent bot deletion, inline button authorization in groups, streaming preview finalization, markdown spoiler delimiter handling
- **GATEWAY:** Node pairing device-metadata pinning, non-loopback bind warning, TLS probe support for `gateway.bind=lan`, shared auth scope preservation, plugin channel auth path canonicalization
- **CONFIG:** Hardened `$include` file loading with symlink rejection, auth profile alias normalization (`mode→type`, `apiKey→key`), models profile suffix parsing for edge cases like `openai/@cf/...`
- **ROUTING:** New `openclaw agents bindings|bind|unbind` CLI for account-scoped route management, multi-account delivery resolution with explicit `delivery.accountId` support
- **SESSION:** Subagent announce dispatch hardening, session cleanup doctor tool (`openclaw sessions cleanup --fix-missing`), transcript tracking improvements
- **CREDENTIAL:** Auth profile field normalization preventing silent drops, MiniMax auth header defaults fixing 401 errors
- **EXEC APPROVAL:** Immutable plan freezing (`argv`/`cwd`/`agentId`/`sessionKey`), canonical value enforcement during forwarding/execution, symlink rebind bypass prevention

Recommendation: **UPDATE** — Security-critical release addressing exec approval bypasses, SSRF leaks, config include attacks, and infrastructure hardening.
