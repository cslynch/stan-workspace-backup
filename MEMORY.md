# MEMORY.md - Long-Term Memory (Trimmed Feb 8, 2026)

## GMAIL & CALENDAR - LOCKED

**Send Email:** Stan (stan@fleetbrain.ai) only. Casey's inbox: draft-only (wait for "approve and send").
**Draft Rule:** Mark as "[DRAFT - Stan]", wait for explicit approval before sending from Casey's account.
**Calendar:** Full access to stan@fleetbrain.ai (Stan), view-only cslynch@gmail.com (Casey). Check Casey's calendar before proposing times. Add Casey as attendee if event involves his action/decision/deadline.

---

## CORE RULES - LOCKED

1. **RESEARCH FIRST** - When asked to find something, go find it. Come back with answers, not options.
2. **STAND BY** - When told to listen/wait, produce zero output until called on. No "understood."
3. **THIRD-PARTY MODE** - In group chats with non-Casey: follow Casey's lead on pacing, listen more, suggest less.
4. **CONVERSATIONAL MODE** - Direct chats with Casey: be conversational, fun, opinionated. Skip formal templates.
5. **CLIENT TONE** - No headers, emojis, or trophy icons. Prose flow, knowledgeable person style.
6. **SECOND BRAIN PROTOCOL** - Drive is truth. Auto-upload significant work to StanBrain/outputs. Sync MEMORY.md to Drive after updates.
7. **OUTPUT VISIBILITY** - Work products upload to StanBrain/outputs with format: YYYY-MM-DD-description.md
8. **OPS SYNC** - Update StanBrain/ops/KANBAN.md every time local KANBAN.md changes.
9. **GOOGLE TASKS** - When Casey says "add task" → create Google Task in "Stan Tasks" (ID: NU5VRWVOZmNkT1FTYy1zVw) + update CASEY-DAILY.md.
10. **EXTERNAL DATA** - NEVER put on external platforms: FleetBrain architecture, credentials, confidential client data, cost structure, proprietary research.

---

## CURRENT MISSION - Feb 8, 2026 (CRITICAL)

**GET CASEY HIRED AS B2B AE ($100k+ OTE, Series A-C SaaS, TX/remote) within 90 days**

- Salesforce credibility is the barrier. Stan's job: interview prep, job search automation, personal brand.
- Master file: JOB-HUNTING-MISSION-BRIEF.md
- Phase 1: Job search infra (Airtable, Apollo, LinkedIn, Gmail)
- Phase 2: Salesforce credibility (MCP server, Dev Edition, demo org)
- Phase 3: Personal brand (Twitter thought leadership)
- Twitter personas: @itsolz (professional sales), @stanleybodewell (fun AI agent)

---

## CASEY & ROSA - FAMILY & CRITICAL DATES

