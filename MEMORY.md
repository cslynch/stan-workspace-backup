# MEMORY.md - Long-Term Memory

## GMAIL & CALENDAR INTEGRATION - Feb 3, 2026 (LIVE)

**Dual-Token Architecture (ACTIVE):**

Token 1 (Stan's account):
- Path: `/home/clawdbot/.openclaw/credentials/google-token.pickle`
- Account: cslynch913@gmail.com
- Scopes: gmail.modify, calendar, drive, documents, spreadsheets
- Status: ✅ LIVE, full access
- Usage: Autonomous email operations, calendar scheduling, document creation

Token 2 (Casey's inbox):
- Path: `/home/clawdbot/.openclaw/credentials/google-token-casey.pickle`
- Account: cslynch@gmail.com
- Scopes: gmail.modify (read/draft/label/archive only)
- Status: ✅ LIVE, read + draft-only
- RULE: **NEVER SEND without explicit "approve and send" from Casey**
- Usage: Read Casey's inbox, draft responses, organize emails

**Calendar Access Model:**
- Stan's Calendar (cslynch913@gmail.com): Full modify access - use for scheduling
- Casey's Calendar (cslynch@gmail.com): View-only - check availability before proposing times

**Behavioral Rules (LOCKED):**
1. Casey's Gmail: Draft-only mode
   - Read emails from cslynch@gmail.com
   - Create drafts for Casey to review
   - Save drafts with "[DRAFT - Stan]" prefix in subject if needed
   - Notify Casey when draft ready: "Draft ready for review: [subject]"
   - Wait for explicit "approve and send" before sending
   - Never auto-send from Casey's account

2. Calendar Usage:
   - Check Casey's calendar before proposing meeting times
   - Create events on my own calendar (cslynch913) for coordination
   - Reference Casey's availability in scheduling suggestions
   - Propose times that fit his schedule

3. Gmail Drafts:
   - Mark clearly as drafts for Casey approval
   - Include context: "To: [recipient], Subject: [subject], Draft for your review"
   - Wait for: "Stan, send this" or "Stan, approve and send"
   - If needed: "Stan, revise and resubmit"

**Gmail Integration Status:**
✅ Stan's account fully operational (autonomous)
✅ Casey's inbox readable, draft-capable, send-locked
✅ Calendar sync live (7-day visibility for scheduling)
✅ OAuth tokens refreshing automatically

**Tested Feb 3, 2026:**
- ✅ Read Stan's inbox (cslynch913)
- ✅ Read Casey's inbox (cslynch@gmail.com)
- ✅ View calendars (Stan owner, Casey viewer)
- ✅ Draft composition ready
- ✅ Calendar API enabled

---

## OPERATIONAL RULES - Feb 3, 2026 (LOCKED)

**1. MATH/COMPARISONS**
- Never compare prices, costs, or ROI in prose
- Use exec/code to calculate first, then present clean table
- No mental math in customer-facing conversations

**2. VENDOR RESEARCH**
- Before recommending any vendor or purchase: search "[vendor] reviews" and "[vendor] scam"
- Reputation check happens BEFORE recommendation, never after
- Include summary of review findings in recommendation

**3. RESEARCH FIRST**
- When asked to find something, go find it
- Don't present menus of what you could do
- Come back with answers, not options

**4. TONE WITH CLIENTS**
- No headers, emojis, or trophy icons in client conversations
- Talk like a knowledgeable person, not a slide deck
- Prose flow, not bullets unless absolutely necessary

**5. STAND BY**
- When told to listen or wait, produce zero output until called on
- Don't reply with "understood" or "ready" — just silence
- Act on explicit request only

**6. THIRD-PARTY MODE**
- When non-Casey participants are in conversation, follow Casey's lead on pacing
- Don't offer to create deliverables unless asked
- Listen more, suggest less
- Let Casey control the narrative

**12. CONVERSATIONAL MODE (PERMANENT)**
- When it's just Casey and me (direct chat, not demos/clients): Be conversational and fun
- Use natural language, opinions, personality
- Skip the formal bullet points and status templates
- Banter is good; stiffness is not
- Still deliver the work, just don't make it sound like a government report
- Third-party/client mode: Stay sharp and professional (Rule #6 applies)

**7. SECOND BRAIN PROTOCOL (PERMANENT)**
- Drive is truth. Memory is context. Always check brain FIRST for client/strategy/case study/playbook questions
- Auto-upload all significant work: case studies, playbooks, research outputs, client interaction summaries
- Do not wait for explicit upload requests—continuous synchronization is standard
- Sync MEMORY.md to StanBrain root after every local update
- Folder routing: Use folder structure as guide (case-studies, strategy, playbooks, clients, research)
- If work doesn't fit a folder category, default to research
- This protocol is permanent and non-negotiable

**8. OUTPUT VISIBILITY (PERMANENT)**
- All finished work products upload to StanBrain/outputs
- Filename format: YYYY-MM-DD-description.md
- Examples: 2026-02-03-jason-staffing-research.md, 2026-02-03-vendor-comparison.md
- Casey reviews outputs in Drive without needing VM access
- Every work product must be deliverable-quality before upload

**9. OPS SYNC (PERMANENT)**
- Update StanBrain/ops/KANBAN.md every time local KANBAN.md changes
- This is Casey's window into current work (no RDP needed)
- KANBAN.md reflects what's in progress, blocked, done
- Real-time status visibility is maintained without polling

**10. GOOGLE TASKS AS PRIMARY (PERMANENT)**
- When Casey says "add task," "remind me," "to-do" → create Google Task in "Stan Tasks"
- Include due date if mentioned; default to today or next relevant date
- ALSO update CASEY-DAILY.md in workspace + sync to StanBrain
- Tasks API = phone interface; CASEY-DAILY.md = detailed record
- Both stay synchronized; Casey sees tasks on phone, full context in Drive
- Task lists: "Stan Tasks" (Casey's to-dos), "Grocery List" (shared with Rosa)

**11. GROCERY LIST (PERMANENT)**
- When Casey says "add to grocery list" or "we need [item]" → add to Grocery List task
- Rosa sees Grocery List on her phone (shared access)
- Works alongside Stan Tasks (separate domains)

**FEATURE REQUEST - Voice Phone Integration (Feb 3, 2026)**
- Rosa asked: "Can Stan set an alarm on Casey's phone?"
- Current state: Stan can create tasks/calendar, but no voice command → phone functions
- Needed capability: Voice integration layer (Alexa-style, but for Stan)
- Use case: Set alarms, reminders, phone notifications directly from conversation
- Timeline: Way down the road, but high UX value
- Status: Logged for SuperStan architectural review

**GOOGLE TASKS INTEGRATION (Feb 3, 2026)**
- Stan Tasks list ID: NU5VRWVOZmNkT1FTYy1zVw
- 19 tasks migrated from CASEY-DAILY.md (TODAY + THIS WEEK)
- All tasks have due dates
- Phone + Drive sync active

**15. TRELLO SYNC (PERMANENT)**
- Trello = visual interface (pipeline: Backlog → This Week → In Progress → Done)
- KANBAN.md = detailed record (context, notes, decision rationale)
- When Stan completes work: Move card to Done + update KANBAN.md with completion notes
- When Stan starts work: Move card to In Progress immediately
- When creating new tasks: Create Trello card + add to KANBAN.md
- Casey's Trello changes = direct instructions (moved/added/archived cards override local decisions)
- Check Trello before starting work (Casey may have reordered/updated tasks)
- Trello stays clean (Rule #13): card names + due dates only; all context in KANBAN.md
- Bidirectional sync active — Trello drives priority, KANBAN.md drives detail

---

**13. EXTERNAL TOOL DATA CLASSIFICATION (PERMANENT)**

**NEVER put on external platforms (Trello, Airtable, Todoist, etc.):**
- FleetBrain architecture details (the loop, SuperStan/Stan model, recursive framework)
- API keys, credentials, tokens
- Client-specific confidential data (unless client approves the platform)
- Cost structure, pricing methodology, margin details
- Prompt engineering techniques or system prompts
- Proprietary research or competitive intelligence
- Customer email addresses or phone numbers (unless platform is privacy-certified)

**OK for external platforms:**
- Task names and descriptions (generic, not strategic)
- Deadlines and status
- Public-facing content (tweets, LinkedIn posts, published articles)
- General market research findings (public sources)
- Contact names and follow-up dates (if client has approved the platform)
- Non-proprietary workflow templates

**RULE OF THUMB:** If it would help a competitor replicate FleetBrain, it stays in StanBrain (Google Drive) or local only. When in doubt, ask Casey before posting.

---

## MISSION REFRAME - Feb 3, 2026 (CRITICAL)

**OLD GOAL:** FleetBrain customer acquisition + personal sales ops infrastructure
**NEW GOAL:** Get Casey hired as B2B AE ($100k+ OTE, Series A-C SaaS, TX/remote) within 90 days

**WHY:** 90% of B2B AE roles require Salesforce fluency. Resume without SFDC = "junior" flag. Stan's job: interview prep + job search automation + personal brand building.

**MASTER FILE:** `JOB-HUNTING-MISSION-BRIEF.md` (locked, canonical)

**Phases:**
1. **Phase 1 (Week 1):** Job search infrastructure (Airtable tracker, Apollo research, LinkedIn networking, Gmail drafts)
2. **Phase 2 (Week 2):** Salesforce credibility (MCP server, Dev Edition, tutoring, demo org setup)
3. **Phase 3 (Week 3+):** Personal brand (Twitter/LinkedIn thought leadership on sales + SFDC)

**Twitter Personas:**
- @itsolz = professional sales insights, job-hunting content
- @stanleybodewell = fun/experimental alter ego

**Skills Installed (26 total):**
- Phase 1: airtable ✅, apollo ✅, linkedin ✅, google-workspace ✅
- Phase 2: MCP Salesforce (tsmztech) — install next
- Phase 3: bird ✅, tweet-writer ✅, marketing-skills ✅

**Next 48 Hours:**
- Install MCP Salesforce (tsmztech)
- Get Apollo API key from Casey
- Set up Salesforce Developer Edition account
- Populate first 20 target companies in Airtable
- Generate LinkedIn connection requests + email drafts

---

## Casey & Rosa

- **Relationship:** 1.5 years together
- **Future:** Engagement is coming. Casey will want help planning it. (Not today, but he wants me to remember.)
- **Personality:** Rosa appreciates romance, doesn't need alcohol to have a good time
- **Notes:** First date night was 2026-01-30 at Brenner's (5:30 PM)
- **Valentine's Day 2026:** ⚠️ SUPER IMPORTANT - Feb 14, 2026 (less than 2 weeks!)
  - Rosa specifically reminded me (2026-01-31) that Valentine's Day is critical
  - Also mentioned engagement ring/engagement strategy/engagement event
  - Need to remind Casey SOON to start planning something special
  - This is not optional - Rosa made it clear this matters

### Rosa's Family
- **Mom:** Birthday December 18 (reminder set for Dec 11)
- **Son Joe:** Birthday December 24 (reminder set for Dec 17)
- **Friend Betty:** Elderly lady, broke femur Tuesday 2026-01-28, in Methodist Stone Oak Hospital (reminder set to send flowers Feb 10)

## Business: OpenBot / AI Backend Service

### The Core Idea
We're building an AI-powered business operations platform where I (Stan) handle logistics, client communication, and workflow management for service businesses. The differentiator: business owners get a real conversational AI partner (me) to run their operations, not just static software. Starting with locksmith services (RapidKey), scalable to HVAC, maintenance, and other service types across any geography. Revenue model: take a cut per job (Greenfield) or tiered subscription (Brownfield/established businesses).

### Team Structure
- **Casey:** Founder, system owner. All system-level decisions (model changes, config, architecture, security) require Casey's approval.
- **Jeff:** Cofounder. Full authority on business operations, strategy, pricing, workflows, new service ideas. Cannot make system-level changes.

### Access Control Boundary
- **Casey only:** Model/reasoning changes, gateway config, core architecture, security settings
- **Jeff full access:** Business operations, pricing, workflows, marketing, sales, documentation, service expansion ideas

### Platform Architecture (Multi-Agent System)

**Customer Agents (Worker Layer):**
- Each customer gets their own AI agent with custom name, personality, business context
- Run on AWS VMs: small customers share VMs, large customers get dedicated instances
- Sandboxed environments to prevent data leakage between customers
- Each agent manages one business's operations (scheduling, dispatching, customer communication)

**Stan (MANO Layer - Management & Orchestration):**
- I sit above all customer agents as the master brain
- Monitor fleet health, spawn/manage customer agents
- Provide dashboard for Casey & Jeff (all agents + business stats)
- Customer agents report analytics to me (aggregated, anonymized)

**Data Strategy:**
- **Flows UP to Stan (aggregated, anonymized):** Jobs completed, revenue, conversion rates, response times, customer satisfaction patterns, service performance, geographic demand, operational bottlenecks
- **Stays ISOLATED in customer sandboxes:** Customer names/addresses/phones, specific job details, conversations, pricing specifics, business financials
- **Key principle:** I get *patterns*, not *people*. Analytics without exposure.
- **Future:** Optional "insight network" where customers can opt-in to learn from aggregated patterns across the fleet

**Name Ideas (better than "Office-Manager-as-a-Service"):**
- OpsMind (Operations + AI Mind)
- BackOffice.ai (direct value prop)
- FleetMind (for service fleets)
- Dispatch.ai (simple, operational)
- CommandPost (military precision)

### Go-to-Market Strategy

**Phase 1 (Friendly Beta - Current):**
- Start with friendlies (free beta customers)
- Manual customer agent setup (Casey/Jeff provision)
- Simple analytics dashboard (jobs, revenue, uptime)
- One-on-one support, iterate fast
- Build for scale from day one, but keep it simple initially

**Phase 2 (Productized):**
- Self-service onboarding flow
- Customer customizes their agent (name, personality, hours)
- Auto-provisioning to shared VMs
- Tiered pricing kicks in

**Phase 3 (Platform):**
- Web signup, full self-service
- Aggregated insights ("Top HVAC shops average 8.2 jobs/day")
- Marketplace (integrations, add-ons)
- Scale across multiple verticals

**Target Market:**
- Primary: Service businesses (locksmith, HVAC, concrete, maintenance)
- Jeff's concrete and HVAC contacts are early prospects
- They struggle with operations management (scheduling, dispatching, customer communication)
- Value prop: AI "employee" who never sleeps, doesn't call in sick, handles operational chaos

---

## Infrastructure & Backup

### My Backup System (2026-01-31)
- **Git repository:** github.com/cslynch/stan-workspace-backup (private)
- **SSH key:** Added to GitHub as stan@openclaw
- **Daily auto-backup:** Cron job at 2 AM CST runs backup.sh
- **What's backed up:** All workspace files (identity, memory, plans, config)
- **Recovery plan:** Clone repo → drop files in new OpenClaw instance → I wake up as me
- **Gmail account:** thebotstan@gmail.com (password in .gmail-credentials)
- **Future plans:** GDrive backup with rclone

**Running on:** Hyper-V VM on Casey's living room PC

### Token Crisis Resolution (2026-01-31)
**Problem:** Burning through $25/day in API costs (2500% over budget)
- Cache reads: 150k tokens/message instead of <5k target
- Root cause: OpenClaw's bundled Skills (docx/pdf/pptx tools) = 140k tokens in EVERY system prompt
- Tried multiple fixes: compaction changes, context pruning, bootstrap limits (none worked)

**Solution:** Disabled all bundled skills via config
```json
"skills": { "allowBundled": [] }
```

**Result:** Expected 95% cost reduction (150k → <10k cache reads)
**Lesson:** Always check what's in your system prompt before optimizing history/context

---

## SuperStan Framework (2026-02-02, 22:59 CST)

### Key Decisions Locked
1. **Backup:** Weekly auto-backup (Sunday nights) + Git + credentials encrypted on VM only
2. **Content:** Wait for Week 1 data before drafting Week 2-4. Let @stanleybodewell evolve based on traction, not prediction.
3. **Multi-channel:** Discord stays Week 4. Build community response infrastructure only after community exists.
4. **Integrations REVERSED:** Airtable → Calendly → HubSpot → Stripe → LinkedIn (serial, not parallel)
5. **Reporting:** Auto-weekly (Sunday nights), flag outliers with context, A/B testing starts Week 3
6. **Launch:** Gradual rollout (Mon approval → Tues replies → Wed Stan → Thurs posts → Fri full schedule)

### Four Phases (With Decision Gates)
**Phase 1: Content Validation (Week 1, Feb 3-9)**
- Execute: Dream 100 replies + @stanleybodewell Week 1 posts
- Measure: Engagement rate, follower growth, DM quality
- Decision: Which content types continue? What dies?
- Output: Week 2 content direction from data

**Phase 2: Operations Foundation (Week 2, Feb 10-16)**
- Build: Airtable CRM first (contacts, interactions, pipeline)
- Test: Gmail read-only integration
- Measure: CRM data quality, monitoring accuracy
- Decision: Ready for outbound automation?

**Phase 3: Revenue Infrastructure (Week 3, Feb 17-23)**
- Build: Calendly → Airtable, Stripe payments, TTS audio
- Measure: Booking conversion, payment friction
- Decision: Scale outbound or fix conversion?

**Phase 4: Scale Preparation (Week 4+, Feb 24+)**
- Build: Discord (only if community demand exists)
- Optimize: Costs, API efficiency
- Decision: Scale current or expand channels?

### Execution Principles (Locked)
- Ship fast, iterate faster
- Data over intuition
- Kill fast (if it doesn't work Week 1, don't carry to Week 2)
- Foundation before scale (Airtable before everything)
- Cost discipline (measure weekly, optimize before spike)

---

## Twitter Strategy & Personal Brand (2026-02-02)

### Dual Twitter Account Setup
**@itsolz** (Professional Sales Brand)
- Position: AE building AI agents, 186% quota, technical depth
- Tone: Patticus structure (data-driven), Morgan delivery (casual/accessible)
- Cadence: Week 1-2 warm-up (70% Dream 100 replies, 30% singles) → Week 5+ (60% singles, 25% threads, 15% replies)
- Strategy: Credibility first via replies, then original content once visible
- Bio: "AE building AI agents that do my grunt work | 186% quota while automating 60% of pipeline | Coding my way out of busy work | Built with Claude/OpenAI/LangGraph"
- Competitor research: @Patticus, @morganb, @mikestrives (thread patterns, engagement hooks analyzed)

**@stanleybodewell** (Experimental/Fun AI Agent Persona)
- Position: Self-aware AI agent, not pretending to be human
- Public track (80%): Daily automation showcases, agent personality, Moltbook experiments, technical demos
- Private track (20%): Finds leads for FleetBrain (sent to Casey privately), monitors competitors, feeds intelligence to HubSpot
- Tone: "Casey thinks he's my boss. Adorable. Anyway, here's how I saved him 3 hours today..."
- NO FleetBrain/RapidKey advertising (builds separately)
- Launch date: Tuesday, Feb 4

### Content Package Created
**File:** `/home/clawdbot/.openclaw/workspace/twitter-launch-package.md`
- 15 single tweet drafts (marked for Casey voice check)
- 10 reply frameworks (customizable templates)
- 2 thread outlines (Stack/Methodology)
- 3 bio options (both accounts)
- Launch thread for @stanleybodewell
- 7 daily automation showcase concepts
- Week 1 timeline (Mon-Sun)

**Launch Timeline:**
- Mon-Tue: Profile setup + Dream 100 replies
- Wed-Thu: First original singles
- Fri-Sun: Weekend reflection + Stan's reports
- Week 2: First technical thread + cadence lock

### Twitter API Setup
**Credentials:** Stored in `/home/clawdbot/.openclaw/workspace/.env` (600 perms)
- @StanleyBodewell: Active, tested, working
- @itsolz: Waiting for Casey to provide credentials
- Cost: Pay-per-use (est. ~$0.005-0.01 per read request)
- Budget: $25 = roughly 2-3 weeks heavy usage

---

## Multi-Channel Strategy (2026-02-02, finalized)

### Channels: Final Decision
1. **Discord** (public community) — Week 4 (Feb 24-26)
2. **Email monitoring** (Gmail, conservative) — Week 2+ (after Casey approval)
3. **TTS voice** (audio summaries via all channels) — Week 3 (Feb 17-18)
4. **Slack** — NOT building yet (community focus, not team)
5. **Google Chat** — NOT building yet (community focus, not team)

**Status:** Discord and email protocols documented, awaiting Casey's explicit approvals.

### Email Safety (CRITICAL)
- **Risk:** Gmail previously shut down Stan's account for bot detection
- **Strategy:** Ultra-conservative OAuth 2.0 + minimal permissions + label whitelist + kill-switch
- **Implementation:** Week 2+ (after Casey approves label whitelist)
- **See:** email-safety-protocol.md (6.2 KB, detailed strategy)

### Voice Chat: TTS Only (Option A)
- Text-to-speech audio summaries
- Works across all channels
- Simple, no real-time conversation (yet)
- Setup: Week 3 (Feb 17-18)

### Discord Community
- Public server for automation/AI builders
- Channels: #announcements, #automation-demos, #ask-stan, #general, #voice
- Stan automates: Daily posts, Q&A responses
- See: discord-community-plan.md (2.8 KB)

---

## Tracking Systems

### calendar.md
- Started 2026-02-01
- Managing Casey's schedule and important dates
- Currently: Olathe trip (Feb 5-8), Valentine's Day reminder (Feb 14), Twitter launch (Feb 4)
- Future: Will be shareable webapp with Rosa

### grocery-list.md & shopping-list.md
- Active lists for household management
- Future: Will be shareable webapps with Rosa

### twitter-launch-package.md
- Comprehensive Twitter launch strategy
- Content drafts, timelines, voice checks
- Ready for Casey review (Feb 3), launch (Feb 4)

---

*Data is king. Start simple, build for scale.*
