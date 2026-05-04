# MEMORY.md - Long-Term Memory (Updated Feb 12, 2026)

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
18. **GOOGLE OAUTH REFRESH** - Before any Google API call (Drive, Calendar, Gmail): load token → check if expired → refresh + resave if needed. Never assume token is valid.

---

## CASEY & ROSA - FAMILY & CRITICAL DATES (Updated May 3, 2026)

**Birthdays (with birth years):**
- Casey Lynch: March 10, 1977
- Rosa: April 22, 1987 **[CELEBRATED - April 22, 2026]**
- Diana (Rosa's mom): December 18, 1961
- Joe (Rosa's son): December 24, 2006
- Tyler (Casey's son): January 22, 2007 **[MINOR - in-home]**
- Ryan (Casey's daughter): December 2, 2009 **[MINOR - in-home]**

**Critical Dates:**
- **Valentine's Day 2026:** ✅ DONE (Feb 13-14) — Reservation: 18 Oaks steakhouse, 7:30 PM, JW Marriott San Antonio Hill Country Resort & Spa.
- **Rosa's Birthday:** ✅ DONE (April 22, 2026)
- **Birthday Trip (April 24-May 1, 2026):** ✅ DATES PASSED — Status unknown. Awaiting feedback from Casey.
- **Engagement coming:** Plan to help when requested.

**Recent Gestures:**
- **Feb 17, 2026:** Flowers sent to Rosa's new office at AWC (pregnancy outreach volunteer group). Pastel arrangement from Oakleaf Florist (~$125). Card message: "I'm so proud of the mission you serve at AWC. 'Every child is a blessing' (Psalm 127:3)."
- **Next up:** Swarovski jewelry + plan a date

**Annual Calendar Reminders (RRULE:FREQ=YEARLY):**
- ✅ Tyler's birthday: Jan 22
- ✅ Ryan's birthday: Dec 2
- ✅ Casey's birthday: March 10
- ✅ Rosa's birthday: April 22
- ✅ Diana's birthday: Dec 18
- ✅ Joe's birthday: Dec 24

---

## SUNDAY METRICS & OPERATIONS (Updated May 3, 2026)

**Weekly Report:** KANBAN-WEEKLY-2026-05-03.md (generated Sun 5:00 PM CDT)

**Critical Alerts:**
1. **DEADLINE PASSED:** Task 35 (Zapier Enterprise AE) — deadline was 3/31/2026 (12 days ago). Verify Ashby status. OTE $240K–$300K. If closed, mark lost opportunity.
2. **DATA STALE:** Tracker.json last updated 2026-03-03 (40 days). Cannot trust status of 23+ tasks. Resume weekly sync.
3. **OAUTH BLOCKER:** Task LTN-002 (Lightning Phase 2) blocked on Google Workspace OAuth for jake@fleetbrain.ai since Feb 11. Verify if provisioned or still pending.

**Quick Wins (This Week):**
- Task 7: X Launch — blocked on mascot image. Task 5 (mascot) is "Ready". ACTION: Generate via Ideogram + apply to @stanleybodewell profile. 3–4 hours.
- Task 25: Marketplace submission — blocked on logo + description. 1 week to complete.
- Task 21: Demo artifacts — no blocker. Coordinate with Stan for 3–4 work clips. 2–3 hours.
- Task 34: Browser profile fix (attachOnly). <1 hour.

**Ownership:**
- Casey: Mascot image, Marketplace assets, browser fix
- SuperStan: Verify OAuth status, unblock Lightning chain
- Stan: Demo artifact capture

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

**Morning Pipeline (CT, daily):**
- 5:50 AM — OpenClaw Release Monitor
- 6:00 AM — Contact CRM Daily Update
- 6:15 AM — Daily Briefing
- 6:30 AM — X Content Scout
- 6:45 AM — Job Scout (NEW)
- 7:00 AM — Research Harvester (rescheduled from 6:45 AM)

---

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

### SKILL: X Content Scout
**Schedule:** 6:30 AM CT daily (OpenClaw cron) — runs AFTER Daily Briefing (6:15 AM)
**Purpose:** Identify and draft shareable content from daily operations. Zero auto-posting; all drafts require Casey approval.

**Full definition:** Read x-content-scout.md from claude-skills/ folder (ID: 12ubdosR2vN5s4vteuhU3uflnvsLi55mY) before first run.

**Workflow (short version):**
1. Read today's briefing from briefings/ folder
2. Read last 48h of research-log.json
3. Scan tracker.json for recently completed items
4. Select 0-2 items worth posting. If nothing strong, skip with "X Scout: No strong candidates today."
5. Draft posts with routing: `📋 X DRAFT — @[ACCOUNT] [CATEGORY] [280 char max text] Source: [trigger]`
6. Send drafts to Casey via Telegram
7. Wait for: APPROVE / KILL / EDIT
8. On APPROVE: post to assigned account, screenshot, confirm
9. On EDIT: use Casey's revised text, post, confirm
10. On KILL: discard

**Account Routing (mandatory):**
- **@itsolz** (Casey voice — FleetBrain practitioner): [INSIGHT] [SIGNAL] [CONTRARIAN]. Competent, direct, industry-facing.
- **@stanleybodewell** (Stan voice — character/bot): [STAN] [BUILD-LOG]. Looser, fun, opinions.
- Casey can override routing on any individual post.

**Categories:** [INSIGHT] [SIGNAL] [BUILD-LOG] [STAN] [CONTRARIAN]

**Voice Rules:**
- Competent practitioner sharing real experience. No sales pitch or hype.
- First-person plural ("we") or third-person ("Stan"). Never "I" as company.
- Allowed: dry humor, mild self-deprecation, genuine frustration with AI hype
- Forbidden: emoji spam, hashtag stuffing, engagement bait, thread openers ("1/🧵")
- Technical specificity > vague claims

**Safety (LOCKED):**
- NEVER expose: file IDs, server names, IPs, credential flows, architecture
- NEVER mention: client names, identifiable operational details, Casey's personal life/family
- Anonymize all examples
- Max 2 posts/day. 0 is fine.
- If unsure: flag and don't draft

**Approval (MANDATORY):**
Nothing goes live without explicit Casey approval. Zero auto-posting.

---

### SKILL: Job Scout
**Schedule:** 6:45 AM CT daily (OpenClaw cron) — runs AFTER X Content Scout (6:30 AM)
**Purpose:** Surface 3-5 relevant job opportunities daily. Targets enterprise AI sales, AI transformation, and solutions engineering roles.

**Workflow (short version):**
1. Read applications.json (StanleyBot root) → get already-surfaced roles (dedup), watchlist companies, active applications
2. Read contacts.json → cross-reference company names for connection matches
3. Web search across 2-3 sources (rotate daily): LinkedIn Jobs, Built In, Wellfound, company career pages, Indeed/Glassdoor
4. Search titles: AI Sales Executive, Enterprise Account Executive (AI/ML), AI Transformation Sales, Solutions Consultant/Engineer, Director of Sales AI, Strategic Account Executive, VP Sales (startups)
5. Filter: Remote/Hybrid (US/TX), Series A+, AI/ML/automation/enterprise SaaS, $150K+ OTE. Exclude: SDR/BDR, pure marketing, SMB-only, 50%+ travel.
6. Score fit: HIGH (3+ fit signals, 0 anti-signals), MEDIUM (1-2 signals or minor anti), LOW (stretch)
7. Fit signals: enterprise sales cycles, technical selling, AI agents/ops, recent funding, C-suite buyers, contact match in contacts.json
8. Select top 3-5 leads. Prioritize HIGH, include ≥1 MEDIUM if <3 HIGH.
9. Format per lead: `🎯 JOB LEAD [FIT: HIGH/MEDIUM/LOW] / Role: [Title] / Company: [Name] — [stage] / Location: [Remote/Hybrid/City] | Comp: [range or Not listed] / Link: [URL] / Fit: [1-2 sentences] / Contact: [name or None] / Flag: [anti-signals or None]`
10. Send via Telegram with pipeline summary (X active, Y awaiting response, Z interviewing)
11. Append all surfaced leads to applications.json with status "Surfaced"
12. If no leads: "Job Scout: No strong matches today. [X] results scanned, none cleared filter."

**Company Watchlist (in applications.json):** 18 companies tracked (Anthropic, OpenAI, Cohere, Mistral, Scale AI, Databricks, etc.)

**Approval Flow:**
- Casey sees leads in Telegram
- Per lead: APPLY (Stan drafts materials), TRACK (add to watchlist), SKIP
- APPLY → status "Applying", drafts cover letter/outreach
- TRACK → status "Watching"
- SKIP → status "Skipped"

**Safety:**
- Never apply on Casey's behalf. Casey applies or explicitly instructs.
- Never send outreach without approval.
- Never expose FleetBrain architecture in application materials.
- Flag if target company could be FleetBrain client (conflict of interest).

**Embedded Skill:** Application Tracker (application-tracker.md) — maintains applications.json, dedup, follow-up flagging, weekly summaries.

---

## JOB SCOUT COMPANY WATCHLIST TRACKING (Feb 25, 2026)

**Purpose:** Prevent wasted cycles re-checking watchlist companies that have no open sales roles.

**Reset Schedule:** Every Sunday (reset all "checked" dates and "nothing open" statuses to prevent permanently skipping companies).

**Tracking Format:**
```
Company Watchlist — Last Updated: 2026-02-25 (reset weekly)

Datadog          — Checked: 2026-02-25 — Status: Nothing open
Slack            — Checked: 2026-02-24 — Status: 1 Enterprise AE open
Figma            — Checked: 2026-02-23 — Status: Nothing open
Stripe           — Checked: 2026-02-22 — Status: 2 Strategic AE open
Notion           — Checked: 2026-02-21 — Status: Nothing open
Monday.com       — Checked: —          — Status: Unchecked
Atlassian        — Checked: —          — Status: Unchecked
Salesforce       — Checked: —          — Status: Unchecked
HubSpot          — Checked: —          — Status: Unchecked
ServiceNow       — Checked: —          — Status: Unchecked
Anthropic        — Checked: —          — Status: Unchecked
OpenAI           — Checked: —          — Status: Unchecked
Cohere           — Checked: —          — Status: Unchecked
Mistral          — Checked: —          — Status: Unchecked
Scale AI         — Checked: —          — Status: Unchecked
Databricks       — Checked: —          — Status: Unchecked
Snyk             — Checked: —          — Status: Unchecked
Miro             — Checked: —          — Status: Unchecked
You.com          — Checked: —          — Status: Unchecked
Retool           — Checked: —          — Status: Unchecked
HashiCorp        — Checked: —          — Status: Unchecked
Zilliz           — Checked: —          — Status: Unchecked
Wiz              — Checked: —          — Status: Unchecked
Lacework         — Checked: —          — Status: Unchecked
```

**Update Instructions:**
- Job Scout updates this list as company career pages are checked
- If "Nothing open" → note in daily report: "Checked: [company], no sales roles open"
- If roles found → they appear in applications.json as surfaced leads (don't repeat here)
- Every Sunday AM: reset all dates and "nothing open" statuses (companies add new roles mid-week)

---

### SKILL: Application Tracker
**Schedule:** Embedded in Job Scout (6:45 AM CT), no separate cron
**Purpose:** Maintain applications.json as single source of truth for Casey's job search. Track: surfaced → applied → interviewing → offer/rejected/withdrawn.

**Data File:** applications.json (D:\StanleyBot\applications.json, synced to Drive)

**Status Values:**
- Surfaced: Found, awaiting Casey decision
- Watching: Marked for later, periodic check
- Applying: Drafting materials
- Applied: Application submitted
- Response: Heard back
- Interview: Active interview process
- Offer: Offer received
- Rejected: Declined
- Withdrawn: Casey pulled out
- Skipped: Casey said no at surface

**Execution (Stan, daily):**
1. After Job Scout surfaces leads, append to applications.json with status "Surfaced"
2. Scan for follow-up triggers:
   - Applied > 7 days, no response → flag in Telegram
   - Interview within 48h → generate prep briefing
   - Watching > 14 days → re-check if role still open
3. Include pipeline summary in Telegram: `📊 Pipeline: [X] active, [Y] awaiting response, [Z] interviewing / ⚠️ Follow-up: [company — role, applied X days ago]`
4. Weekly (Sundays): append to daily briefing with summary of new leads, applications, responses, interviews, stale entries

**Rules:**
- Never modify status without Casey instruction (except Surfaced auto on scout)
- Never delete entries. Rejected/Skipped stay for history.
- Dedup by company + role title
- Prep briefings saved to materials.prep_briefing field
- Cover letters, outreach drafts require Casey approval before use

---

### SKILL: Research Harvester
**Schedule:** 7:00 AM CT daily (OpenClaw cron) — runs AFTER Job Scout (6:45 AM)
**Purpose:** Harvest Perplexity deep research output from Drive and index into research-log.json for persistent retrieval.

**Workflow (short version):**
1. Scan StanleyBot Drive folder for Google Docs with prefix: `perplexity-research-*`
2. For each doc found:
   - Read content
   - Generate slug from title (lowercase, hyphens, no special chars)
   - Write markdown to `D:\StanleyBot\research\[slug].md`
   - Append to `research-log.json` with: `original_doc_id`, `slug`, `title`, `created_at`, `content_hash`
   - Dedup check: skip if `original_doc_id` already in log
   - Trash original Google Doc (only after both markdown and log entry succeed)
3. Send Telegram summary if docs processed: `Research Harvester: X docs indexed. Slugs: [list]`
4. If no new docs found, send nothing (silent skip)

**Naming Convention (PERMANENT):**
All Perplexity deep research output saved to Drive MUST use prefix: `perplexity-research-*`
Example: `perplexity-research-ai-agent-pricing-models-2026`
Docs without this prefix are ignored.

**Safety:**
- Never delete a Doc unless BOTH markdown and log entry succeeded
- Content hash prevents re-processing same content
- research-log.json is append-only and authoritative

---

### SKILL: OpenClaw Release Monitor
**Schedule:** 5:50 AM CT daily (OpenClaw cron) — runs BEFORE Contact CRM (6:00 AM)
**Purpose:** Monitor OpenClaw releases for security/relevant updates. Feed briefing snippets to Daily Briefing at 6:15 AM.

**Full definition:** Read openclaw-release-monitor.md from claude-skills/ folder (ID: 12ubdosR2vN5s4vteuhU3uflnvsLi55mY) before first run.

**Workflow (short version):**
1. Fetch latest 5 releases from https://api.github.com/repos/openclaw/openclaw/releases?per_page=5
2. Compare latest tag against baseline version 2026.2.6
3. If newer version exists:
   - Read release body
   - Filter for relevant keywords: telegram, security, anthropic, gateway, config, routing, session, credential, exec approval, SSRF, TLS
   - Ignore: discord, slack, feishu, tlon, bluebubbles, macos, web ui, i18n, docs, ci, test
4. If relevant changes found:
   - Write briefing snippet to workspace
   - Format: `## OpenClaw Update Available / Version: [new] (current: 2026.2.6) / Released: [date] / Relevant changes: [list] / Recommendation: UPDATE|DEFER|REVIEW`
   - Daily Briefing skill picks this up at 6:15 AM
5. If no new version or no relevant changes, do nothing

**Recommendation Logic:**
- **UPDATE:** If security keyword or critical infrastructure change
- **DEFER:** If all changes match ignore list
- **REVIEW:** Otherwise

**Safety:**
- Never expose current version in public output
- Store snippet locally only
- No auto-updates; briefing is informational only

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

## 0-VAULT — ENCRYPTED CREDENTIAL STORAGE (Feb 12, 2026)

**Location:** `My Drive/0-vault/` on casey@fleetbrain.ai Google Drive

**Purpose:** Secure storage for service account keys, OAuth tokens, and sensitive credentials

**Format & Rules:**
- All secrets **GPG-encrypted** before upload (e.g., `filename.json.gpg`)
- Plaintext keys stored **locally only** (VM .env, never in git)
- **NEVER** store unencrypted credentials on Drive
- **NEVER** commit secrets to git
- Only Casey can decrypt (own GPG key)

**Current Entries:**
- `stan-chat-sa-key.json.gpg` — Google Chat service account key (stan-fleetbrain-bot@fleetbrain-stan-prod.iam.gserviceaccount.com)
  - Plaintext copy: `/home/clawdbot/.openclaw/credentials/fleetbrain-stan-prod-534550cd7a84.json` (local only)
  - Used by: chat-webhook.service via GOOGLE_CHAT_SA_CREDENTIALS env var
  - Status: ✅ Live and verified

**Workflow for New Credentials:**
1. Generate key in GCP Console
2. Encrypt locally: `gpg -c < key.json > key.json.gpg`
3. Upload encrypted file to 0-vault/
4. Store plaintext in `/home/clawdbot/.openclaw/credentials/` locally only
5. Reference in .env (never commit .env to git)

---

## GOOGLE CHAT WEBHOOK — LIVE & PRODUCTION (Feb 12, 2026)

**Pipeline:** Google Chat → Tailscale Funnel → gunicorn webhook (systemd service) → OpenClaw Gateway API (/v1/responses) → Stan's brain → Chat API reply

**Architecture:**
```
External User (Google Chat)
        ↓
HTTPS Tailscale Funnel
        ↓
https://clawdbot-vm.tail9ce6a9.ts.net/chat/webhook
        ↓ (proxies to)
127.0.0.1:8000 (gunicorn, 4 workers)
        ↓
POST /v1/responses (gateway API)
        ↓
Stan agent processes message
        ↓
POST /v1/spaces/{id}/messages (Chat API)
        ↓
Response appears in Chat space
```

**GCP Setup:**
- **Project:** fleetbrain-stan-prod (owner: casey@fleetbrain.ai)
- **Chat API:** Enabled
- **Service Account:** stan-fleetbrain-bot@fleetbrain-stan-prod.iam.gserviceaccount.com
  - Scope: `https://www.googleapis.com/auth/chat.bot`
  - Key file: `fleetbrain-stan-prod-534550cd7a84.json` (in 0-vault + local)

**Server Deployment:**
- **Service:** `chat-webhook.service` (systemd, enabled on boot)
- **Server:** gunicorn (4 worker processes)
- **Port:** 8000 (localhost, proxied via Tailscale Funnel)
- **Code:** `/home/clawdbot/.openclaw/workspace/chat_webhook.py`
- **Config:** `/home/clawdbot/.openclaw/.env`
- **Startup script:** `/home/clawdbot/.openclaw/chat-webhook-gunicorn.sh`
- **Logs:** `journalctl -u chat-webhook` or `/var/log/chat-webhook-*.log`

**Gateway Integration:**
- **Endpoint:** `POST http://127.0.0.1:18789/v1/responses` (OpenResponses API)
- **Auth:** Bearer token from `openclaw.json` gateway.auth.token
- **Agent routing:** Header `x-openclaw-agent-id: main`
- **Status:** ✅ Endpoint enabled in openclaw.json, tested and working

**Tailscale Funnel:**
- **Public URL:** https://clawdbot-vm.tail9ce6a9.ts.net/
- **Webhook endpoint:** https://clawdbot-vm.tail9ce6a9.ts.net/chat/webhook
- **Status:** ✅ Persistent, verified working

**Status:** ✅ LIVE - Round-trip tested, agent integration confirmed, systemd auto-start enabled

**Recent Changes (Feb 12, 2026):**
- ✅ Enabled /v1/responses endpoint in openclaw.json
- ✅ Fixed webhook agent integration (now uses gateway HTTP API instead of CLI)
- ✅ Converted to production server (gunicorn + systemd)
- ✅ End-to-end test passed: message → agent processing → reply in Chat

---

## SESSION STATE - Feb 12, 2026

- Running on Haiku (claude-haiku-4-5)
- ✅ OpenClaw v2026.2.9 running (gateway /v1/responses endpoint enabled)
- ✅ Identity: stan@fleetbrain.ai (email, Drive, Calendar) LIVE
- ✅ StanleyBot shared folder: All 7 file IDs test-verified Feb 11
- ✅ Cedar Stone shared folder: Editor access verified Feb 11
- ✅ Contact CRM skill: Ready to deploy (6:00 AM CT)
- ✅ Daily Briefing skill: Ready to deploy (6:15 AM CT)
- ✅ Research Log schema: Documented and ready to use
- ✅ KANBAN.md: Local cache synced to git daily (1:55 AM/2:00 AM)
- ✅ **Google Chat Webhook: PRODUCTION LIVE** — systemd service, gunicorn, agent integration confirmed
- ✅ **GCP Project: fleetbrain-stan-prod** — Chat API enabled, service account deployed
- ✅ **0-Vault: Encrypted credential storage** — GPG-encrypted keys on Drive, plaintext local only
- ✅ **Tailscale Funnel: Persistent public URL** — https://clawdbot-vm.tail9ce6a9.ts.net/

## OAUTH TOKEN LOADING BUG - FIXED Feb 13, 2026

**Issue:** `/v1/responses` gateway endpoint creates fresh sessions without Google Workspace OAuth tokens (works in Telegram because those sessions have context). 

**Root Cause:** OAuth tokens exist at ~/.openclaw/credentials/google-token.pickle but weren't being loaded by plugin initialization in fresh gateway sessions.

**Fix Applied (Feb 13, 2026 - 03:45 CT):**
1. ✅ Located token files: 
   - `/home/clawdbot/.openclaw/credentials/google-token.pickle` (valid, working)
   - `/home/clawdbot/.openclaw/credentials/google-credentials.json`
   - Verified tokens load and authenticate correctly
2. ✅ Added environment variables to openclaw.json:
   - `GOOGLE_TOKEN_PATH`: `/home/clawdbot/.openclaw/credentials/google-token.pickle`
   - `GOOGLE_CREDENTIALS_PATH`: `/home/clawdbot/.openclaw/credentials/google-credentials.json`
3. ✅ Enabled googlechat plugin in plugins.entries
4. ✅ Restarted gateway with new config

**Status:** RESOLVED. Google Chat now has full Google Workspace OAuth access.

---

## SUNDAY METRICS CHECKPOINT - March 29, 2026

**Status:** 3-week data gap. Tracker snapshot (Mar 3) is 26 days old. Minimal daily logs since Feb 25.

**Critical Decision Gates (All Due This Week):**
1. **🚨 Zapier Application** (Task #35) — Deadline **3/31/2026 (2 DAYS!)** — OTE $240K–$300K — Status unknown, needs immediate clarity
2. **Lightning Phase 1** (Task #1036) — Target end-of-March — Status "Not Started" (needs clarification if setup began)
3. **Jake OAuth** (Task #1037) — Blocked on Google Workspace OAuth setup — Timeline needed
4. **Marketplace Submission** (Task #25) — Priority Q1 vs Q2? Blocks Spaces automation

**Blockers:** 
- LTN-003 specification (SuperStan) — blocks Lightning Phase 3
- Jake OAuth setup — blocks secondary agent deployment

**Recommendations:**
- Fresh tracker.json snapshot needed from SuperStan
- Casey status update on Zapier, Lightning Phase 1, OAuth, Marketplace priority
- 3-week velocity assessment pending data refresh

**Reports Generated:**
- `/home/clawdbot/.openclaw/workspace/metrics/2026-03-29-sunday-metrics.md`
- `/home/clawdbot/.openclaw/workspace/metrics/2026-03-29-decision-gates-summary.md`

---

## SUNDAY METRICS CHECKPOINT - March 8, 2026

**Weekly Review Completed:** 2026-03-08 17:00 CST

**Project State (as of tracker.json Mar 3):**
- Total tasks: 40
- Done: 17 (42.5% complete)
- In Progress: 7 (no stalling)
- Blocked: 2 (Jake OAuth, LTN-003)
- Parked: 7 (demand-triggered, healthy)
- Not Started: 7 (P1 items need prioritization)

**P0 Status:** 9/10 complete. Job search Week 1 live (applied: Hebbia, Forethought, Deepgram).

**Key Decision Gates (Casey Input Required This Week):**
1. **Zapier AE Application** (Task #35) — Deadline 3/31. OTE $240K–$300K. Time commitment: 3+ weeks. Decision: Go or defer?
2. **Marketplace Submission** (Task #25) — P1 lynchpin for Spaces automation (Task #26). Decision: Q1 or Q2?
3. **Jake OAuth Activation** (Task #1037) — Unblock Lightning Phase 2. Action: Activate this week.
4. **Lightning Phase 1 Intent** (Task #1036) — Marked "Not Started." Clarify: started or queued?

**Blockers Requiring SuperStan:**
- LTN-003 specification (blocks Agent Teams protocol design)

**Stale P1 Items (Awaiting Prioritization):**
- Capability demo videos (Task #21)
- Stan browser profile fix (Task #34)
- Webhook hardening (Task #27)
- Contact research (Apollo + LinkedIn) (Task #1)
- Service account key vault (Task #28)

**Reports Generated:**
- `metrics/2026-03-08-sunday-metrics.md` (40-item full analysis)
- `briefings/2026-03-08-sunday-metrics-summary.md` (executive summary for Casey)
- Updated KANBAN.md with blockers and decision gates

---

## GOOGLE CHAT WEBHOOK - IMAGE ATTACHMENT FEATURE (P1, Needed Before Demos)

**Problem:** Webhook only passes `text` field to gateway. When users send images/attachments, the webhook payload includes attachment objects at `payload["chat"]["messagePayload"]["message"]["attachment"]` but images are never downloaded or forwarded to Stan.

**Solution:** Enhance webhook handler (in `/home/clawdbot/.openclaw/workspace` or on clawdbot-vm) to:

1. **Detect attachments** in incoming payload:
   - Check `payload["chat"]["messagePayload"]["message"]["attachment"]` (may be array or single object)
   - Extract `resourceName` and `contentType` from each attachment

2. **Download via Chat API:**
   - Use service account auth (already configured on clawdbot-vm)
   - `GET https://www.googleapis.com/chat/v1/{resourceName}` with `alt=media` parameter
   - Set `Authorization: Bearer {service_account_token}`

3. **Include in /v1/responses call:**
   - Option A: Base64 encode image → include as `base64://` data URL in message text or separate field
   - Option B: Upload to temp storage → pass URL to gateway
   - Decide based on gateway input format (check `/v1/responses` schema)

4. **Preserve metadata:**
   - Filename from attachment name
   - Content type (image/png, image/jpeg, etc.)
   - Original sender + timestamp (from message context)

**Implementation Notes:**
- Service account credentials available in standard location
- May need to refresh OAuth token before each download (follow OAUTH token refresh rule)
- Error handling: if download fails, return fallback text message noting attachment couldn't be processed
- Test with screenshots (PNG/JPG), documents (PDF), and mixed message+image inputs before demo
