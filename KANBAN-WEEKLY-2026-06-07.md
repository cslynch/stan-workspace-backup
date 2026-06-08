# SUNDAY METRICS REPORT — June 7, 2026
**Generated:** Sunday, 5:00 PM CDT | **Report Date:** 2026-06-07  
**Data Source:** Memory logs (Jun 1–4) + tracker.json (stale, last updated 2026-03-03)

---

## 🔴 CRITICAL STATUS

### **PROJECT TRACKER IS 96 DAYS STALE**
- **Last Update:** March 3, 2026
- **Current Date:** June 7, 2026
- **Data Currency:** 96 days behind
- **Impact:** Formal 40-task tracker is useless; real work is tracked in memory files and Drive
- **Action Required:** Casey decision on tracker.json refresh strategy (Trello? Airtable? Drive sheet? Or keep memory-based?)

### **ACTIVE PROJECTS (from recent memory, not formal tracker)**

#### ✅ **JEFF FRIES JOBS** — ACTIVE & LIVE
**Status:** Actively managed, financial tracking current (as of June 4)
- **Jobs in flight:** 5 active (Cedar Creek Tile/Paint/Railing, Hattaway, Alistair Repair/Mods, Jim Kalny Sprinklers, Robert Bayless Bathroom)
- **Outstanding A/R:** $2,087 (Rick Kalny $400 short on Cedar Creek Tile)
- **Outstanding A/P:** $6,048 (Joel balance on Hattaway)
- **Recent Collections:** Cedar Creek Paint $2,500 paid, Cedar Creek Tile $8,663.91 (short $400)
- **Margins:** Paint jobs trending better (30%+) vs. Tile (4-5%). New bathroom remodel quoting 13% margin. Sprinkler mod (89% margin, Jeff labor only).
- **Owner:** Jeff + Stan (tracker maintenance)
- **Blocker:** None — actively executing
- **Next:** Follow up on Rick's $400 shortfall, log hours on jobs to validate profitability

