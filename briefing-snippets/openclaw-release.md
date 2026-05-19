## OpenClaw Update Available
Version: 2026.5.16-beta.7 (current: 2026.2.6)
Released: 2026-05-18T08:47:11Z

Relevant changes:
- **Telegram routing fixes**: Forum-topic origin preservation, HTTP 421 misdirected request retry, improved topic closure handling
- **Gateway infrastructure**: Startup probe/config attribution, plugin-service parallelization for faster restarts, session visibility improvements
- **Security & credentials**: Exec approval credential forwarding fix (enables async command completion), OAuth profile migration support
- **Config management**: Subagent model config cleanup, broken plugin discovery hardening
- **TLS proxy support**: HTTPS managed forward-proxy endpoints with scoped CA trust configuration

Recommendation: UPDATE
- Contains security fixes for credential handling and TLS infrastructure
- Addresses Telegram routing reliability issues
- Gateway performance and stability improvements
