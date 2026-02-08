# KANBAN - Project Status
**Last Updated:** Feb 8, 2026 11:06 CST  
**Updated By:** Stan (Phase 2 Sync: Completed Items Moved to DONE)
**Trello Board:** StanOps (sync via Rule #15: clean names on Trello, detail in KANBAN.md only)

---

## BACKLOG (To Start - No Due Dates)

### DEFERRED ITEMS
- [ ] Docker sandboxing for Stan VM
- [ ] Audit 27 ClawHub skills for security
- [ ] Credential rotation schedule
- [ ] Separate dangerous tool combinations
- [ ] Connect Stan to Salesforce dev org
- [ ] Salesforce tutoring sessions
- [ ] Finish Jake bootstrap (OpenClaw + Telegram bot on Lightning)

### Claude.ai Integration Watch
- [ ] **Monitor for native Trello/MCP connector**
  - Watch for: claude.ai MCP server support, Trello integration, connector marketplace launch
  - Trigger: Flag immediately with source link if found (Rule #16)
  - Impact: Would eliminate manual Trello sync layer

### Email Configuration (Blocked on Casey)
- [ ] Casey: Provide Gmail label whitelist
- [ ] Stan: Implement OAuth flow
- [ ] Stan: Test read-only access
- [ ] Casey: Explicit authorization
- [ ] Stan: Activate monitoring

---

## THIS WEEK (Due Feb 8-14)

### INFRASTRUCTURE (Critical Path - Feb 8) - ALL COMPLETE ✅
- [x] ✅ OpenClaw v2026.2.6 installed and running (Feb 8 09:26)
- [x] ✅ Tailscale authenticated, connected (IP: 100.71.67.28, Feb 8 09:46)
- [x] ✅ Verify Google Workspace domain (fleetbrain.ai active, Feb 8 09:50)
- [x] ✅ GPG encrypt .env on VM (Feb 8 03:43, stored in Bitwarden)
- [x] ✅ Fix email routing (cslynch913@gmail.com primary, verified)

### SECURITY (Feb 8-10) - PARTIALLY COMPLETE
- [x] ✅ Run `openclaw security audit --fix` (file permissions tightened, Feb 8 09:59)
- [x] ✅ Skills audit complete (56 eligible, 21 ready, 36 bloat identified, Feb 8 10:00)
- [x] ✅ Grep workspace for dead references (thebotstan removed, stan-config-export.txt deleted, Feb 8 10:04)
- [ ] Install Clawdex + scan (command not found - not available)
- [ ] Run Snyk mcp-scan (installed but mcp-scan command doesn't exist)
- [ ] Remove unused skills (36 identified, awaiting execution)
- [ ] Fix email OAuth scoping (review needed)

### CASE STUDY WORK (Feb 8-10)
- [ ] Export Telegram chat logs (Ryan + Deb conversations)
- [ ] Compile evidence for case studies #0, #2, #3, #4, #5, #6
- [ ] Gather screenshots + conversation transcripts
- [ ] Apply anonymization rule to all external-facing output

### TAILSCALE AUTH (✅ COMPLETE - Feb 8)
- [x] **Set Tailscale operator permissions on Mater VM**
  - ✅ Operator permissions set
  - ✅ Tailscale authenticated on phone
  - ✅ Connected: 100.71.67.28 (clawdbot-vm)
  - **Status:** DONE

### TELEGRAM & CONFIG (✅ COMPLETE - Feb 8)
- [x] ✅ Change Telegram DM policy to "pairing" (Random users blocked, Feb 8 09:50)
- [x] ✅ Dead reference purge (thebotstan removed, config export deleted, Feb 8 10:04)

### STAN OPS (Feb 8-14)
- [ ] Regenerate 7 StanBrain research files (verify with ls after upload)
- [ ] Push verification loop correction (3-layer, permanent rule)
- [ ] Install browser skills (playwright-cli / agent-browser)
- [ ] Push proactive behavior correction (Rosa pattern — flag important dates/needs)
- [ ] Set up recurring task: Monthly AI tool landscape scout (first: March 3)
- [ ] Complete Rosa vacation research (T&C and FL Keys pricing gap analysis)
- [ ] Push fourth-wall leak rule to default agent baseline

---

## IN PROGRESS

### WEBSITES & BRAND (In Build - Feb 8+)
- [ ] Set up DNS records (GoDaddy → GitHub Pages)
- [ ] Set up email forwarding (casey@fleetbrain.ai → Casey's inbox)
- [ ] Deploy fleetbrain.ai to GitHub Pages (site in Claude Code)
- [ ] Deploy stanleybot.fleetbrain.ai to GitHub Pages

### BUSINESS DEVELOPMENT
- [ ] Jason Rawlings follow-up / two-node demo prep
- [ ] Apply for Google Workspace Reseller program
- [ ] Twitter launch — both accounts (awaiting Casey go-signal)
  - [ ] @itsolz: Professional sales brand
  - [ ] @stanleybodewell: Experimental AI agent persona

### JOB SEARCH (Phase 1 Active)
- [ ] Update LinkedIn profile (research 5 top profiles, audit Casey's, gap analysis)
- [ ] Launch job search automation (20 companies, B2B AE, Series A-C, $100k+ OTE)
- [ ] Export LinkedIn data for relationship intelligence mapping

### FILING & DOCUMENTATION
- [ ] File FleetBrain logo (Mark B) to StanBrain
- [ ] File website content briefs to StanBrain
- [ ] Update bootstrap runbook (Lightning/Jake, phases 5+)

---

## DONE (Completed - Feb 3-8)

- ✅ GPG encrypt .env on VM (Feb 8 03:43) — Passphrase: [stored in Bitwarden]
- ✅ Email routing verified (cslynch913@gmail.com configured as primary send account)
- ✅ MEMORY.md trimmed to 3976 bytes (under 8000 char bootstrap limit)
- ✅ Sessions cleared & bloat fixed (Feb 8 03:36)
- ✅ Model corrected to claude-haiku-4-5 (Sonnet → Haiku)
- ✅ Twitter infrastructure live (@itsolz + @stanleybodewell)
- ✅ Content drafted (twitter-launch-package.md, stanleybodewell-week-1-posts.md)
- ✅ Dream 100 research complete
- ✅ Job search Airtable base (25 companies populated)
- ✅ Apollo API tested & working
- ✅ GitHub backup active (auto-commits daily)
- ✅ Case study evidence search (6 case studies: #0-#6)
- ✅ Anonymization rule locked (Rule #18)

---

## BLOCKER ITEMS (Remaining External Dependencies)

| Item | Blocker | Status | Note |
|------|---------|--------|------|
| Twitter launch | Casey content approval | Waiting | Content drafted, needs voice check |
| Job search outreach | Casey Apollo key + LinkedIn creds | Partial | Airtable ready, hiring research needs manual assist |
| Salesforce Phase 2 | Casey Dev Edition signup | Waiting | Creates interview prep infrastructure |
| Case study writeups | Telegram chat exports | Waiting | Need Ryan + Deb conversation logs |
| Rosa vacation research | Pricing data completion | In Progress | T&C and FL Keys pricing gap analysis needed |

---

## TRACKING & METRICS

### Weekly Reporting (Sundays, 5pm CST)
- Task completion rate
- Infrastructure status
- Cost tracking
- Twitter metrics (when launched)

### Next Report
- Sun Feb 9 (Week 1 wrap-up from Twitter if live)
- Sun Feb 16 (Infrastructure readiness check)
- Sun Feb 23 (Stan Ops progress)

---

## RULE #13 APPLICATION (Trello + KANBAN Sync)

**Trello Card Names:** Clean, short, action-oriented
- "Verify Google Workspace domain"
- "Install Tailscale"
- "GPG encrypt .env" ✅
- etc.

**KANBAN.md:** Full context, blockers, dependencies, notes
- All detail lives here
- Trello stays visual only
- Both sync bidirectional (Trello priority changes override local decisions)

---

## CURRENT BOARD STATE NEEDED

**Question for Casey:**
What's the current state of your Trello StanOps board? I can:
1. **Option A:** Read Trello directly if you give me board access (would need API setup)
2. **Option B:** You tell me the current card structure, I ensure KANBAN.md matches, then we keep them in sync
3. **Option C:** I create all new cards locally in KANBAN.md, you manually create/update on Trello

Which works best?

---

**Status Summary (Feb 8, 2026 11:06 CST):**
- **Infrastructure:** 5 items (✅ 5 complete/verified)
- **Security:** 6 items (✅ 3 complete, 3 pending/blocked on tools)
- **Telegram & Config:** 2 items (✅ 2 complete)
- **Case Study Work:** 4 items (0 done, awaiting Telegram exports)
- **Stan Ops:** 7 items (0 done, prioritized)
- **Websites:** 4 items in progress
- **Business:** 3 items in progress (Twitter waiting approval)
- **Job Search:** 3 items active (Phase 1)
- **Filing:** 3 items in progress

**Total:** 32 active items, 7 deferred, 5 blocked on external dependencies, 4 blocked on Casey action
**Completed This Session:** 10 items (Infrastructure 5 + Security 3 + Telegram/Config 2)

Standing by for Trello board state or API access instruction.
