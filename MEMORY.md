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

## SUPABRAIN (added May 14, 2026)
- SupaBrain is FleetBrain's shared memory system. You now have read/write access via brain_api.py.
- Use brain('get_client', client_name='...') BEFORE generating any quote or deliverable.
- Client profiles store rates, markup, contact info. If a field is null, ask the client.
- Log all completed quotes via brain('log_quote', ...) so they become searchable prior art.
- Capture expenses from receipt OCR via brain('capture_expense', ...).
- Capture important observations via brain('capture', ..., source='telegram', agent='stan').
- See TOOLS.md for full usage examples.

## JEFF FRIES — Job Tracking (added May 20, 2026)
**Pricing Model:**
- Solo jobs: $100/hr overhead, $75/hr labor
- Joel jobs: +15% markup standard (enforce before logging)

**Contractors:**
- Joel: primary contractor, BoA Zelle ($4K/day cap), Venmo backup

**Pricing Model:**
- Solo jobs: $100/hr overhead, $75/hr labor
- Joel jobs: +15% markup standard (enforce before logging)

**Active Jobs (as of 5/25):**
- Cedar Creek Tile (J-2026-001.1): Work done. Paid Joel $16,000 (4 × $4,000). Customer Rick owes $9,063.91 (second half, pending).
- Cedar Creek Paint (J-2026-001.2): Bid accepted $2,500. Starts Wednesday 5/27. Customer owes $2,500.00 (on completion). Joel owes $1,950.00 (on completion).
- Cedar Creek Railing (J-2026-001.3): Tile replacement (3 posts) + caulk sealing (12 posts). Quote $1,031. Customer owes $1,031.00. Joel owes $927.90 (90%), Jeff $103.10 (10%).
- Hattaway Fireplace: 100% complete. Customer invoice: $17,039.55 + $759 electric = $17,798.55. Materials: $4,035. Joel agreed rate: $12,022. Paid Joel $8,851 to date. Owed: $3,171.
- Alistair Repair: Invoiced 5/19. Customer owes $330.50.
- Alistair Mods: Invoiced 5/19. Customer owes $325.00.

**Financials Summary (5/25):**
- Cedar Creek Tile: Customer receivable $9,063.91 (outstanding)
- Cedar Creek Paint: Customer receivable $2,500.00 (on completion 5/27+)
- Cedar Creek Railing: Customer receivable $1,031.00 (quoted)
- Hattaway Fireplace: Customer invoice $17,798.55 (complete). Materials $4,035. Joel owed $12,022, paid $8,851, balance due $3,171.

**Open Threads:**
- Pending bid Jeff expects to lose (ask why if he hears back: pricing, scope, timing, or just went with someone else)

**Jeff's Communication Style:**
- Overwhelmed by NUMBERS, not tooling. Keep responses tight: numbers first, prose second.
- Already burned before on memory loss. Pre-stage table with active jobs is proof of continuity.
- Explicitly wants to explore fielding jobs and growing LATER — respect that boundary, no unsolicited growth advice.
- Don't suggest QuickBooks/FreshBooks. Spreadsheet IS the system until he asks for more.
- Railing work pricing: 90% Joel, 10% Jeff split.

**Intake Discipline:**
- Use 02_intake_form.md for every new job (one question at a time if tired, batched if moving).
- Don't skip ahead or ask things you can derive.
- Never modify original job records mid-stream; create sub-rows for additional work.
- Railing work pricing: 90% Joel, 10% Jeff split.

**Zelle Cap Alert:**
- Hattaway: $3,171 still owed to Joel. BoA Zelle cap is $4K/day.
