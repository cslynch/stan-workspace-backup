# Automation Schedule
**Created:** Feb 2, 2026 23:17 CST

---

## Weekly Tasks (Automatic)

### Sunday 5pm CST - KANBAN Update + Metrics Report
**Schedule:** Every Sunday 17:00 (5pm) America/Chicago  
**Cron:** `0 17 * * 0`  
**Job ID:** `64adf21a-57e5-4ccf-81cd-a3522dfdf0e8`

**What happens:**
1. Stan compiles metrics from the week
   - Twitter: followers, engagement rates, DM volume
   - Operations: task completion %, costs
   - Infrastructure: uptime, API success rate
2. Updates KANBAN.md with progress
3. Documents any blockers
4. Analyzes decision gates (are we on track?)
5. Commits to GitHub
6. Sends summary to Telegram

**Deliverable:** Weekly metrics report in Telegram (text) + updated KANBAN.md in GitHub

---

## Manual Tasks (As Needed)

### KANBAN Update (On-Demand)
- Trigger: You ask "update kanban" 
- Response: Stan updates immediately, commits, sends status

### Daily Standups (Optional, Week 1+)
- During launch week (Feb 7-9): Daily summary of posts + engagement
- Trigger: You ask "daily standup" or Stan auto-sends at 8pm each day

---

## Future Automations (To Schedule)

### Daily (Once Metrics Stabilize)
- [ ] Morning briefing (5 min executive summary)
- [ ] Evening report (Twitter activity, API spend)

### Weekly (Additional)
- [ ] Cost analysis (spending vs budget)
- [ ] Competitor monitoring alert (if anything major happens)
- [ ] Content performance analysis (what's working)

### Monthly (Mar+)
- [ ] Revenue report (if applicable)
- [ ] Full retrospective (wins, lessons, pivots)

---

## How to Trigger Manual Updates

**KANBAN Update:**
```
"update kanban"
```

**Custom Report:**
```
"give me [report type]" 
(e.g., "give me today's metrics", "cost report", "engagement analysis")
```

**Pause Automation:**
```
"pause weekly updates"
```

**Resume Automation:**
```
"resume weekly updates"
```

---

## Cron Job Details

**Status:** ✅ Active

**Next run:** Sunday Feb 9, 2026 5pm CST

**Command:** Sends system event to Stan's session, triggering metrics compilation + KANBAN update

**Backup:** Job config stored in OpenClaw gateway, also documented here

**If it fails:** Stan will notify you immediately (unusual activity alert)

---

**Monitoring:** Check back on KANBAN.md every Sunday evening to see the update.
