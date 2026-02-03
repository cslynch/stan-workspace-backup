# Airtable Setup Plan
**Status:** Ready to execute (Week 2: Feb 12-13)  
**Purpose:** CRM for Casey's operations + Twitter leads + pipeline tracking

---

## Workspace Structure

### Base 1: Twitter Operations
Tables:
1. **Leads**
   - Fields: Name, Email, Tweet Context, Interest Level (1-5), Last Contact, Follow-up Date
   - Linked to: Tasks, Conversations
   
2. **Conversations**
   - Fields: Timestamp, From Account (@itsolz or @stanleybodewell), Message, Response, Notes
   - Linked to: Leads
   
3. **Tasks**
   - Fields: Task, Due Date, Priority, Status (Open/Done), Owner (Casey or Stan), Notes
   - Linked to: Calendar events (via Zapier)

4. **Metrics** (Daily)
   - Fields: Date, @itsolz Followers, @itsolz Engagement, @stanleybodewell Followers, Engagement, DMs Received, DMs Replied, New Leads
   - Automated: Stan updates daily

---

## Setup Steps

1. **Create Airtable Account**
   - Free tier supports all we need
   - Set Casey as owner
   - Generate API key for Stan integration

2. **Create Base: "Twitter & Operations"**
   - Workspace: "Casey's Operations"

3. **Build Tables** (empty schemas)
   - **Leads** table
   - **Conversations** table
   - **Tasks** table
   - **Metrics** table

4. **Configure API Access**
   - Generate personal access token (PAT)
   - Store in .env as `AIRTABLE_TOKEN`
   - Permissions: Read + Write on all tables

5. **Build Connectors**
   - Twitter mention → Auto-create Lead in Airtable
   - Task → Auto-create Calendar event (Week 2, via Zapier)
   - Daily metrics → Auto-update Metrics table

---

## What Stan Can Do (Without Casey)

- [ ] Create Airtable account
- [ ] Create Base structure (tables, field schemas)
- [ ] Set up API access
- [ ] Document webhook endpoints for auto-syncing
- [ ] Test with mock data

## What Needs Casey

- [ ] Airtable account email (who owns it?)
- [ ] Confirm table structure (does this match Casey's workflow?)
- [ ] Approve API key generation

---

**Estimated setup time:** 2 hours (Week 2, Feb 12)  
**Cost:** Free tier, no charges

---

## Future Expansions

- Pipeline tracking (if FleetBrain/RapidKey customers)
- Revenue metrics (if Stripe integrated)
- Calendar blocks (linked to Airtable tasks)
- Automation triggers (Zapier → more complex workflows)
