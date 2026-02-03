# Phase 1 Execution Checklist - Job Search Infrastructure

**Timeline:** Week 1 (Starting Today - Feb 3)
**Goal:** 20 target companies researched + 15+ LinkedIn connections + 5+ application drafts

---

## Setup (Do Now)

### Skills Status
- ✅ airtable (installed)
- ✅ apollo (installed)
- ✅ linkedin (installed)
- ✅ google-workspace (installed)

### Airtable Setup
- [ ] Create Airtable base called "Job Hunt 2026"
- [ ] Create table: "Target Companies" with fields:
  - Company name (text)
  - Role title (text)
  - Job posting URL (URL)
  - Funding stage (single select: Seed / Series A / Series B / Series C)
  - Tech stack (text)
  - Using Salesforce? (checkbox)
  - Hiring manager name (text)
  - Hiring manager email (text)
  - Hiring manager LinkedIn URL (URL)
  - Connection status (single select: Not connected / Requested / Connected / Chatted)
  - Application status (single select: Interested / Applied / Pending / Interviewing / Rejected / Offer)
  - Application date (date)
  - Last contact (date)
  - Next follow-up (date)
  - Interview date(s) (date)
  - Salary range (text)
  - Recent news (text)
  - Personalized angle (text)
  - Notes (text)

### API Keys Needed from Casey
- [ ] **Apollo API key** (from apollo.io → Account → API Keys)
- [ ] **Google OAuth credentials** (if not already set up from Phase 2)
  - For Gmail draft composition

### Salesforce Setup (Prep for Phase 2)
- [ ] Casey sign up for [Salesforce Developer Edition](https://developer.salesforce.com/signup) (FREE)
- [ ] Create Salesforce OAuth app for MCP integration

---

## Workflow 1: Find 20 Target Companies

### Search Criteria
- B2B SaaS
- Hiring for: AE or Senior AE role
- Salary: $100k+ OTE
- Funding: Series A, B, or C
- Location: Texas or Remote

### Sources to Check (Manual)
- LinkedIn Jobs (filtered by above criteria)
- Angel List (funded companies only)
- Glassdoor (B2B SaaS, AE roles)
- PitchBook (funded companies)
- Company websites (careers pages)

### First Batch (Start Today)
Pick 20 companies and create Airtable entries (even if no open role yet - research ahead):
- [ ] Company 1
- [ ] Company 2
- [ ] ... (20 total)

---

## Workflow 2: Apollo Company Research

**For each of the 20 companies:**

### Command Template
```bash
# Research company
apollo-enrich-website.sh "[company domain]"

# Search for people at company
apollo-people-search.sh "[company name] [title]" 1 10
```

### Fill in Airtable Fields
From Apollo research:
- Funding stage
- Tech stack (check SFDC usage)
- Recent funding announcements
- Key hires (especially sales leaders)
- Company size, location, revenue signals

### Find Hiring Manager
- If job posting exists: hiring manager email/name from posting
- If not: Use Apollo to find VP Sales, Sales Director, or Recruiting Manager
- Populate: Hiring manager name + email + LinkedIn

---

## Workflow 3: LinkedIn Networking

**For each of the 20 hiring managers:**

### LinkedIn Actions
1. [ ] Search for hiring manager on LinkedIn
2. [ ] Add personalized connection request:
   ```
   Hi [name], I'm exploring roles on your team at [company]. 
   I've got [X years] of B2B sales experience and I'm impressed with [specific company achievement/product/funding]. 
   Would love to connect and learn more about your sales org.
   ```
3. [ ] Note connection status in Airtable
4. [ ] Once connected: Send InMail or 1st message

### InMail Template (For Week 1 or early Week 2)
```
Hi [name],

I'm exploring AE opportunities and [company name] caught my attention because [personalized reason: funding, product, team growth, etc.].

I've got [X years] B2B SaaS experience, most recently [brief context on last role/wins].

Is your team hiring? I'd love to explore whether there's a fit.

Best,
Casey
```

---

## Workflow 4: Email Outreach Drafts

**Create personalized email drafts for 5-10 hiring managers.**

### Gmail Draft Template
```
Subject: AE opportunity at [company]?

Hi [name],

I'm exploring next opportunities and [company name] stands out because [specific reason]:
- [Recent funding/product launch/market expansion]
- [Your sales chops match their ICP]
- [Team growth signal]

I've got [X years] B2B SaaS experience in [relevant vertical/motion], most recently [brief win/stat]:
- Increased quota attainment from 85% to 112%
- Built [sales ops achievement]
- [Number] customers closed in [timeframe]

Would be great to connect and explore whether there's a fit on your team.

Best,
Casey
```

**Action:** Draft 5+ emails, send 2-3 this week, rest by end of Phase 1.

---

## Workflow 5: Application Submissions

**For posted roles with hiring manager already researched:**

### Checklist Per Application
1. [ ] Customize resume to highlight:
   - Salesforce experience (or "SFDC training in progress")
   - Sales process improvements
   - Revenue/quota results
   - Any tech stack familiarity
2. [ ] Customize cover letter to:
   - Mention company-specific reason (funding, product, team)
   - Highlight 1-2 relevant wins
   - Show Salesforce fluency (if applicable)
3. [ ] Submit via LinkedIn or company website
4. [ ] Log in Airtable with application date
5. [ ] Set follow-up reminder: 1 week (if no response)

---

## Daily Standup (Week 1)

**Each day, report to Casey:**
```
Stan, status on job search:
- New companies researched: [#]
- New LinkedIn connections requested: [#]
- Email drafts completed: [#]
- Applications submitted: [#]
- Interviews scheduled: [#]

Top 3 opportunities this week:
1. [Company + hiring manager + reason it's a fit]
2. [Company + hiring manager + reason it's a fit]
3. [Company + hiring manager + reason it's a fit]

Next actions:
- [ ] Research [company X]
- [ ] Send email to [person Y]
- [ ] Follow up with [person Z]
```

---

## Success Metrics (Week 1)

- [ ] 20 target companies in Airtable with full research
- [ ] 15+ LinkedIn connection requests sent
- [ ] 5+ personalized emails drafted (in Gmail)
- [ ] 3+ applications submitted
- [ ] 1+ interviews scheduled

---

## Notes

- **Don't spam:** Quality > quantity. Each outreach should be personalized with Apollo research + company context.
- **LinkedIn first:** Warm outreach (through connection) > cold email
- **Follow-up:** Set reminders for 1-week follow-ups on all outreach
- **Airtable = living doc:** Update daily with progress, status changes, new contacts
- **Phase 2 prep:** Start thinking about Salesforce Dev Edition sign-up (free) — we'll set it up Week 2

---

## Blockers / Needs from Casey

- [ ] Apollo API key
- [ ] Confirm Airtable access + table creation OK
- [ ] LinkedIn account + credentials for automation (if using bird)
- [ ] 20 initial company targets (or permission to research + propose)

**Ready to execute. Waiting on:** Apollo API key + confirmation on above. 🧭
