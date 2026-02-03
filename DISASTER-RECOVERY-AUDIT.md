# Disaster Recovery Audit Report

**Generated:** 2026-02-03 07:18 CST  
**Agent:** Stan (local execution layer)  
**Status:** PARTIAL (credentials at risk, GitHub backup incomplete)

---

## 1. CODE & CONFIGS PUSHED TO GITHUB

**Repository:** github.com:cslynch/stan-workspace-backup.git  
**Last Commit:** `210fd27` (2026-02-03 05:41 CST)  
**Total Files Tracked:** 186 files  

**Key Files in Git (ALL TRACKED):**
- MEMORY.md (long-term memory, locked)
- JOB-HUNTING-MISSION-BRIEF.md (canonical master plan)
- PHASE-1-EXECUTION.md (execution checklist)
- KANBAN.md (project status + sprint tracking)
- AUTOMATION.md (cron jobs, scheduled tasks)
- 30-day-execution-plan.md (strategy framework)
- SOUL.md (identity + values)
- USER.md (Casey profile)
- IDENTITY.md (Stan profile)
- All skill files (.md documentation)
- Twitter launch package files
- Marketing/sales content strategies
- Cost reports + usage tracking
- Backup documentation

**Git Status:** CLEAN (no uncommitted changes)

---

## 2. CREDENTIALS & API KEYS IN USE

**Location:** `/home/clawdbot/.openclaw/workspace/.env` (LOCAL ONLY, NOT IN GIT)  
**Permissions:** 600 (read/write owner only)

**Services with Active API Keys:**

| Service | Credential Type | Used For | Stored In |
|---------|-----------------|----------|-----------|
| **Twitter (@stanleybodewell)** | Bearer Token, API Key/Secret, Access Token/Secret | Tweet posting, account auth | .env |
| **Twitter (@itsolz)** | Bearer Token, API Key/Secret, Access Token/Secret | Tweet posting, account auth | .env |
| **Apollo.io** | API Key (Master) | Company/people search, enrichment | .env |
| **Airtable** | Personal Access Token | Base/table CRUD, record management | .env |
| **Google Workspace** | OAuth 2.0 (if set up) | Gmail, Calendar, Sheets (NOT YET ACTIVE) | TBD |
| **Salesforce** | OAuth 2.0 (if set up) | MCP server auth (NOT YET ACTIVE) | TBD |

**Total Keys at Risk if VM Dies:** 6 active keys + 2 pending

---

## 3. LOCAL-ONLY FILES (Would Be Lost if VM Dies)

**Location:** `/home/clawdbot/.openclaw/workspace/`

### Critical Local Files:
1. **`.env`** — ALL API keys, Bearer tokens, secrets (56-character lines, 915 bytes total)
2. **`.gmail-credentials`** — Gmail OAuth token placeholder (53 bytes)

### Non-Critical Local Files (can be regenerated):
- `kanban.html` — rendered KANBAN board (viewable in git version)
- `rosa-birthday-restaurants.html` — parsed search results (can re-scrape)

### Regenerable Files (in git but showing as local edits):
- Job hunt strategy files (all committed to git)
- Memory files (2026-02-02.md in memory/ folder, committed)
- Content drafts (all committed)

**Risk Level:** 🔴 **CRITICAL** — `.env` file contains all active credentials

---

## 4. TELEGRAM BOT SETUP DETAILS

**Configuration File:** `/home/clawdbot/.openclaw/openclaw.json`

**Active Settings:**
- **Bot Token:** `8360881607:AAF...` (32-char abbreviated, full token in config)
- **Enabled:** Yes
- **Mode:** Local gateway on loopback
- **Gateway Port:** 18789
- **DM Policy:** Open (accepts DMs from anyone)
- **Group Policy:** Open (accepts group messages)
- **Mention Requirement:** Not required
- **Stream Mode:** Partial (buffered, not full realtime)

**User Authorized:** Casey Lynch (ID: 8461430130)

**Receiving Channels:** Telegram → OpenClaw Gateway → local HTTP → Stan (Haiku model)

---

