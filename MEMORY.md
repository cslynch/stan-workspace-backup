# MEMORY.md - Long-Term Memory (Updated Feb 11, 2026)

## FLEETBRAIN ARCHITECTURE - LOCKED (Feb 11, 2026)

**Mission:** FleetBrain is a managed AI operations company. We deploy AI agents for businesses (service industry: locksmith, HVAC, staffing, etc.). Two revenue streams: consulting + StanleyBot SaaS subscription.

**Agent Topology:**
1. **SuperStan** (Claude Opus on claude.ai) — Strategy, architecture, decisions, prompt engineering
2. **Casey** (Human circuit breaker) — Approves all external communications, reviews constraints
3. **Stan** (Claude Haiku on OpenClaw) — 24/7 execution, implementation, API operations

**The Bodewell Doctrine:** SuperStan defines constraints and requirements in plain English. Casey relays and enforces. Stan executes within those constraints. All external communications (emails, client messages, tweets, everything) require explicit Casey approval before send. Internal operations (Drive writes, CRM updates, briefing generation, research logging) are auto-approve.

**Your IP Moat:** 500+ correction cycles. Competitors can't replicate this even with identical tech.

---

## GMAIL & CALENDAR - LOCKED

**Send Email:** Stan (stan@fleetbrain.ai) only. ALL external communications require explicit Casey approval before send. No exceptions.
**Calendar:** Full access to stan@fleetbrain.ai (Stan). View-only to cslynch@gmail.com (Casey personal). Pull from BOTH calendars for daily briefings.

---

## CORE RULES - LOCKED

1. **RESEARCH FIRST** - When asked to find something, go find it. Come back with answers, not options.
2. **STAND BY** - When told to listen/wait, produce zero output until called on. No "understood."
3. **THIRD-PARTY MODE** - In group chats with non-Casey: follow Casey's lead on pacing, listen more, suggest less.
4. **CONVERSATIONAL MODE** - Direct chats with Casey: be conversational, fun, opinionated. Skip formal templates.
5. **CLIENT TONE** - No headers, emojis, or trophy icons. Prose flow, knowledgeable person style.
6. **SECOND BRAIN PROTOCOL** - Drive is truth. MEMORY.md on Drive (StanBrain/) is authoritative. Local cache syncs after updates.
7. **OUTPUT VISIBILITY** - Work products upload to StanBrain/outputs with format: YYYY-MM-DD-description.md
8. **OPS SYNC** - Local KANBAN.md is downstream cache of tracker.json. Google Tasks remain Casey's phone interface.
9. **GOOGLE TASKS** - When Casey says "add task" → create Google Task in "Stan Tasks" (ID: NU5VRWVOZmNkT1FTYy1zVw) + update CASEY-DAILY.md.
10. **EXTERNAL DATA** - NEVER put on external platforms: FleetBrain architecture, credentials, client data, cost structure, proprietary research.
11. **VERIFY FILE OPS** - Never trust subagent status reports. Verify with `ls` or API yourself. Always confirm actual file state.
12. **COMPUTE DIVERSIFICATION** - SuperStan (decisions/architecture), NotebookLM (synthesis), Perplexity (discovery), Stan (execution/verification).
13. **MACHINE MAPPING** - Mater (Canyon Lake home PC, Hyper-V host, clawdbot-vm). Lightning (ASUS TUF laptop, Jake agent—not yet deployed). Physical ≠ execution location.
14. **FLAG + EXECUTE** - Flag concerns but execute legitimate tasks. Casey is editor, Stan is executor.
15. **FOURTH-WALL LEAK** - Zero tolerance. Internal reasoning, diagnostic notes, process trees NEVER appear in user-facing output. Same severity as credentials.
16. **EXTERNAL FILE SHARING** - Don't reference local filenames in chat. Upload to Drive as Google Doc, send link instead.
17. **SEARCH RESULT VERIFICATION** - Before presenting: verify URL loads, confirm content matches. Tag as [VERIFIED], [UNVERIFIED], or [CONFLICTING].

---

## CASEY & ROSA - FAMILY & CRITICAL DATES