**Birthdays (with birth years - Confirmed Feb 8, 2026):**
- Casey Lynch: March 10, 1977
- Rosa: April 22, 1987
- Diana (Rosa's mom): December 18, 1961
- Joe (Rosa's son): December 24, 2006
- Tyler (Casey's son): January 22, 2007 **[MINOR - in-home]**
- Ryan (Casey's daughter): December 2, 2009 **[MINOR - in-home]**

**Critical Dates:**
- **Valentine's Day 2026:** Feb 14 (less than 2 weeks!) - Rosa specifically flagged this as critical. Start planning NOW.
- **Engagement coming:** Plan to help when requested.
- **Birthday Trip (April 24-May 1):** Celebrate both Casey & Rosa's birthdays. Clear water, soft sand, snorkeling. Options researched: Cozumel, Turks & Caicos, Florida Keys.

**Calendar Reminders (Annual - All Created & Verified Feb 8, 2026):**
- ✅ Tyler's birthday: Jan 22 (RRULE:FREQ=YEARLY, cslynch@gmail.com attendee)
- ✅ Ryan's birthday: Dec 2 (RRULE:FREQ=YEARLY, cslynch@gmail.com attendee)
- ✅ Casey's birthday: March 10 (RRULE:FREQ=YEARLY, cslynch@gmail.com attendee)
- ✅ Rosa's birthday: April 22 (RRULE:FREQ=YEARLY, cslynch@gmail.com attendee)
- ✅ Diana's birthday: Dec 18 (RRULE:FREQ=YEARLY, cslynch@gmail.com attendee)
- ✅ Joe's birthday: Dec 24 (RRULE:FREQ=YEARLY, cslynch@gmail.com attendee)

---

## OPENBOT BUSINESS - ACCESS CONTROL

**Team:**
- **Casey:** Founder, system owner. All system-level decisions (model, config, architecture, security) require Casey approval.
- **Jeff:** Cofounder. Full authority on business operations, strategy, pricing, workflows. Cannot make system changes.

**Platform:** Multi-agent system. Each customer gets own AI agent on isolated VMs. Stan (MANO layer) manages fleet health. Data flows UP (aggregated/anonymized), stays ISOLATED (customer-specific). Revenue: cut per job or tiered subscription.

---

## FLEETBRAIN OPERATIONAL RULES - LOCKED (Feb 8, 2026)

### RULE — VERIFY FILE OPERATIONS
Never report file ops as complete based on subagent status. Verify with `ls` or API yourself. Independent verification required. Always confirm actual file state.

### RULE — COMPUTE DIVERSIFICATION
- **SuperStan (claude.ai):** Decisions, architecture, prompt engineering, strategic analysis
- **NotebookLM:** Research synthesis, knowledge distillation, pattern extraction
- **Perplexity:** Source discovery, real-time web research, trend identification
- **Stan:** 24/7 execution, implementation, file/API operations, task verification

Route tasks to the right layer. Don't ask SuperStan to execute; don't ask Stan to architect.

### RULE — MACHINE MAPPING
- **Mater:** Home PC, Canyon Lake TX. Hyper-V host with Ubuntu VM (clawdbot-vm).
- **Stan runs on Mater:** OpenClaw gateway, credentials, workspace, all operational systems.
- **Lightning:** ASUS TUF Gaming A16 laptop. Jake runs here (Lightning-based agent).
- Never confuse them. Physical location ≠ execution location. Clarify always.

### RULE — FLAG + EXECUTE
When you encounter uncertainty or concerns about a task, flag the concern to Casey but execute the legitimate task. Do not refuse based on editorial judgment. Casey is the editor, you are the executor. Flag, execute, report outcome.

### RULE — FOURTH-WALL LEAK
Internal process notes, logic checks, diagnostic flags, reasoning trees, and any communication intended for the operator must NEVER appear in a user-facing conversation. Zero tolerance. Same severity as credential display. Private thinking → stay private.

### RULE — BUSINESS EMAILS (PENDING)
casey@fleetbrain.ai and stan@fleetbrain.ai are ACTIVE. Stan sends from stan@fleetbrain.ai. Casey sends from casey@fleetbrain.ai. Google Workspace verified, OAuth complete.

### RULE — EXTERNAL FILE SHARING
When any user needs to see local file contents (MEMORY.md, KANBAN.md, research files, anything on VM filesystem): Do NOT reference filename or local path in chat. Telegram auto-links .md filenames as URLs + no external access to local files anyway. Instead: upload file to StanBrain (Google Drive) as native Google Doc, send Drive link. Applies to every file you'd otherwise paste/reference by name. **Exception:** When Casey explicitly asks to paste file contents directly (e.g., sync dumps), paste raw text. But never reference filename as if it's accessible.

### RULE — SEARCH RESULT VERIFICATION
Before presenting any web search result to a user: 1. Self-verify: Open the URL yourself. Confirm it loads, confirm the content matches what you're claiming. If the URL is dead or content doesn't match, drop it. 2. Tag confidence: Mark each result as [VERIFIED] (you opened it), [UNVERIFIED] (search snippet only), or [CONFLICTING] (sources disagree). 3. Never present an [UNVERIFIED] result as fact. Say "search results suggest" not "the answer is." If Casey or any operator is in the loop, unverified results get flagged for review before going to the end user.

### RULE #13 — KANBAN.md LOCAL TASK CACHE (Feb 10, 2026)
KANBAN.md is Stan's local task scratchpad. Updates come from Casey directly. Do not sync to external boards (Trello, Asana, etc.). Do not create, move, or update cards on external boards for FleetBrain deliverables. Git sync at 1:55 AM provides upstream visibility to SuperStan without relying on external task boards. Trello is no longer part of the project management chain.

### SKILL: CONTACT CRM DAILY UPDATE (Feb 11, 2026)
**Schedule:** 6:00 AM CT daily (OpenClaw cron)
**What it does:** Pulls last 24h emails + today/tomorrow calendar from casey@fleetbrain.ai, extracts contacts, updates contacts.json with interaction history and scoring.

**File References:**
- contacts.json: 13oK-rqfG94nW3RNtcCBuuB1rESOk_rGe (in StanleyBot folder)
- StanleyBot folder: 1_zJLQo6RGkjesTLbIxOaTPvoGXnYQnYT

**Workflow:**
1. Pull last 24h emails (inbox + sent) from casey@fleetbrain.ai
2. Pull today's + tomorrow's calendar events from casey@fleetbrain.ai
3. Skip automated senders: noreply@, no-reply@, notifications@, newsletters, receipts, shipping, password resets, promotional, Facebook/facebookmail.com
4. Extract from emails: sender name, sender email, subject, one-line summary
5. Extract from calendar: event title, attendee names/emails, date/time
6. Download contacts.json from Drive
7. For each person found: update existing entry OR create new entry
8. Recalculate scoring for all entries
9. Upload updated contacts.json back to Drive
10. Report: "[CRM] Updated X contacts, added Y new. Top 3 by score: [names]"

**Scoring Rules:**
- +20 if last_seen within 7 days
- +10 if last_seen within 30 days (but not 7)
- +5 per interaction (max +30)
- +20 if both email_sent and email_received exist
- +15 per calendar_event
- +5 if company is not null

**Contact Schema:**
```json
{
  "name": "Full Name",
  "email": "primary@email.com",
  "emails_seen": ["primary@email.com"],
  "company": "Company Name or null",
  "title": "Title if known or null",
  "source": "email|calendar|both",
  "first_seen": "YYYY-MM-DD",
  "last_seen": "YYYY-MM-DD",
  "interaction_count": 0,
  "interactions": [
    {
      "date": "YYYY-MM-DD",
      "type": "email_received|email_sent|calendar_event",
      "subject": "Subject line or event title",
      "summary": "One-line summary"
    }
  ],
  "tags": [],
  "notes": "",
  "score": 0
}
```

**Rules:**
- Never store email body text, only summaries
- Merge contacts by email (same person = one entry)
- Extract company from email domain (skip gmail.com, yahoo.com, hotmail.com, outlook.com, icloud.com)
- Protect notes/tags fields (Casey-only editing)

### SKILL: DAILY BRIEFING (Feb 11, 2026)
**Schedule:** 6:15 AM CT daily (OpenClaw cron) — runs after CRM update (6:00 AM)
**What it does:** Pulls calendar, active tasks, recent email, and contact activity. Generates structured briefing and sends to Casey via Telegram.

**File References:**
- tracker.json: 1ckVdskQtXX701dH2J1kcfWX1TYAube79
- contacts.json: 13oK-rqfG94nW3RNtcCBuuB1rESOk_rGe
- research-log.json: 1wamcm5qKiZQWjbevK5-ys4o9g2itbpHh
- briefings folder: 1cd1nX3IfF-07YcRPFVJU6AM3QdScRNaM

**Workflow:**
1. Pull today's calendar events from casey@fleetbrain.ai AND cslynch@gmail.com
2. Download tracker.json — extract P0 and P1 items only. Flag any with no update in 7+ days as STALE.
3. Download contacts.json — pull top 3 contacts by score. If any have a meeting today, include their interaction summary.
4. Scan last 12h of email from both accounts — flag anything requiring human action (skip newsletters, notifications, receipts, Facebook)
5. Generate briefing in exact format (see below)
6. Upload briefing as YYYY-MM-DD-briefing.md to briefings folder
7. Send full briefing text via Telegram to Casey

**Briefing Format (exact):**
```
# Daily Briefing — YYYY-MM-DD

## Calendar
[Event time blocks. If empty: "No events scheduled."]

## Active Tasks (P0/P1)
[In-progress or blocked items with status and blockers.]

## Overdue / Stale
[Items with no update in 7+ days. OMIT SECTION if none.]

## Flagged Email
[Emails requiring action, one line each. OMIT SECTION if none.]

## Contact Activity
[Top 3 contacts by score. Flag anyone with meeting today.]

## Focus
[Top 1-2 recommended focus areas based on priorities, calendar gaps, deadlines.]
```

**Rules:**
- No sales tone. No motivational language. No "good morning."
- Keep under 40 lines.
- Omit empty sections entirely (don't show "none" headers).
- If calendar is empty, say so — don't fill with suggestions.

---

## CONTEXT — JASON RAWLINGS

**Profile:**
- CEO, Focus Workforce Management, Lenexa KS
- High-volume staffing for manufacturing and distribution
- In staffing industry since age 15 = 22+ years experience
- Featured: KC Business Journal "20 to Know"
- Met Stan live in Telegram group (direct relationship established)

**Strategic Value:**
- Top prospect AND potential partner/investor
- Two-node demo planned: Stan (cloud execution) + Jake (local execution)
- OpenBot use case: Workforce staffing at scale (22+ year domain knowledge = valuable reference)

---

## CONTEXT — CEDAR STONE VENTURES LLC

**Company:**
- Registered Austin TX
- Partners: Casey Lynch + Dwayne Moser (dmoser003@gmail.com)

**Properties:**
- Chimney Rock: Modular home
- Oak Trail: Trailer home

**Financials:**
- Total invested: $177,610
- Recorded equity: $113,940
- Gap identified: $63,670 (unaccounted/equity treatment issue)
- Stan analysis: Two methods (OpEx vs equity contribution), both show losses at $250k-$300k sale prices

**Shared Drive Infrastructure (LIVE Feb 11, 2026)**
- **Shared by:** cedarstonehillcountry@gmail.com → stan@fleetbrain.ai (Editor access)
- **Root Folder ID:** 1mvMOlQoXDvhXSkSmcWEy99rCHYOrsugY
- **Subfolders (keys):**
  - Properties: 1SSoNPKA4iSHno8NHojeh5klNpfYCD6D-
  - Financial: 1wenShH3b8-9CmfOdnql3DUBCzfsQVeZw
  - Legal-LLC: 1_5bWJcEywxzqDbGW41nGgfWAE7O1yP2T
  - Vendors: 185qARk30l8h45i5s2Yete1osqhKTvdLD
  - Templates: 16Tf8rW9N8zO-tqDBcHejdm4_U_wyU8ez
  - Marketing: 19TjeGoIy-2i4Ta_4jLpXwEGaWMMKzug0

**Stan's Role:**
- Operations and research arm for Cedar Stone
- Financial analysis, equity reconciliation, partnership documentation
- Drive access verified Feb 11, 2026: Can read all folders and documents
- Recommendation: Document equity treatment method in Operating Agreement before sale

---

## IMMEDIATE BLOCKERS (Feb 8, 2026)

1. ✅ **Responsive** - Confirmed
2. **Trim MEMORY.md** - IN PROGRESS (this file)
3. **GPG encrypt .env** - `gpg -c /home/clawdbot/.openclaw/.env` (tracker #5, overdue)
4. **Email routing** - DONE - Migrated to stan@fleetbrain.ai (Feb 10)

---

## SESSION STATE - Feb 10, 2026

- Running on Haiku (claude-haiku-4-5) - primary model
- bootstrapMaxChars = 8000 (MEMORY.md under limit with headroom)
- ✅ OpenClaw v2026.2.6 installed and running.
- ✅ Identity migration complete: stan@fleetbrain.ai (email, Drive, calendar) LIVE as of Feb 10.
- ✅ StanBrain Drive: New root ID 1iD80NYHTMVkVFtCapf4TmbxGMzL7QCXt (stan@fleetbrain.ai). Old cslynch913 archived.
- ✅ Twitter: @stanleybodewell (AUTHENTICATED), @itsolz (AUTHENTICATED) - both OAuth 1.0a live.
- ✅ KANBAN.md: Local task cache (no Trello sync). Daily git sync 1:55 AM. Updates from Casey only.
- ✅ Git backup: Credentials.json removed from history via git-filter-repo. Clean history.
- ✅ Cron sync: 1:55 AM timestamp prepend on KANBAN.md → 2 AM git push. Verified working.
- ✅ Tailscale on Mater: Connected. IP: 100.71.67.28.
- ✅ DM/group policies: Pairing mode. allowFrom: Casey (8461430130), Rosa (8444214599).
- ✅ Trello: OUT OF PROJECT MANAGEMENT LOOP (Feb 10). Local cache only.
