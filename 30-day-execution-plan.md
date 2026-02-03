# 30-Day Execution Playbook
**Status:** In Progress  
**Start Date:** Feb 3, 2026  
**End Date:** Mar 2, 2026

---

## IMMEDIATE (Feb 3-4)

### Feb 3
- [ ] Casey reviews twitter-launch-package.md
- [ ] Casey voice-checks content, selects options
- [ ] Casey approves bios, singles, threads, reply frameworks
- [ ] Lock posting schedule for both accounts

### Feb 4
- [ ] Content finalized by EOD
- [ ] Posting calendar locked
- [ ] Ready for API credential handoff

**Prompt Point:** ✅ Content approval ready

---

## LAUNCH SEQUENCE (Feb 5-7)

### Wed Feb 5
- [ ] Receive @itsolz API credentials from Casey
- [ ] Configure API access to .env
- [ ] Test posting functionality (@itsolz)
- [ ] Test reply/mention monitoring
- [ ] Verify email monitoring active (see: Email Safety Protocol below)
- [ ] Report: "Launch ready" or blockers

### Thu Feb 6
- [ ] Final verification tests both accounts
- [ ] Confirm posting schedule loaded and ready
- [ ] Test DM access (@itsolz)
- [ ] EOD: Report go/no-go status

### Fri Feb 7 - LAUNCH
- [ ] @stanleybodewell: 8am daily post (automated)
- [ ] @itsolz: First research engagement (afternoon)
- [ ] Monitor all day for issues
- [ ] Evening: Summary to Casey (metrics, any blockers)

**Prompt Point:** ✅ Launch day report

---

## WEEK 1 OPERATIONS (Feb 7-9)

### Fri-Sun (Feb 7-9)
- [ ] Execute scheduled posts (both accounts)
- [ ] Monitor mentions and DMs
- [ ] Reply engagement (Dream 100 accounts)
- [ ] Track metrics: followers, engagement, DM quality
- [ ] Sun: Compile Week 1 report

**Metrics to Report:**
- @itsolz: Follower count, avg engagement/tweet, reply threads started, DM volume
- @stanleybodewell: Follower count, avg engagement/tweet, retweets/quote tweets
- Combined: Cost of API usage this week

**Prompt Point:** ✅ Week 1 metrics report

---

## WEEK 2 BUILD (Feb 10-16)

### Mon-Tue (Feb 10-11): Google Calendar Integration
- [ ] Research Gmail/Calendar API safe access patterns
- [ ] Set up OAuth (not password auth) for minimal permissions
- [ ] Build: Calendar read → Extract Casey's schedule → Prioritize tasks
- [ ] Test with read-only access

### Wed-Thu (Feb 12-13): CRM Integration (Airtable)
- [ ] Set up Airtable workspace
- [ ] Create schema: Leads, Tasks, Twitter Metrics
- [ ] Build API connector
- [ ] Test: Lead data → Airtable → Casey alert

### Fri-Sun (Feb 14-16): Full Workflow Test
- [ ] Twitter mention → Parse → Lead score → Airtable → Calendar block → Casey alert
- [ ] Document workflow end-to-end
- [ ] Sun: Report integration status + issues

**Prompt Point:** ✅ Integration complete or blockers

---

## WEEK 3 VOICE + STRIPE (Feb 17-23)

### Mon-Tue (Feb 17-18): TTS Implementation
- [ ] Configure TTS (Text-to-Speech) for all channels
- [ ] Test: Stan reads daily summary → audio file → send to Telegram/Discord/Slack
- [ ] Record sample voice message for Casey approval

### Wed-Thu (Feb 19-20): Stripe Monitoring
- [ ] Set up Stripe account (if FleetBrain has paying customers by then)
- [ ] Monitor: Charges, failed payments, usage spikes
- [ ] Alert Casey if: >$10/day in charges, any payment failures

### Fri-Sun (Feb 21-23): Cost Optimization
- [ ] Audit all API usage (Twitter, Gmail, Calendar, Airtable, Stripe)
- [ ] Identify expensive operations, optimize
- [ ] Report: Total cost this week, projections

**Prompt Point:** ✅ TTS verified, cost report

---

## WEEK 4 PREP (Feb 24-Mar 2)

### Mon-Wed (Feb 24-26): Discord Community Setup
- [ ] Create Discord server
- [ ] Channels: announcements, automation-demos, ask-stan, general
- [ ] Connect Stan as bot
- [ ] Set up roles: Admin (Casey), Moderator, Community
- [ ] Test voice channel (if TTS+Discord audio works well)