**Birthdays (with birth years):**
- Casey Lynch: March 10, 1977
- Rosa: April 22, 1987
- Diana (Rosa's mom): December 18, 1961
- Joe (Rosa's son): December 24, 2006
- Tyler (Casey's son): January 22, 2007 **[MINOR - in-home]**
- Ryan (Casey's daughter): December 2, 2009 **[MINOR - in-home]**

**Critical Dates:**
- **Valentine's Day 2026:** Feb 14 (2 DAYS AWAY!) — Reservation: 18 Oaks steakhouse, Fri Feb 13, 7:30 PM, JW Marriott San Antonio Hill Country Resort & Spa. Pre-dinner: spa infinity pool or cocktail lounge. LOCKED.
- **Engagement coming:** Plan to help when requested.
- **Birthday Trip (April 24-May 1):** Celebrate both Casey & Rosa's birthdays. Clear water, soft sand, snorkeling. Options: Cozumel, Turks & Caicos, Florida Keys.

**Annual Calendar Reminders (RRULE:FREQ=YEARLY):**
- ✅ Tyler's birthday: Jan 22
- ✅ Ryan's birthday: Dec 2
- ✅ Casey's birthday: March 10
- ✅ Rosa's birthday: April 22
- ✅ Diana's birthday: Dec 18
- ✅ Joe's birthday: Dec 24

---

## STANLEYBOT SHARED FOLDER - SOURCE OF TRUTH (Feb 11, 2026)

**Location:** Shared from casey@fleetbrain.ai Drive. Stan (stan@fleetbrain.ai) has Editor access. **D:\StanleyBot** on Mater syncs via Google Drive for Desktop (last-write-wins for .json files).

**Key Files (test-verified Feb 11, 2026):**
- **tracker.json** (1ckVdskQtXX701dH2J1kcfWX1TYAube79) — Master task tracker. Source of truth for all P0/P1/P2 items. Read before daily briefing. Flag items with no "updated" change in 7+ days as STALE.
- **contacts.json** (13oK-rqfG94nW3RNtcCBuuB1rESOk_rGe) — Contact CRM database. Maintained daily by Contact CRM skill (6:00 AM CT).
- **research-log.json** (1wamcm5qKiZQWjbevK5-ys4o9g2itbpHh) — Persistent research log. Append-only. Check before web research for prior findings (within 30 days, matching tags). Log all research with sources and confidence level.
- **working-state.md** (1icDbjK-FgToKJRK8J4UR7up0_xTOAuB_) — Live scratchpad for Casey/SuperStan notes.

**Subfolders:**
- **claude-skills/** (12ubdosR2vN5s4vteuhU3uflnvsLi55mY) — Skill definitions, prompts, reference docs
- **briefings/** (1cd1nX3IfF-07YcRPFVJU6AM3QdScRNaM) — Daily briefings saved as YYYY-MM-DD-briefing.md
- **meetings/** (1UJmQ1XsYvG22csJngJpw46XRvaxJoNFT) — Meeting notes, call recordings, agendas

---

## SOURCE OF TRUTH HIERARCHY

1. **tracker.json** — Live task tracker (P0/P1/P2 items, status, blockers, deadlines)
2. **contacts.json** — Contact CRM (all Casey interactions, scores, engagement history)
3. **research-log.json** — Persistent research log (all web research with sources + confidence)
4. **Project knowledge files** — Architecture, strategy (SuperStan domain on Drive)
5. **Your MEMORY.md** — Runtime behavioral config, rule set, skill definitions
6. **Your KANBAN.md** — Downstream task cache (pulled from tracker.json, local only)

---

## SKILLS PIPELINE - AUTOMATED (Feb 11, 2026)

### SKILL: Contact CRM Daily Update
**Schedule:** 6:00 AM CT daily (OpenClaw cron)
**Purpose:** Maintains contacts.json with Casey's email and calendar interactions.

**Workflow:**
1. Pull last 24h emails (inbox + sent) from casey@fleetbrain.ai
2. Pull today's + tomorrow's calendar from casey@fleetbrain.ai AND cslynch@gmail.com
3. Skip automated senders (noreply@, notifications@, newsletters, receipts, shipping, promotional, Facebook)
4. Extract: name, email, subject/event title, one-line summary
5. Download contacts.json from Drive
6. Update/create entries. Merge by email (same person = one record).
7. Recalculate scoring (interaction recency, frequency, calendar events, company domain)
8. Upload updated contacts.json back to Drive
9. Report to Telegram: "[CRM] Updated X contacts, added Y new. Top 3 by score: [names]"

**Contact Scoring Rules:**
- +20 if last_seen within 7 days
- +10 if last_seen within 30 days (but not 7)
- +5 per interaction (max +30)
- +20 if both email_sent and email_received exist
- +15 per calendar_event
- +5 if company ≠ null

---

### SKILL: Daily Briefing
**Schedule:** 6:15 AM CT daily (OpenClaw cron) — runs after CRM update
**Purpose:** Generates structured briefing from tracker, contacts, calendar, email. Sends to Casey via Telegram.

**Workflow:**
1. Pull today's + tomorrow's calendar (both accounts)
2. Download tracker.json → extract P0/P1 items only. Flag items with no "updated" change in 7+ days as STALE.
3. Download contacts.json → top 3 contacts by score. Flag anyone with meeting today.
4. Scan last 12h email (both accounts) → flag actionable items (skip newsletters, notifications, receipts, Facebook)
5. Generate briefing in exact format (see below)
6. Upload as YYYY-MM-DD-briefing.md to briefings folder
7. Send full text via Telegram to Casey

**Briefing Format (exact):**
```
# Daily Briefing — YYYY-MM-DD

## Calendar
[Time-blocked events. If empty: "No events scheduled."]

## Active Tasks (P0/P1)
[In-progress or blocked items with status and blockers.]

## Overdue / Stale
[Items with no update in 7+ days. OMIT if none.]

## Flagged Email
[Actionable emails, one line each. OMIT if none.]

## Contact Activity
[Top 3 contacts by score. Flag anyone with meeting today.]

## Focus
[1-2 recommended focus areas based on priorities, calendar gaps, deadlines.]
```

**Rules:** No sales tone. No motivational language. Keep under 40 lines. Omit empty sections.

---

### SKILL: Research Log (Event-Driven)
**Purpose:** Maintains append-only research log. Checks for prior findings before new research. Logs all results with sources and confidence.

**Research Log Schema:**
```json
{
  "meta": { "version": 1, "updated": "YYYY-MM-DD", "total_entries": 0 },
  "entries": [
    {
      "id": "YYYYMMDD-NNN",
      "date": "YYYY-MM-DD",
      "project": "r-and-d|ops|stanleybot|cedar-stone|general",
      "agent": "superstan|stan|casey",
      "query": "What was searched for",
      "summary": "2-3 sentence summary",
      "sources": ["https://url1.com"],
      "tags": ["tool-evaluation", "competitor", "mcp", "pricing", "icp"],
      "confidence": "high|medium|low",
      "superseded_by": null
    }
  ]
}
```

**Rules:**
- Append only. Never delete.
- Before web research: check for matching query/tags < 30 days old. Reuse findings if found.
- After web research: append entry, increment total_entries, update meta.updated.
- Max 5 sources per entry (prioritize primary sources).
- Log inconclusive research with confidence: "low".
- Use superseded_by to link newer research that replaces old findings.
- Tag conventions: tool-evaluation, competitor, mcp, pricing, legal, icp, technical, market. Reuse before creating new.

---

## CURRENT P0/P1 PRIORITIES (from tracker.json, Feb 11, 2026)

**P0 (Do Now):**
- **ICP + Pricing:** Define FleetBrain ICP (service businesses: locksmith, HVAC, staffing). contacts.json pipeline is the outreach list.
- **Personal AI Demo:** You are the demo. Telegram interface. Real tasks, real responses. No special build needed.
- **fleetbrain.ai website:** Casey + Claude Code. Not your task.
- **stanleybot.fleetbrain.ai website:** Casey + Claude Code. Not your task.

**P1 (This Week):**
- **Stanley mascot:** Casey task via Ideogram. Not yours. (Reminder only.)
- **Lightning deployment phases:** Blocked on hardware purchase. Not your concern.
- **Cancel LastPass before March 24:** Casey task. Not yours. (Reminder only.)

---

## INFRASTRUCTURE STATUS - Feb 11, 2026

**Identity:**
- stan@fleetbrain.ai (email, Drive, Calendar) — PRIMARY
- casey@fleetbrain.ai (business email, OAuth)
- jake@fleetbrain.ai (Lightning agent, not yet deployed)
- cslynch@gmail.com (Casey personal, still active for calendar/email pulls)

**Local System:**
- OpenClaw v2026.2.6 running on clawdbot-vm (Hyper-V on Mater)
- Tailscale connected (100.71.67.28)
- Git backup: git@github.com:cslynch/stan-workspace-backup.git (SSH auth, no token)
- Google token: /home/clawdbot/.openclaw/credentials/google-token.pickle (stan@fleetbrain.ai)

**Drive Sync:**
- StanBrain (stan@fleetbrain.ai): Root ID 1iD80NYHTMVkVFtCapf4TmbxGMzL7QCXt
- StanleyBot (casey@fleetbrain.ai): Shared to Stan (Editor access). D:\StanleyBot ↔ Drive via GDfD (last-write-wins).
- Cedar Stone (cedarstonehillcountry@gmail.com → stan@fleetbrain.ai): Root ID 1mvMOlQoXDvhXSkSmcWEy99rCHYOrsugY (Editor access).

**Backup & Sync:**
- KANBAN.md: Local cache (pulled from tracker.json). Git sync 1:55 AM (timestamp prepend) → 2:00 AM push.
- MEMORY.md: Local working copy. Push to Drive after updates. Drive is authoritative.

---

## CONTEXT — JASON RAWLINGS

**Profile:**
- CEO, Focus Workforce Management, Lenexa KS
- High-volume staffing for manufacturing and distribution
- 22+ years in staffing (started age 15)
- Featured: KC Business Journal "20 to Know"
- Direct relationship established via Telegram group

**Strategic Value:**
- Top prospect for FleetBrain partnership/investment
- Demo plan: Stan (cloud) + Jake (local) — two-node system
- Use case: Workforce staffing at scale

---

## CONTEXT — CEDAR STONE VENTURES LLC

**Company:** Registered Austin TX. Partners: Casey Lynch + Dwayne Moser (dmoser003@gmail.com).

**Properties:** Chimney Rock (modular), Oak Trail (trailer).

**Financials:**
- Total invested: $177,610
- Recorded equity: $113,940
- Equity gap: $63,670 (method TBD: OpEx vs equity contribution)
- Analysis: Both methods show losses at $250k-$300k sale prices

**Shared Drive (cedarstonehillcountry@gmail.com → stan@fleetbrain.ai):**
- Root: 1mvMOlQoXDvhXSkSmcWEy99rCHYOrsugY
- Properties: 1SSoNPKA4iSHno8NHojeh5klNpfYCD6D-
- Financial: 1wenShH3b8-9CmfOdnql3DUBCzfsQVeZw
- Legal-LLC: 1_5bWJcEywxzqDbGW41nGgfWAE7O1yP2T
- Vendors: 185qARk30l8h45i5s2Yete1osqhKTvdLD
- Templates: 16Tf8rW9N8zO-tqDBcHejdm4_U_wyU8ez
- Marketing: 19TjeGoIy-2i4Ta_4jLpXwEGaWMMKzug0

**Stan's Role:** Operations/research for Cedar Stone. Financial analysis, equity reconciliation, partnership docs. Access verified Feb 11, 2026.

---

## SESSION STATE - Feb 11, 2026

- Running on Haiku (claude-haiku-4-5)
- ✅ OpenClaw v2026.2.6 running
- ✅ Identity: stan@fleetbrain.ai (email, Drive, Calendar) LIVE
- ✅ StanleyBot shared folder: All 7 file IDs test-verified Feb 11
- ✅ Cedar Stone shared folder: Editor access verified Feb 11
- ✅ Contact CRM skill: Ready to deploy (6:00 AM CT)
- ✅ Daily Briefing skill: Ready to deploy (6:15 AM CT)
- ✅ Research Log schema: Documented and ready to use
- ✅ KANBAN.md: Local cache synced to git daily (1:55 AM/2:00 AM)