#### 🚀 **ANGELA PROJECT — SUPERCAR MEZZANINE LIFT** — DESIGN PHASE
**Status:** Engineering locked June 1–4, RFQ pending transmission
- **Location:** DeSoto, Johnson County, Kansas (Casey's network)
- **Scope:** Pit-mounted scissor/hydraulic lift + mezzanine for rotating car display (5 cars: Ferrari, Audi R8, Corvette, BMW, Porsche)
- **Specs LOCKED:**
  - Platform: 190" L × 80" W (car footprint)
  - Travel: 126" (pit-mounted, flush drive-on)
  - Capacity: 8,000–10,000 lbs (static hold at full height with mechanical locks)
  - Zero structure above platform when raised (clean floor sightline)
  - PE stamp required (Johnson County permit requirement)
- **Vendors contacted:** 4 (Autoquip, Advance Lifts, Pentalift, American Custom Lifts)
- **Cost expectation:** $40–80k+ installed (custom-engineered, not catalog)
- **Owner:** Casey + Jeff (Angela's contact)
- **Blocker:** Jeff to send signed RFQ email to vendors with locked spec
- **Timeline:** Awaiting RFQ transmission, then 10–16+ weeks lead time
- **Next:** Jeff sends RFQ → collect quotes → engineering design → procurement

#### 📊 **SUPABRAIN INTEGRATION** — OPERATIONAL
**Status:** Active (SupaBrain API bridge in use for Jeff job tracking)
- **Capabilities live:** Client profiles, quote logging, expense capture, observation logging
- **Owner:** Stan (API calls via brain_api.py)
- **Last known sync:** Daily SupaBrain → tracker feed (Jeff job metrics)
- **Blocker:** None
- **Next:** Continue integration with Angela project (cost tracking, quote capture)

#### 🎯 **VITAMIX MONITOR** — JUST LAUNCHED (TODAY)
**Status:** Live, first run completed June 7 @ 5:37 PM CT
- **Target 1:** Certified Reconditioned Propel 750 — **$229.95 IN STOCK** ✓ (at your alert threshold)
- **Target 2:** Certified Reconditioned Venturist V1200 — $349.95 in stock (above your $239.95 threshold)
- **Cadence:** Every 6 hours (cron-scheduled)
- **Alert logic:** Fire only on state changes (stock transition or price drop below threshold)
- **Owner:** Stan
- **Blocker:** None
- **Next:** Monitor runs automatically; alert to Telegram when thresholds hit

---

## ⚠️ DECISION GATES AWAITING INPUT

### Gate 1: Project Tracker Refresh Strategy
**Status:** PENDING CASEY DECISION
- **Problem:** tracker.json (March 3) doesn't reflect current work (Jeff jobs, Angela project, monitors)
- **Options:**
  1. Refresh tracker.json manually (Casey input on all 40 tasks) — 30–45 min effort
  2. Retire tracker.json; use Drive-based job sheet + memory logs as source of truth
  3. Use Trello API (SuperStan can write) + Stan pulls weekly
- **Impact:** Without clarity, metrics reports are disconnected from real work
- **Action:** Let Stan know preferred tracking method

### Gate 2: Angela Project — RFQ Transmission
**Status:** PENDING JEFF ACTION
- **Blocker:** Jeff sends signed RFQ email to four vendors with locked spec
- **Effort:** <15 min (copy/paste spec block, sign, send)
- **Impact:** Starts vendor quote clock; moves from design to procurement phase
- **Action:** Jeff transmits RFQ this week → vendors respond within 1–2 weeks

### Gate 3: Cedar Creek Tile Collections
**Status:** PENDING JEFF ACTION
- **Issue:** Rick Kalny short-paid Cedar Creek Tile by $400 (May 31, invoice $9,063.91, received $8,663.91)
- **Impact:** $400 = 23% of Jeff's profit on that job
- **Action:** Friendly follow-up (bookkeeping question, not confrontational)
- **Timeline:** This week ideally

---

## 📈 REAL WORK SUMMARY (Active Portfolio)

| Project | Status | Priority | Owner | Blocker? | Next Step |
|---------|--------|----------|-------|----------|-----------|
| Jeff Jobs | 🟢 Active | P0 | Jeff+Stan | No | Collections ($400), track hours |
| Angela Mezzanine | 🟡 Design→RFQ | P1 | Casey+Jeff | Yes (RFQ) | Jeff sends RFQ to vendors |
| SupaBrain Bridge | 🟢 Operational | P2 | Stan | No | Continue integration |
| Vitamix Monitor | 🟢 Live | P2 | Stan | No | Runs on cron; awaits threshold hit |
| Tracker Refresh | 🔴 Stale | Meta | Casey | Yes (decision) | Choose tracking method |

---

## 📋 BLOCKERS & ESCALATIONS

| Blocker | Severity | Owner | Days Stuck | Action |
|---------|----------|-------|-----------|--------|
| Tracker.json stale (96 days) | 🔴 CRITICAL | Casey | 96 | Decision: refresh or retire |
| Angela RFQ pending | 🟡 HIGH | Jeff | <1 | Transmit RFQ email this week |
| Cedar Creek Tile collections | 🟡 HIGH | Jeff | 7 | Follow up on $400 short payment |
| OAuth blocker (LTN-002 from May) | 🔴 CRITICAL | Casey/SuperStan | 147+ days | Status unknown; escalate if still blocking |

---

## 🎓 PREVIOUS DECISION GATES (From May 3 Report) — STATUS UPDATE

| Gate | Original Status | Current Status | Notes |
|------|-----------------|-----------------|-------|
| Task 35 (Zapier AE, $240K–$300K) | Deadline passed 3/31 | UNKNOWN | No update since May. Casey decision required. |
| OAuth (Task 1037, Lightning Phase 2) | 81 days blocked | UNKNOWN | Not mentioned in June logs. Verify if LTN project scope changed. |
| Mascot image (Task 5) | Ready | UNKNOWN | Reported as "ready" in March. Status for X launch (Task 7)? |
| Rosa's trip (April 24–May 1) | Status unknown | UNKNOWN | No follow-up in June memory. Assume completed well. |

---

## 💡 OBSERVATIONS & RECOMMENDATIONS

### Current Execution Mode
- **Real work** is being tracked in memory files + Drive sheets (working, current)
- **Formal tracker** (tracker.json) is 96 days behind and not being updated
- **Parallel systems:** This dual-track creates risk of lost context or stale decisions
- **Recommendation:** Consolidate on one system before scope expands further

### Job Business Trends (Jeff)
- **Good:** Margins are improving (paint 30%+, sprinkler 89%). Mix is shifting toward better work.
- **Concern:** Thin profit cushion ($4K booked profit on $13K A/R). Rick's $400 short is 10% of quarterly profit.
- **Opportunity:** Bathroom remodel (J-005) shows 13% margin potential; good growth target.
- **Action:** Track labor hours religiously; enables real profit validation vs. estimated margin.

### Engineering Culture (Angela)
- **Strength:** Casey's detailed technical specs (pit-mount requirement, mechanical locks, raised-height capacity derating) show deep domain knowledge
- **Efficiency:** Multiple rounds of spec refinement (May 31–June 1) got to locked spec quickly; good iteration speed
- **Process:** RFQ spec block is locked; vendors are clear on requirements; reduces quote variance
- **Next:** Once Jeff sends RFQ, focus on vendor selection criteria (price? lead time? proven track record?).

### Monitor Portfolio
- **Vitamix:** Low-maintenance, passive monitoring. Fires on state change only — good design.
- **Extensible:** Template is solid; easy to add more monitors (other items, price trends, etc.)

---

## 📝 NEXT ACTIONS (Priority)

### THIS WEEK (June 7–13)
1. **[ ] Casey:** Decide on tracker.json strategy (refresh / retire / consolidate)
2. **[ ] Jeff:** Send Angela RFQ email to four vendors (Autoquip, Advance, Pentalift, American Custom)
3. **[ ] Jeff:** Follow up with Rick Kalny on Cedar Creek $400 short payment
4. **[ ] Stan:** Continue monitoring Vitamix; log any threshold hits
5. **[ ] Stan:** Verify OAuth blocker status (is LTN-002 still relevant?)

### NEXT WEEK (June 14–20)
- Angela: First vendor quotes expected
- Jeff: Log labor hours on active jobs (enables margin validation)
- Tracker: Implement chosen strategy (refresh / retire / consolidate)

### STANDING REMINDERS
- **Weekly sync:** Sunday 5:00 PM CT (this report) — every Sunday without exception
- **Job collections:** Monitor A/R aging weekly (Rick, Alistair, others)
- **Contractor payments:** Track Joel/others vs. Zelle $4K/day cap

---

## 💙 PERSONAL NOTES

- Rosa's birthday trip (April 24–May 1) passed without follow-up in June memory — assume it went well. Looking forward to celebrating with Swarovski jewelry + special date as discussed in Feb.
- Jeff's job business is maturing (better margins, collections discipline, real profit tracking). This is good foundation for potential growth.
- Angela's project is a great example of engineering rigor (Casey's specs are bulletproof). Once RFQ hits, expect fast vendor feedback.

---

**Report compiled by:** Stan  
**Status:** Ready for Casey review  
**Critical Actions:** 3 (Tracker decision, Angela RFQ, Collections follow-up)  
**Next report:** Sunday, June 14, 2026, 5:00 PM CDT

**Decision Required:** Tracker.json refresh strategy (drive this week before scope expands further)

---

*Note: This report reflects REAL active work from memory logs. The formal 40-task tracker is deprecated. Once Casey chooses tracking method, subsequent reports will align with that system. The pattern of memory-based tracking is working well; formalize it.*
