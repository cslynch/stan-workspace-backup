# Skill: Job Scout

## Purpose
Surface 3-5 relevant job opportunities daily from web research.
Targets enterprise AI sales, AI transformation, and solutions engineering roles.
Delivers curated leads to Casey via Telegram every morning.
Casey decides which to pursue — Stan tracks applications on approval.

## Inputs
- Target role criteria (defined below)
- Web search results (Stan's browser + web research skills)
- applications.json (Drive file — tracks what's already been surfaced/applied to, prevents duplicates)
- contacts.json (Drive file — cross-reference if Casey knows anyone at the company)

## Output
- 3-5 job leads delivered via Telegram daily
- Each lead includes: role, company, location, comp (if listed), link, and a 1-2 sentence fit assessment
- Duplicate suppression against applications.json

## Target Role Criteria

### Primary Titles (search for these)
- Enterprise Account Executive (any industry, B2B SaaS focus)
- Strategic Account Executive
- Account Executive (enterprise/mid-market)
- Sales Director / VP Sales (enterprise-focused, B2B SaaS)
- Regional Sales Director (B2B SaaS)

### Secondary Titles (surface if strong fit, rare)
- Sales Manager / Senior Account Manager (at B2B SaaS scale-up)

### DO NOT SURFACE (explicit exclusion)
- Solutions Architect / Solutions Engineer / Sales Engineer (any flavor)
- Account Manager (SMB-focused, non-enterprise)
- Business Development / BD Manager
- Inside Sales / SDR / BDR
- Sales Development Rep / Account Coordinator
- Product Manager / Marketing / Engineering roles
- Consulting (unless explicitly enterprise sales management)

### Filters
- **Geography:** Texas (Austin, Dallas, Houston, San Antonio) OR Remote (US-based)
- **Company stage:** Series B through public. Open to late-stage Series A if comp is strong.
- **Industry:** B2B SaaS (any vertical), AI/automation/infrastructure platforms selling to enterprises, DevOps/cloud platforms, security/compliance, data platforms. Companies selling to enterprise buyers (not SMB/self-serve).
- **Comp:** $150K+ OTE minimum. Flag $120K-$150K as "tight" but not auto-exclude.
- **Exclude:** Pure SDR/BDR. Pure marketing. Non-enterprise (SMB-only sales). Roles requiring 50%+ travel.

### Posting Date Validation (REQUIRED — prevents stale listings)
**When scraping career pages, check for:**
- **"Deadline to Apply"** field (Ashby career sites show this explicitly)
- **"Posted on"** dates older than 60 days (treat as stale unless company explicitly re-posted)
- **"Closed"** or **"Expired"** indicators on the job card
- **LinkedIn "Posted X days ago"** — if > 90 days, verify it's still actively hiring

**Action when stale posting detected:**
- Mark as **STALE** in output (do not include in US-RELEVANT count)
- Flag separately in daily report with expiration date so Casey can see it but knows not to apply
- Remove from consideration for application recommendations
- Log in tracking file so we don't surface the same expired role twice

**Example stale scenario:** Synthflow Sr AE listing (Dec 20 2024 deadline) appeared open on Ashby but was already expired by Feb 26. This filter catches it and prevents wasted application effort.

### Fit Signals (boost ranking)
- Job description mentions: enterprise sales cycles, consultative selling, technical sales, solution architecture, regulated industries, AI agents, AI ops
- Company has raised recent funding or is scaling sales team
- Role involves selling to C-suite or VP-level buyers
- Company's product involves AI agents, AI automation, or AI infrastructure
- Casey has a contact at the company (cross-reference contacts.json)

### Anti-Signals (flag but still surface)
- "Must have 5+ years selling AI specifically" — Casey has 1 year direct but 13+ adjacent
- Requires specific certifications Casey doesn't have
- Bay Area / NYC hybrid-only with no remote option

## Output Format (per lead in daily YYYY-MM-DD-job-scout.md)

### Active Postings (Recommend Applying)
```markdown
## [FIT: HIGH/MEDIUM/LOW] — [Company] – [Role Title]

- **Comp:** [range if listed, "Not listed" if not]
- **Location:** [Remote/Hybrid/City]
- **Company:** [one-line description, funding stage if known]
- **Link:** [URL]

**Fit:** [1-2 sentences. Key signal: Casey has 13 years enterprise tech sales (Red Hat, Kiewit, Burns & McDonnell) + hands-on AI/ML knowledge. A sales leader who can build what he sells is rare. Mention specific match.]

**Contact:** [Name from contacts.json if match found, "None in network" if not]

**Flag:** [Any anti-signals or concerns, or "None"]

---
```

### Stale Postings (Do Not Apply)
```markdown
## [STALE — EXPIRED] — [Company] – [Role Title]

- **Deadline:** [Expired date or "Posted [X] days ago"]
- **Location:** [Remote/Hybrid/City]
- **Link:** [URL]

**Reason:** Posting deadline passed / older than 60 days / marked closed. Do not apply.

---
```

**Status:** 
- Active postings: Default to NEW. Casey or SuperStan updates to APPROVED/SKIP/HOLD as needed.
- Stale postings: Status "STALE" (for reference only, no action required).

## Search Strategy — Source Hierarchy

### PRIMARY SOURCES (every run)
**1. LinkedIn Jobs** — highest quality signal, most reliable comp data, direct company attribution
   - Search: Target titles (Enterprise AE, Strategic AE, Account Executive, Sales Director, VP Sales) + "B2B SaaS" OR "AI" + "remote" OR "Texas"
   - Company filter: Apply watchlist company names (rotate subset per run)
   - Dedup: Check against applications.json surfaced entries before surfacing

**2. Company Career Pages** — direct from source, unlisted roles, company context visible
   - Rotation: Check 3–4 watchlist companies per run (24 companies = full cycle every 6 days)
   - Tracking: Log which companies checked and found nothing (reset weekly)
   - Scope: Sales roles only (Account Executive, Strategic Account Executive, VP Sales, Sales Director)
   - LinkedIn company pages: Also check LinkedIn company page for each watchlist company (unlisted roles sometimes posted there first)

### SECONDARY SOURCES (rotate 1–2 per run)
**3. Built In** (builtin.com) — strong for B2B SaaS, tech companies, good comp data
**4. Wellfound** (wellfound.com, formerly AngelList) — Series B+ AI/SaaS companies, founder visibility
**5. Y Combinator Work at a Startup** (ycombinator.com/work-at-startup) — later-stage YC companies with enterprise sales motion

### DEPRIORITIZE (fallback only if primary/secondary < 3 leads)
**6. RemoteRocketship** — aggregator board, lower comp, company context stripped
**7. Virtual Vocations** — aggregator, lower comp tier
**8. Indeed / Glassdoor** — broad but high noise, difficult to filter for high-comp roles
**9. USARemoteJobs** — aggregator, lower comp focus
**10. Google search** — "[title] AI company hiring 2026" (use only when nothing from primary/secondary)

### Company Watchlist (check career pages directly)
Maintain in applications.json under "watchlist" key. Updated list:

**B2B SaaS Giants (enterprise sales heavy):**
- Salesforce, ServiceNow, HubSpot, Slack, Figma, Stripe, Notion, Atlassian, Datadog

**AI/Automation Platforms:**
- Anthropic, OpenAI, Cohere, Mistral, Scale AI, Databricks

**Infrastructure/Data:**
- HashiCorp, Zilliz, Retool

**Security (enterprise):**
- Snyk, Wiz, Lacework

**Other B2B SaaS:**
- Miro, You.com

Casey can add/remove from watchlist at any time. Deprioritize pure research/ML labs. Focus on companies actively selling to enterprises and scaling their sales teams.

## Execution — Stan
1. Run at 6:45 AM CT daily (after X Content Scout completes)
2. Read applications.json to get: already-surfaced roles (dedup), watchlist companies, active applications
3. Read contacts.json to cross-reference company names
4. Execute web searches across 2-3 sources (rotate sources daily to cover all weekly)
5. **Validate posting dates:** Check for deadline, posted date, or closed/expired indicators. Mark stale postings (>60 days old, expired deadline, or closed indicator) as STALE and exclude from US-RELEVANT count.
6. Filter results against criteria (enterprise sales roles only, Texas/remote, $150K+ OTE, B2B SaaS/AI/automation, active postings only)
7. Score fit: HIGH (3+ fit signals, 0 anti-signals), MEDIUM (1-2 fit signals or minor anti-signals), LOW (interesting but stretch)
8. Select top 3-5 leads. Prioritize HIGH fit. Include at least 1 MEDIUM if fewer than 3 HIGH. Do not include STALE postings in final count.
9. Format output as YYYY-MM-DD-job-scout.md file (see format above)
10. **Dual output:**
    - Write file to Drive (job-scout/ folder, ID: 1_r4ykfESPOwiF6I1d3SfCYkjbReAfVEj)
    - Send summary to Telegram with lead links
11. Append all surfaced leads to applications.json with status "NEW" (active postings only; note stale postings separately with status "STALE")
12. If no leads meet criteria: "Job Scout: No strong matches today. [X] results scanned, [Y] stale/expired, none cleared the filter."

## Execution — SuperStan
Can run on-demand when Casey says "find me roles at [company]" or "search for [specific title]."
Same scoring and format. Write results to applications.json.

## Approval Flow
- Casey sees leads in Telegram
- Casey replies per lead: APPLY (Stan drafts application materials), TRACK (add to watchlist/later), or SKIP
- APPLY triggers: Stan drafts a tailored cover letter or outreach message, saves to applications.json with status "Applying"
- TRACK triggers: status update in applications.json to "Watching"
- SKIP triggers: status update to "Skipped"

## Application Follow-Up
Stan checks applications.json daily for:
- Applications with no response after 7 days → flag for follow-up in Telegram
- Interviews scheduled → prep briefing using research-log + contacts.json + company research
- Offers → surface in daily briefing as priority item

## Rules

**Application Rules:**
- Never apply to a job on Casey's behalf. Casey applies himself or explicitly tells Stan to submit.
- Never send outreach emails without Casey approval.
- Never expose FleetBrain internal architecture in application materials.
- If a role is at a company that could be a FleetBrain client, flag the conflict — Casey decides.

**Lead Quality Rules:**
- Never surface a lead without a company name. If the listing doesn't name the company, skip it (unverifiable).
- Don't surface the same role twice. Dedup by company + title + posting date against applications.json.
- Quality over quantity. 0 leads is fine if nothing fits the criteria.

**Company Tracking Rules:**
- When checking company career pages: also search that company's LinkedIn company page for unlisted roles (often posted there before external boards).
- If a watchlist company has been checked and has no open sales roles: note it in daily report as "checked, nothing open" to avoid wasting cycles on re-checks.
- Reset "checked, nothing open" flags weekly (every Sunday) — companies post new roles frequently.
- Maintain a spreadsheet or notes in MEMORY.md with: company name, last checked date, status (open roles / nothing open).

## Drive Archival
Each day's results persist to Drive in job-scout/ folder:
- **Folder ID:** 1_r4ykfESPOwiF6I1d3SfCYkjbReAfVEj
- **Path:** StanleyBot/job-scout/
- **File format:** YYYY-MM-DD-job-scout.md
- **Content:** All leads found that day with fit scores, links, and status
- **Telegram delivery continues:** Summary + key links delivered to Casey daily
- **Purpose:** Casey can review on his timeline, search/filter Drive for past leads, maintain application pipeline awareness

## Company Tracking (Prevent Wasted Checks)

Maintain a simple tracker in a separate file or MEMORY.md section:

```
Company Watchlist Tracking (reset weekly on Sundays)

Last Updated: YYYY-MM-DD

Datadog          — Last checked: 2026-02-25 — Status: Nothing open (sales team complete)
Slack            — Last checked: 2026-02-24 — Status: 1 Enterprise AE role open
Figma            — Last checked: 2026-02-23 — Status: Nothing open
Stripe           — Last checked: 2026-02-22 — Status: 2 Strategic AE roles open
Notion           — Last checked: 2026-02-21 — Status: Nothing open
[... etc for all 24 companies]
```

**Weekly Reset Logic:**
- Every Sunday morning (before first run): Clear "checked" dates and "nothing open" statuses
- This prevents permanently skipping companies that add new roles mid-week
- Keep "open" roles visible until they appear in applications.json as surfaced leads

## Cron Dependency
Runs AFTER X Content Scout (6:30 AM CT). Schedule at 6:45 AM CT.
Chain: CRM (6:00) → Briefing (6:15) → X Scout (6:30) → Job Scout (6:45)
**Output:** Telegram (summary) + Drive (full daily file)

## Status
UPDATED Feb 26, 2026 — Posting date validation filter added (checks deadline, posted date, closed/expired indicators). Stale postings (>60 days, expired deadline) marked as STALE and excluded from recommendation count. Prevents wasted applications on expired listings. Ready for cron execution with dual output (Telegram + Drive).