### Thu-Fri (Feb 27-28): Documentation + Controls
- [ ] Create admin playbook for Jeff (if needed)
- [ ] Document all integrations (which services connect where)
- [ ] Create controls: Casey's emergency commands, pause automations, reset
- [ ] Document cost controls: spending limits, alerts, audit logs

### Weekend (Mar 1-2): Month Review
- [ ] Comprehensive metrics review with Casey
- [ ] What worked, what needs adjustment
- [ ] Plan Month 2 (next 30 days)
- [ ] Report: Total month costs, ROI, efficiency

**Prompt Point:** ✅ Month 1 complete, Month 2 plan

---

## COORDINATION RULES (Locked)

### Priority Hierarchy
1. **Casey urgent** (stops everything)
2. **Customer-facing** (FleetBrain operations)
3. **Scheduled posts** (Twitter daily content)
4. **Research** (background work)
5. **Analytics** (reporting, metrics)

### Cost Management
- Alert Casey BEFORE any operation costs >$5
- Daily cost tracking (no surprises)
- Weekly cost report (every Sunday)
- Escalate if monthly trending >$200

### Reporting Schedule
- Daily: During launch week (Feb 7-9)
- Weekly: Every Sunday (5pm CST)
- Monthly: Every 30 days

### Task Queue Discipline
- Checkpoint every 30 minutes
- Never run operations >30min without reporting status
- Escalate immediately:
  - Cost spike (>$1 per hour)
  - System failure (any API down >5min)
  - Priority conflict (two urgent tasks)

### Email Safety Protocol (CRITICAL)
**Problem:** Gmail shut down Stan's previous account due to bot detection  
**Risk:** Casey loses access to his own Gmail (locked out for suspicious activity)

**Implementation (Conservative):**
1. **OAuth only** — Never use password authentication
2. **Minimal permissions** — Read-only on specific labels only
3. **Infrequent checks** — Max 1 check per hour (not real-time)
4. **Monitored labels only** — Only read labels Casey explicitly allows
5. **User-Agent transparency** — Identify as OpenClaw/Stan (not hidden)
6. **Alert on flagging** — If Gmail shows security warning, immediately stop and alert Casey
7. **No forwarding** — Never forward Casey's emails anywhere
8. **No modifications** — Never mark as read, delete, or change labels

**Before activating:**
- [ ] Casey explicitly authorizes email access
- [ ] Casey chooses which labels to monitor (e.g., "Urgent", "From Rosa", "From Jeff")
- [ ] Establish kill-switch: If Gmail flags account, immediately disable Stan's access
- [ ] Document: Email-related permissions and what Stan can/cannot do

---

## METRICS TO TRACK (Locked)

### Twitter Metrics
- Followers (both accounts)
- Engagement rate (likes + retweets per tweet)
- DM volume + quality
- DM→Lead conversion (if applicable)
- Cost per 1K impressions

### Operations Metrics
- Task completion rate (% of planned tasks executed)
- Response time (avg time from trigger to action)
- Cost per task
- System uptime %
- API success rate %

### Financial Metrics
- Total monthly API costs (Twitter, Gmail, Calendar, Airtable, Stripe, TTS, Discord)
- Cost per task
- Cost per lead (if applicable)
- Monthly trend (tracking to budget)

---

## DECISIONS MADE

### CRM Choice: Airtable
**Reason:** Simpler than HubSpot, API-first, flexible schema, can grow with complexity  
**Setup:** Week 2 (Feb 12-13)

### Voice Chat: TTS Only (Option A)
**Reason:** Least complexity, works across all channels, no real-time conversation (yet)  
**Implementation:** Week 3 (Feb 17-18)  
**How it works:** Stan reads summaries → TTS audio → sends via Telegram/Discord/Slack/Email

### Community First: Discord
**Reason:** Web + mobile, voice channels, good for community, easy integration  
**Setup:** Week 4 (Feb 24-26)

### Email Access: Highly Conservative
**Risk:** Gmail shutdown due to bot detection  
**Strategy:** OAuth + minimal permissions + infrequent checks + kill-switch  
**Status:** Waiting for Casey's explicit label approval before implementing

---

## NEXT STEPS

### Waiting on Casey:
1. [ ] Twitter content approval (by EOD Feb 4)
2. [ ] @itsolz API credentials (by Feb 5)
3. [ ] Email label whitelist (which labels can Stan monitor?)
4. [ ] Email access go-ahead (explicit permission to implement)

### Ready to Execute (no Casey input needed):
1. [ ] Airtable setup (anytime)
2. [ ] TTS implementation (Week 3)
3. [ ] Discord setup (Week 4)
4. [ ] Calendar integration (Week 2, Gmail-safe version)

---

**Status:** Ready for launch sequence Feb 5.  
**Awaiting:** Content approval + @itsolz credentials + email permissions.
