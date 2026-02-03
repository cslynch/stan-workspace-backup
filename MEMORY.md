# MEMORY.md - Long-Term Memory

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
