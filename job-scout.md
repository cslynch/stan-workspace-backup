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
- AI Sales Executive / AI Sales Director
- Enterprise Account Executive (AI/ML companies)
- AI Transformation Sales / Digital Transformation Sales
- Solutions Consultant / Solutions Engineer (AI platforms)
- Director of Sales, AI / Automation
- Strategic Account Executive (AI, automation, enterprise software)
- VP Sales (startup/scaleup, AI-focused)

### Secondary Titles (surface if strong fit)
- Revenue Leader / Head of Revenue (AI companies)
- Sales Engineer / Pre-Sales Engineer (AI/ML platforms)
- Business Development Director (AI/enterprise)
- GTM Lead (AI startups)

### Filters
- **Geography:** Remote (US), Hybrid (Austin TX, San Antonio TX). Open to North American territory roles.
- **Company stage:** Series A through public. No pre-seed/seed unless comp is strong.
- **Industry:** AI/ML platforms, enterprise SaaS, automation, AI consulting, AI infrastructure. Adjacent: cybersecurity with AI focus, cloud platforms with AI GTM motion.
- **Comp:** $150K+ OTE preferred. Flag anything below $120K base as low-comp.
- **Exclude:** Pure SDR/BDR roles. Pure marketing roles. Non-enterprise (SMB-only). Roles requiring 50%+ travel (flag 25-50% for Casey's decision).

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

## Output Format (per lead)
```
🎯 JOB LEAD — [FIT: HIGH/MEDIUM/LOW]

Role: [Title]
Company: [Name] — [one-line description, funding stage if known]
Location: [Remote/Hybrid/City] | Comp: [range if listed, "Not listed" if not]
Link: [URL]

Fit: [1-2 sentences — why this matches Casey's background. Be specific.]
Contact: [Name from contacts.json if match found, "None in network" if not]
Flag: [Any anti-signals or concerns, or "None"]
```

## Search Strategy

### Sources (rotate daily, hit all weekly)
1. **LinkedIn Jobs** — primary source. Search target titles + "AI" + "remote"
2. **Built In** — AI/tech company job boards
3. **Wellfound (AngelList)** — startup roles, often higher equity comp
4. **Company career pages** — for specific companies Casey is tracking (maintain a watchlist)
5. **Indeed / Glassdoor** — broad sweep, filter aggressively
6. **Y Combinator Work at a Startup** — AI startups scaling sales
7. **Google search** — "[title] AI company hiring 2026" for recent postings

### Company Watchlist (check career pages directly)
Maintain in applications.json under "watchlist" key. Initial list:
- Anthropic, OpenAI, Cohere, Mistral (foundation model companies)
- LangChain, LlamaIndex, CrewAI, AutoGen (agent framework companies)
- Scale AI, Weights & Biases, Databricks, Snowflake (AI infrastructure)
- Salesforce AI, ServiceNow, HubSpot (enterprise with AI GTM)
- Palantir, C3.ai, DataRobot (AI enterprise sales)

Casey can add/remove from watchlist at any time.

## Execution — Stan
1. Run at 6:45 AM CT daily (after X Content Scout completes)
2. Read applications.json to get: already-surfaced roles (dedup), watchlist companies, active applications
3. Read contacts.json to cross-reference company names
4. Execute web searches across 2-3 sources (rotate sources daily to cover all weekly)
5. Filter results against criteria
6. Score fit: HIGH (3+ fit signals, 0 anti-signals), MEDIUM (1-2 fit signals or minor anti-signals), LOW (interesting but stretch)
7. Select top 3-5 leads. Prioritize HIGH fit. Include at least 1 MEDIUM if fewer than 3 HIGH.
8. Format output and send via Telegram
9. Append all surfaced leads to applications.json with status "Surfaced"
10. If no leads meet criteria: "Job Scout: No strong matches today. [X] results scanned, none cleared the filter."

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
- Never apply to a job on Casey's behalf. Casey applies himself or explicitly tells Stan to submit.
- Never send outreach emails without Casey approval.
- Never expose FleetBrain internal architecture in application materials.
- If a role is at a company that could be a FleetBrain client, flag the conflict — Casey decides.
- Don't surface the same role twice. Dedup by company + title + posting date.
- Quality over quantity. 0 leads is fine if nothing fits.

## Cron Dependency
Runs AFTER X Content Scout (6:30 AM CT). Schedule at 6:45 AM CT.
Chain: CRM (6:00) → Briefing (6:15) → X Scout (6:30) → Job Scout (6:45)

## Status
ACTIVE — skill definition complete. Requires Stan cron setup and applications.json initialization.
