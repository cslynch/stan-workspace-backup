--- Last sync: 2026-02-10 11:50 CST ---
# KANBAN - Project Status
**Last Updated:** 2026-02-10 11:50 CST
**Updated By:** Stan
**Trello Board:** StanOps
**Source of Truth:** Master tracker (SuperStan) → Trello (SuperStan direct write) → KANBAN.md (Stan local cache, daily sync at 1:55 AM)

---

## COMPLETED TODAY (Feb 10)

- [x] Valentine's dinner: full research → 18 Oaks reservation confirmed + calendar event added
- [x] JW Marriott amenities research (spa, lounge, pre-dinner options)
- [x] StanBrain file manifest: 37 files, 7 folders with IDs (migration ready)
- [x] Git remote audit: SSH-based, safe from token swap
- [x] Skills directory audit: no hardcoded email references
- [x] Model behavior correction: stopped fabricating contradictions, trust config as truth
- [x] KANBAN sync infrastructure: cron added (1:55 AM daily), timestamp prepend tested

---

## READY FOR SUPERSTAN (Pull Queue)

- [ ] StanBrain migration manifest (37 files, 7 folders, all IDs documented) — Ready for Phase 1 implementation
- [ ] Calendar event inventory — partial (need full recurrence rules capture for Phase 5.1)
- [ ] Migration runbook doc created in StanBrain/ops/ (ID: 1BLPJqOuNMDZ2RJS1fUY7n6JTibAaLMGT9jtU4SbQ4PA) — needs content population
- [ ] .env.gpg audit — blocked on passphrase (priority: credential security)
- [ ] Real estate property gaps (111 Valley View St): flood zone, septic, HOA, rehab estimates, comps, walkthrough questions
- [ ] Twitter approval package status (awaiting Casey voice/content approval to launch @itsolz + @stanleybodewell)

---

## IN PROGRESS

- [ ] .env.gpg audit (passphrase waiting)
- [ ] Calendar event full inventory with recurrence rules (Phase 3.1 deliverable)
- [ ] Real estate property research (market comps, rehab estimates, cap rate analysis)

---

## THIS WEEK (Trello — 18 cards)

- [ ] Approve twitter content selections (due: 2026-02-04)
- [ ] Buy guitar strings and capo for Ry (due: 2026-02-07)
- [ ] Content launch - Add originals phase (due: 2026-02-07)
- [ ] Content launch - Reply engagement phase (due: 2026-02-05)
- [ ] Draft outreach emails (due: 2026-02-07)
- [ ] Finalize case studies #2 and #3 (12 review questions)
- [ ] Fix DNS/SSL for fleetbrain.ai + stanleybot subdomain
- [ ] Google Drive stale doc cleanup
- [ ] Install browser skills (playwright/agent-browser)
- [ ] Push proactive behavior correction (Rosa pattern)
- [ ] Regenerate 7 StanBrain research files
- [ ] Research hiring managers (Apollo + LinkedIn) (due: 2026-02-07)
- [ ] Set up recurring: Monthly AI tool landscape scout
- [ ] Submit applications (due: 2026-02-08)
- [ ] Update LinkedIn profile (sales positioning)
- [ ] Valentine's Day planning (due: 2026-02-12)
- [ ] Website content audit vs v2 spec
- [ ] Week 1 metrics report (due: 2026-02-28)
- [ ] #11 Email forwarding / Send As for casey@fleetbrain.ai → cslynch@gmail.com — In progress
- [ ] #54 Cancel LastPass Premium (due: before 2026-03-24) — Parked, migration complete
- [ ] #58 Activate jake@fleetbrain.ai (password, 2FA, Bitwarden) — After casey@ and stan@ fully settled
- [ ] #59 Phase B: Stan identity migration — OAuth swap from cslynch913 to stan@fleetbrain.ai, StanBrain transfer, calendar migration, Trello rotation, MEMORY.md updates. Requires downtime window.
- [ ] #62 Credential rotation — GitHub PAT and Trello API key/token exposed in chats. Rotate both.

---

## IN PROGRESS (3 cards)

- [ ] Content approval workflow
- [ ] Twitter infrastructure testing
- [ ] #57 Email forwarding / Send As for casey@fleetbrain.ai → cslynch@gmail.com — Parked, will resume

---

## BACKLOG (8 cards)

- [ ] Disaster Recovery - Decide AWS strategy
- [ ] Disaster Recovery - Decide Drive backup cadence
- [ ] Disaster Recovery - Decide GPG passphrase
- [ ] Email monitoring - Define label whitelist
- [ ] Finish Jake bootstrap (OpenClaw on Lightning)
- [ ] Fix email OAuth scoping (cslynch@ = compose only)
- [ ] Google Workspace open items (DKIM, DMARC, agent accounts)
- [ ] Jason Rawlings demo (two-node)

---

## DONE (37 cards - showing most recent)

- [x] ✅ #51 Bitwarden org architecture (Feb 9) — FleetBrain org created, FleetBrain-Ops + Recovery collections
- [x] ✅ #52 LastPass → Bitwarden migration (Feb 9) — 484 items imported
- [x] ✅ #53 LastPass disabled, Bitwarden sole PM (Feb 9) — Windows + Android
- [x] ✅ #55 Activate casey@fleetbrain.ai (Feb 9) — Password set, 2FA enabled, saved in Bitwarden
- [x] ✅ #56 Activate stan@fleetbrain.ai (Feb 9) — Password set, 2FA enabled, saved in Bitwarden
- [x] ✅ #60 Chrome connector operational in Claude Desktop (Feb 9) — MCP bridge working
- [x] ✅ #61 GitHub MCP connected in Claude Desktop (Feb 9)
- [x] ✅ #36 Credential rotation (Trello) (Feb 9) — API creds rotated. Recurring schedule still needed.
- [x] ✅ Research: Claude.ai native Trello/MCP connector
- [x] ✅ Run Snyk mpc-scan against skill configs

---

**SYNC PROTOCOL (Updated Feb 10, 2026):**

Stan and SuperStan both have direct Trello API access and write independently.

When Stan completes work:
1. Update KANBAN.md locally (three sections: COMPLETED TODAY, IN PROGRESS, READY FOR SUPERSTAN)
2. At 1:55 AM daily, cron prepends timestamp and git pushes
3. SuperStan reads git repo at morning strategy review
4. SuperStan can write directly to Trello if needed for sync
5. Stan pulls fresh Trello state periodically to verify alignment

When Stan discovers new tasks:
1. Report to Casey for triage
2. Casey decides priority
3. SuperStan (or Casey) creates the Trello card

**Source of Truth:** Trello is primary. KANBAN.md is Stan's local scratchpad + upstream visibility. Daily git sync at 1:55 AM makes work visible to SuperStan without Casey relay.
