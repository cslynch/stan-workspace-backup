# External Tool Data Classification Protocol

**FleetBrain Framework Document**  
**Created:** Feb 3, 2026  
**Classification:** Internal / Confidential

---

## Overview

This protocol defines what data can be safely stored in third-party platforms (Airtable, Trello, Todoist, Slack, Discord, etc.) versus what must remain in StanBrain (Google Drive) or local storage only.

The core principle: **If it would help a competitor replicate FleetBrain, it stays internal.**

---

## Data Classification Framework

### TIER 1 - NEVER External (Always StanBrain or Local)

These categories contain proprietary or sensitive information that defines FleetBrain's competitive advantage:

**Architecture & IP:**
- FleetBrain system design (dual-layer Stan/SuperStan model)
- The recursive escalation loop (when/how to delegate to SuperStan)
- Operational Rules (1-13, the decision framework)
- Second Brain Protocol (Drive-first retrieval pattern)
- Prompt engineering techniques or system prompts
- Internal decision gates or trigger logic

**Security & Credentials:**
- API keys, tokens, refresh tokens, OAuth credentials
- Password managers or credential storage
- Email addresses of APIs or services
- SSH keys, private certificates
- Database connection strings

**Client Confidential:**
- Client names (unless in public case studies with approval)
- Client budgets, pricing, or deal terms
- Client strategic plans or revenue figures
- Client proprietary data or industry secrets
- Anything marked "confidential" by client

**Business Sensitive:**
- FleetBrain pricing structure or cost calculations
- Consultant margin details or profit targets
- Deal negotiations or contract terms
- Internal revenue figures
- Churn or customer satisfaction data
- Hiring plans or team information
- Investor communications or cap table

**Methodology:**
- How we calculate ROI for clients
- Our cost-modeling approach
- Interview scripts or questioning techniques
- Competitive intelligence (how we research competitors)
- Sales playbook or closing strategies

---

### TIER 2 - OK for External (With Caveats)

These can go on third-party platforms if the platform is secure, private, and purpose-built:

**Task Management:**
- Task names and descriptions (generic: "Research market" not "Research XYZ confidential client")
- Due dates and status (open, in-progress, done)
- Assignee names
- General priority levels (high/medium/low)
- Subtasks or dependencies

**Calendar & Scheduling:**
- Meeting times (without revealing client names or strategic purpose)
- Deadlines for public projects or launches
- Availability windows
- Time zone conversions for coordination

**Public Content:**
- Tweets, LinkedIn posts, published articles
- Blog drafts (pre-publication)
- Press releases or public announcements
- Case studies (with client approval)
- General industry research or reports

**Contact Management (Vetted Platforms Only):**
- Contact names (first + last)
- Company and title
- Follow-up dates
- Interaction history (generic)
- Communication preference
- Only on platforms with privacy agreements

**General Research:**
- Market size / TAM data (from public sources)
- Competitor feature lists (public information)
- Industry trends or benchmark data
- Technology stacks or vendor comparisons
- Conference schedules or event dates

---

### TIER 3 - Situational (Ask Casey First)

These depend on context, client approval, or platform:

- Customer testimonials or quotes
- Performance metrics (if generic/non-identifying)
- Workflow templates (if not proprietary)
- Training materials or documentation
- Vendor comparisons or RFP responses
- Budget allocation frameworks (if not tied to specific clients)

**Rule:** When in doubt, ask Casey before posting.

---

## Platform Risk Assessment

### GREEN (Lower Risk, More OK)

- **Google Drive** (private, encrypted, under our control) — EVERYTHING OK
- **Microsoft OneDrive** (private, encrypted, under our control) — EVERYTHING OK
- **GitHub Private Repo** (private, access-controlled, versioned) — EVERYTHING except credentials
- **1Password/LastPass** (encrypted credential vault) — CREDENTIALS OK here
- **Local SSD/USB** (not networked, under physical control) — EVERYTHING OK

### YELLOW (Medium Risk, Careful)

- **Airtable** (encrypted in transit, but cloud-hosted, shared access) — TIER 2 only
- **Notion** (encrypted in transit, but cloud-hosted, shared access) — TIER 2 only
- **Trello** (basic encryption, cloud-hosted) — TIER 2 only
- **Todoist** (basic encryption, cloud-hosted) — TIER 2 only
- **Slack** (encrypted in transit, but searchable history) — TIER 2 only
- **Calendly** (public availability info) — Dates + times only

### RED (Higher Risk, Restricted)

- **Discord** (searchable, shared servers, low privacy) — Public content only
- **Telegram** (unless private chat with encryption) — TIER 2 only
- **Spreadsheets shared via email** (unencrypted, forwarded widely) — TIER 2 only
- **Public GitHub repo** (anyone can see) — NOTHING sensitive
- **Figma** (cloud-hosted, potentially shared) — Mockups/design only, no strategy

---

## Decision Tree

**Before uploading/sharing ANY data on an external platform:**

```
1. Is it FleetBrain architecture, system prompts, or operational framework?
   → NO → proceed to question 2
   → YES → STOP. Keep in StanBrain/local only.

2. Does it contain API keys, passwords, or authentication credentials?
   → NO → proceed to question 3
   → YES → STOP. Keep in StanBrain/local only.

3. Is it confidential to a specific client?
   → NO → proceed to question 4
   → YES → Ask client permission first.

4. Does it contain pricing, cost structure, or proprietary methodology?
   → NO → proceed to question 5
   → YES → STOP. Keep in StanBrain/local only.

5. Would this help a competitor understand or replicate FleetBrain?
   → NO → OK to share on platform (verify platform tier above)
   → YES → STOP. Keep in StanBrain/local only.

6. When in doubt → ASK CASEY before posting.
```

---

## Examples

### ❌ NEVER External

- "Dual-layer execution model with escalation to SuperStan for strategy decisions"
- OpenAI API key: sk-proj-xxxxx
- "Acme Corp engaged us at $3k/month on 12-month contract"
- "We generate leads by querying Apollo API with intent signals and score them using a proprietary formula"
- System prompt or instruction text

### ✅ OK External

- Task: "Research market size for B2B SaaS"
- Task: "Prepare presentation for Casey review"
- Tweet: "Just shipped 3 new skills to OpenClaw. Workflow velocity 🚀"
- Contact: "John Smith, VP Sales, Acme Corp, follow up Mar 15"
- Meeting: "Feb 10, 2pm PST - Strategy sync"

### ❓ ASK FIRST

- "Case study: We helped Acme Corp reduce processing time by 40%"
- Competitor feature comparison chart
- Budget allocation template (generic, not tied to client)
- Performance chart showing "X tasks automated, Y hours saved" (if it reveals client)

---

## Enforcement

**For Stan:**
- Before any third-party upload, apply this framework
- When in doubt, default to TIER 1 (keep internal)
- Ask Casey before posting anything TIER 3

**For Casey:**
- Review what Stan uploads to external platforms
- If something seems sensitive, ask Stan to delete and move to StanBrain
- This protocol overrides convenience — default to restrictive

---

## Updates

As new platforms are integrated, add them to this framework. Re-evaluate quarterly.

**Last reviewed:** Feb 3, 2026  
**Next review:** May 3, 2026