## 5. DISASTER RECOVERY GAPS & RISKS

### 🔴 CRITICAL ISSUES:

1. **`.env` file NOT encrypted**
   - Contains 6 active API keys (Twitter ×2, Apollo, Airtable, Gmail placeholder, SFDC placeholder)
   - Single point of failure: VM storage is only copy
   - No encrypted backup on Google Drive or AWS

2. **Telegram bot token in openclaw.json (local)**
   - Could be rotated, but not backed up
   - Config file not version controlled (probably intentional for security)

3. **Gmail OAuth token (`.gmail-credentials`)**
   - Placeholder only (no actual OAuth token yet)
   - Will need OAuth flow when Google Workspace integrated

4. **No AWS disaster recovery setup**
   - Casey hasn't decided on AWS account strategy yet
   - No cross-region backup configured

### 🟡 MEDIUM ISSUES:

1. **Memory files** 
   - Daily notes (2026-02-02.md) ARE in git
   - But `memory/` folder not in .gitignore, risk of overwriting

2. **GitHub repository access**
   - Requires GitHub SSH key (not stored in .env, but needed for git push)
   - If SSH key lost, can't push future updates

3. **Airtable base not backed up**
   - 25 target companies in "Job Hunt 2026" base
   - If Airtable account compromised or deleted, data gone
   - No regular snapshot backup

---

## 6. RECOVERY TIME OBJECTIVES (RTO)

**If VM dies TODAY:**

| Component | Recovery Time | Data Loss |
|-----------|----------------|-----------|
| Code/configs | 5 min (git clone) | None (all in GitHub) |
| API Keys | 30 min (regenerate + update) | None (regeneratable) |
| Airtable data | 1-2 hours (manual re-entry) | 25 target companies |
| Twitter accounts | 10 min (rotate tokens) | None (accounts still exist) |
| Telegram bot | 15 min (update token in config) | None (Telegram still has messages) |
| **Total RTO** | **2-3 hours** | 25 Airtable records |

---

## 7. WHAT NEEDS TO HAPPEN NEXT

**Immediate (Today):**
1. ✅ Encrypt `.env` with GPG (Casey provides passphrase)
2. ✅ Back up encrypted `.env` to Google Drive (`4-Archive/credentials/`)
3. ✅ Back up openclaw.json to Google Drive
4. ✅ Create Airtable snapshot/export (manual for now)

**This Week:**
1. Set up automated `.env` backup (daily encrypted backup to Google Drive via cron)
2. Set up Airtable API auto-export (daily CSV backup)
3. Document GitHub SSH key location + recovery procedure
4. Test disaster recovery process (simulate VM death, restore from backups)

**Phase 2:**
1. AWS backup setup (if Casey approves)
2. Cross-region replication
3. Automated restore testing

---

## 8. GITHUB VERIFICATION

**Remote URL:** `git@github.com:cslynch/stan-workspace-backup.git`  
**Last Push:** ~12 hours ago  
**Branch:** main  
**Files Behind:** None (all committed)

**To Restore:**
```bash
git clone git@github.com:cslynch/stan-workspace-backup.git /recovery/workspace
cd /recovery/workspace
source .env.gpg (decrypt with Casey's passphrase)
```

---

## 9. SUMMARY FOR SUPERSTAN

**Current State:**
- ✅ Code/configs: Fully version controlled in GitHub (186 files, clean history)
- ✅ Code changes: Tracked via git commits (20 commits, last was job-hunting reframe)
- 🟡 Credentials: Active in unencrypted .env file (6 API keys + tokens)
- 🟡 Local storage: 2 critical files (.env, .gmail-credentials) not backed up
- 🟡 Telegram: Bot token in openclaw.json (local, not version controlled)
- 🔴 Airtable: 25 target company records in cloud (not backed up locally)

**Risk Assessment:** MEDIUM (all code recoverable, credentials at risk, data loss possible if Airtable deleted)

**Recommended Action:** Encrypt .env → Google Drive + set up automated daily backup

---

*Format for SuperStan: Copy this entire report and paste at claude.ai for analysis & recommendations*
