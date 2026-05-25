## OpenClaw Update Available
**Version:** 2026.5.22 (current: 2026.2.6)
**Released:** 2026-05-24 01:12:56 UTC
**Status:** REVIEW

### Relevant Changes
- **Gateway/perf:** Process-stable channel catalog reuse, plugin metadata snapshot caching, lazy-load startup handlers, plugin alias map caching — performance optimizations that improve startup time and reduce CPU overhead
- **Telegram:** Wildcard topic defaults added to config support
- **Config:** Signal configPath, Termux home fallback, include-path validation added to documentation

### Summary
Release 2026.5.22 is primarily performance-focused (gateway caching/lazy-loading) and documentation updates. No security keywords detected. Gateway changes are infrastructure optimizations, not critical rewrites. Telegram support expanded with config options.

### Recommendation
**REVIEW** — Gateway performance improvements and Telegram config enhancements merit evaluation, but no security issues or critical breaking changes. Consider updating if performance matters for your deployment; otherwise deferrable to next release cycle.
