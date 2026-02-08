# KANBAN - Project Status
**Last Updated:** Feb 8, 2026 09:15 CST  
**Updated By:** Stan (Master Tracker Sync)
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

### INFRASTRUCTURE (Critical Path - Feb 8)
- [ ] Verify Google Workspace domain (fleetbrain.ai) — phone rate limit reset check
- [ ] Install Tailscale on Mater + phone
- [ ] GPG encrypt .env on VM (DONE Feb 8 03:43)
  - ✅ Encrypted with passphrase stored in Bitwarden
  - ✅ File: /home/clawdbot/.openclaw/workspace/.env.gpg (819 bytes)
- [ ] Fix email routing — send from cslynch913@gmail.com only, never cslynch@
- [ ] Update OpenClaw to v2026.2.6 (awaiting Casey go-signal)

### SECURITY (Feb 8-10)
- [ ] Run `openclaw security audit --fix` (tighten file permissions)
- [ ] Install Clawdex + scan all 27 installed skills
- [ ] Run Snyk mcp-scan against skill configs
- [ ] Remove unused skills (reduce from 27 to essential set)
- [ ] Fix email OAuth scoping (cslynch@ = drafts only, not send)
- [ ] Grep workspace for dead references (thebotstan@, LastPass, 1Password)

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

## BLOCKER ITEMS (External Dependencies)

| Item | Blocker | Status | Note |
|------|---------|--------|------|
| OpenClaw v2026.2.6 | Casey approval | Waiting | Available but not installed yet |
| Twitter launch | Casey content approval | Waiting | Content drafted, needs voice check |
| Job search outreach | Casey Apollo key + LinkedIn creds | Partial | Airtable ready, hiring research needs manual assist |
| Salesforce Phase 2 | Casey Dev Edition signup | Waiting | Creates interview prep infrastructure |
| Tailscale auth | Casey setup on phone | Waiting | Installed on Mater, needs pairing |
| Google Workspace verification | Phone rate limit reset | Pending | Check by Feb 8 EOD |
| Case study writeups | Telegram chat exports | Waiting | Need Ryan + Deb conversation logs |

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

**Status Summary:**
- **Infrastructure:** 5 items due This Week (2 done, 3 in progress)
- **Security:** 6 items due This Week (0 done, ready to execute)
- **Stan Ops:** 7 items due This Week (1 in progress — case studies)
- **Websites:** 4 items in progress (no due date set)
- **Business:** 3 items in progress (Twitter waiting approval)
- **Job Search:** 3 items active (Phase 1)
- **Filing:** 3 items in progress

**Total:** 34 active items, 7 deferred, 2 blocked on external, 3 blocked on Casey action

Standing by for Trello board state or API access instruction.
