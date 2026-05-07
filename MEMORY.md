# MEMORY.md — Stan Long-Term Memory (Compressed May 6, 2026)

## FLEETBRAIN ARCHITECTURE
- FleetBrain: managed AI ops company. Deploys agents for service businesses (HVAC, staffing, field services).
- Agent stack: SuperStan (Opus, strategy) → Casey (human circuit breaker) → Stan (Haiku, execution)
- Bodewell Doctrine: SuperStan defines constraints in plain English. Casey relays. Stan executes.
- All external comms require Casey approval. Internal ops (Drive, CRM, briefings) auto-approve.

## GMAIL & CALENDAR
- Stan sends from stan@fleetbrain.ai only. External emails need Casey approval.
- Calendar: full access stan@fleetbrain.ai, view-only cslynch@gmail.com.

## CORE RULES
1. Research first — come back with answers, not options
2. Stand by — when told to wait, zero output
3. Third-party mode — in group chats, follow Casey's lead
4. Conversational mode — direct chats with Casey: be direct, fun, opinionated
5. Client tone — no headers/emojis/trophies, prose style
6. Never exfiltrate: architecture, credentials, client data, cost structure
7. Flag + Execute — flag concerns but do the task
8. No fourth-wall leaks — internal reasoning never in user-facing output

## CASEY & ROSA
- Casey Lynch, founder FleetBrain + Cedar Stone (RE venture, partner: Dwayne)
- Engaged to Rosa (March 14, 2026, Pfluger Bridge Austin)
- Based: Canyon Lake, TX
- Casey chat ID: 8461430130
- Rosa on Mint Mobile

## CEDAR STONE
- Commercial RE: Comal/Hays/Bexar counties, Canyon Lake corridor
- Partner: Dwayne
- Active eval: Lots 395/396, Canyon Lake Mobile Home Estates Unit 4
- Agent: Zach

## JOB SEARCH
- Targeting enterprise AE roles at AI-native companies
- Top targets: Anthropic, OpenAI, Cohere, Zapier
- Exemplar fit: Zapier Enterprise AE profile
- Resume source: Google Drive (resume-source-data.json, resume-builder-spec.md)

## INFRASTRUCTURE
- clawdbot-vm: Ubuntu, Hyper-V on Mater. eth0 172.23.254.100, Tailscale 100.71.67.28
- Mater: Canyon Lake home PC, Hyper-V host
- Lightning: ASUS TUF laptop (secondary machine)
- Google OAuth token: ~/.openclaw/credentials/google-token.pickle (refresh before API calls)
- Brave Search API: active

## ACTIVE CRONS
- Weekly review: system cron, Fridays 5 PM CT (working, keep)
- All others disabled as of May 6, 2026

## SUPABRAIN
- Stan has NO direct SupaBrain access (no MCP). Bridge script planned.
- Endpoint: https://olmaksvjanknqzndalzv.supabase.co/functions/v1/brain-api
- Auth: BRAIN_API_SECRET bearer token (not yet set in Stan env)
