# Working State - Feb 12, 2026

## TASK 1A: GOOGLE CHAT BOT DEPLOYMENT (PRIORITY 1) — ✅ COMPLETE

### Status: PRODUCTION LIVE (Feb 12, 2026 22:01 CST)

**Completed Deliverables:**
- ✅ GCP project: **fleetbrain-stan-prod** (owner: casey@fleetbrain.ai)
- ✅ Google Chat API: Enabled on GCP project
- ✅ Service account: **stan-fleetbrain-bot@fleetbrain-stan-prod.iam.gserviceaccount.com** (chat.bot scope)
- ✅ Service account key: Stored in 0-vault (GPG encrypted), local copy in `/home/clawdbot/.openclaw/credentials/fleetbrain-stan-prod-534550cd7a84.json`
- ✅ Workspace Admin: External Chat messaging enabled by Casey
- ✅ Tailscale Funnel: **https://clawdbot-vm.tail9ce6a9.ts.net/** (persistent, verified working)
- ✅ Webhook endpoint: `/chat/webhook` (receives Google Chat API v2 messages)
- ✅ Production server: **gunicorn** (4 worker processes, systemd service)
- ✅ Systemd service: **chat-webhook.service** (enabled on boot, auto-restart on failure)
- ✅ Agent integration: OpenClaw gateway `/v1/responses` API (HTTP, Bearer auth, full agent brain)
- ✅ End-to-end testing: Message → Agent processing → Chat API reply **CONFIRMED WORKING**

**Architecture:**
```
Google Chat (External User)
    ↓
Tailscale Funnel HTTPS
    ↓ https://clawdbot-vm.tail9ce6a9.ts.net/chat/webhook
    ↓
gunicorn (127.0.0.1:8000, 4 workers)
    ↓
OpenClaw Gateway API: POST /v1/responses
    ↓
Stan's brain (claude-haiku-4-5)
    ↓
Chat API reply: POST /v1/spaces/{id}/messages
    ↓
Response appears in Google Chat space
```

**Files & Config:**
- **Webhook code:** `/home/clawdbot/.openclaw/workspace/chat_webhook.py`
- **Service file:** `/etc/systemd/system/chat-webhook.service`
- **Gunicorn script:** `/home/clawdbot/.openclaw/chat-webhook-gunicorn.sh`
- **Environment:** `/home/clawdbot/.openclaw/.env` (GOOGLE_CHAT_SA_CREDENTIALS + OPENCLAW_GATEWAY_TOKEN)
- **Deployment docs:** `/home/clawdbot/.openclaw/CHAT_WEBHOOK_PRODUCTION.md`
- **Logs:** `journalctl -u chat-webhook -f`

**Service Management:**
```bash
sudo systemctl status chat-webhook      # Check status
sudo systemctl restart chat-webhook     # Restart after code changes
journalctl -u chat-webhook -n 50        # View logs
```

**Status: 🟢 PRODUCTION READY — LIVE CONTACT VECTOR FOR STAN**

---

### Requirement Summary
External users (outside fleetbrain.ai domain) message stan@fleetbrain.ai via Google Chat → receive responses from Stan (OpenClaw agent).

### Deployment Architecture

**Option A: HTTP Endpoint (Recommended for OpenClaw)**
- **How it works:** External user messages → Google Chat API → HTTP POST to OpenClaw endpoint → Stan processes → service account replies via Chat API
- **Setup:** Service account with `chat.bot` scope (no admin approval needed)
- **Response type:** Synchronous (real-time, ideal for agent interactions)
- **Complexity:** Medium (webhook routing + service account management)
- **Latency:** ~500ms-1s per message (API roundtrips)

**Option B: Cloud Pub/Sub (Alternative, async)**
- **How it works:** Google Chat → Pub/Sub topic → OpenClaw consumer → Stan processes → replies via API
- **Advantage:** Async, decoupled, handles burst traffic
- **Disadvantage:** Slower (latency: 1-3s), requires GCP expertise, overkill for warm leads
- **Not recommended:** For interactive agent, HTTP is better

**Option C: Apps Script (Simplest, limited)**
- **How it works:** Google Chat → Apps Script → direct Chat API calls
- **Advantage:** Zero infrastructure, native Google ecosystem
- **Disadvantage:** Can't integrate with OpenClaw easily, slower, execution limits
- **Not recommended:** For this use case (need OpenClaw integration)

**Recommendation: HTTP Endpoint**
- Synchronous responses (agent feels real-time)
- Native OpenClaw integration (expose webhook endpoint)
- Service account for bot identity
- Least friction for external users

---

### Service Account Setup (What Stan Needs to Do)

1. **Create Google Cloud Project** (or use existing)
   - Navigate to: Google Cloud Console → Select/Create project
   - Enable Chat API: APIs & Services → Search "Google Chat API" → Enable
   - Time: 5-10 minutes

2. **Create Service Account**
   - IAM & Admin → Service Accounts → Create service account
   - Name: "stan-fleetbrain-bot" (or similar)
   - Generate JSON key file (save securely)
   - Time: 2-3 minutes

3. **Grant Chat API Scope**
   - Scope needed: `https://www.googleapis.com/auth/chat.bot` (NO admin approval required)
   - This scope allows:
     - Receiving messages from Chat
     - Sending messages as bot
     - Reading user info (limited)
   - Already included in service account default scopes
   - Time: Automatic with creation

4. **Deploy OpenClaw Endpoint**
   - Create webhook endpoint in OpenClaw that accepts Chat API POST requests
   - Message format: JSON (from Google Chat API)
   - Route to stan@fleetbrain.ai agent
   - Return response as JSON
   - Time: 1-2 hours (depends on OpenClaw HTTP routing setup)

5. **Register Chat App in Google Workspace**
   - Google Chat settings (workspace-wide) → Apps & integrations
   - Create new app:
     - Display name: "Stan" 
     - Description: "AI operations bot"
     - Icon: (optional)
   - Configuration:
     - Connection type: HTTP endpoint
     - Endpoint URL: `https://<openclaw-exposed-url>/chat/webhook`
     - Auth: Service account (JSON key)
   - Allow external users: YES (see admin settings below)
   - Time: 5-10 minutes

---

### What Stan Needs from Casey (Google Workspace Admin)

**1. Enable External Chat (Workspace Admin)**
   - Google Admin console → Apps → Google Chat & Meet → Chat settings
   - Setting: "Allow users to chat with external users"
   - Toggle: ON
   - Estimated time: 2 minutes (Casey does this)

**2. Allow External Users to Message Workspace**
   - Admin console → Apps → Google Chat & Meet → Chat settings
   - Setting: "Allow external users to message your organization"
   - Toggle: ON (if not already)
   - This lets strangers message stan@fleetbrain.ai directly
   - Estimated time: 2 minutes (Casey does this)

**3. Create Stan User Account (if not using stan@fleetbrain.ai directly)**
   - Option A: Use existing stan@fleetbrain.ai account, give service account access
   - Option B: Create dedicated bot account (stan-bot@fleetbrain.ai)
   - Recommendation: Option A (reuse existing)
   - Time: 0-5 minutes depending on choice

**4. Grant Service Account Chat Permissions (Optional but Recommended)**
   - Admin console → Security → API controls
   - Allowlist service account (stan-fleetbrain-bot@...) for Chat API calls
   - This prevents accidental abuse
   - Time: 5 minutes (Casey does this)

**5. Set Up Domain DLP/Filtering (Optional)**
   - Chat incoming messages from external users → log/scan
   - Prevents malicious prompts reaching Stan
   - Time: 10-30 minutes if paranoid, 0 if trust external traffic

---

### Implementation Checklist

**Stan's Tasks (6-8 hours total)**
- [ ] Create Google Cloud project + Chat API enable (30 min)
- [ ] Create service account + download JSON key (15 min)
- [ ] Deploy OpenClaw webhook endpoint for Chat (2-3 hrs)
- [ ] Test endpoint locally before exposing (30 min)
- [ ] Expose endpoint (Tailscale funnel or ngrok) (15 min)
- [ ] Register Chat app in Workspace (10 min)
- [ ] Test message flow end-to-end (30 min)

**Casey's Tasks (15 minutes total)**
- [ ] Enable external Chat in Admin console (2 min)
- [ ] Enable external users → internal messaging (2 min)
- [ ] Verify stan@fleetbrain.ai account exists (2 min)
- [ ] (Optional) Allowlist service account in API controls (5 min)
- [ ] (Optional) Set up Chat DLP if needed (10-30 min)

**Total Deployment Time:** 7-8 hours (1 calendar day with parallel work)

---

### Technical Details: Message Flow

```
External User texts/dms stan@fleetbrain.ai
      ↓
Google Chat API receives message
      ↓
Calls HTTP endpoint: POST https://<openclaw-url>/chat/webhook
Body: {
  "type": "MESSAGE",
  "space": "spaces/XXXXXX",
  "user": "users/XXXXXX",
  "message": {
    "name": "spaces/XXXXXX/messages/XXXXXX",
    "text": "Hello Stan, can you help with..."
  }
}
      ↓
OpenClaw webhook handler parses request
      ↓
Routes message to stan@fleetbrain.ai agent
Agent processes (like any other incoming message)
Agent generates response
      ↓
Stan calls Google Chat API:
POST https://chat.googleapis.com/v1/spaces/{spaceId}/messages
Auth: Service account (JWT token)
Body: {
  "text": "Sure! Here's what I can do...",
  "thread": { "name": "..." } // replies in same thread
}
      ↓
Response appears in user's Google Chat
User sees message immediately
```

---

### Security Considerations

1. **Service Account Key Storage**
   - Store JSON key securely (not in git, not in workspace)
   - Consider: Google Cloud Secret Manager
   - Rotate key yearly or if compromised

2. **External Message Filtering**
   - Google Chat doesn't pre-filter; all messages reach endpoint
   - Implement rate limiting in OpenClaw webhook (max 10 msgs/min per user?)
   - Implement content filtering (reject known prompt injection patterns)
   - Log all external messages for audit

3. **Endpoint Protection**
   - Use HTTPS only (Tailscale funnel or ngrok enforces this)
   - Validate Google Chat signature on incoming requests
   - Return 403 if signature invalid

4. **Service Account Scope Limitation**
   - chat.bot scope is minimal (can't read all workspace data)
   - Can only message in spaces service account is member of
   - If external user DMs, service account must be in DM thread (automatic)

---

### Fallback & Alternatives

**If HTTP endpoint too complex:**
- Use Apps Script (no infrastructure, but slower and harder to integrate with OpenClaw)
- Use Pub/Sub (async, better for batch, worse for conversational)

**If external messaging not allowed by compliance:**
- Only allow internal users (employees) to message Stan
- Requires different UX (no external lead contact)

**Phase 2 Alternative (after Google Chat works):**
- Add Twilio SMS + web chat (as originally planned)
- Google Chat handles *known* users
- Twilio handles *unknown* warm leads
- Users can escalate from SMS to Google Chat for continuity

---

## TASK 25: WORKSPACE MARKETPLACE SUBMISSION (P1, Casey+Stan)

**Objective:** Submit stan-fleetbrain-bot Chat app to Google Workspace Marketplace for public discovery

**Why:** 
- Removes friction (one-click install vs. manual invite)
- Increases credibility (marketplace-backed)
- Enables discovery by prospects who search "AI agent" or "agent for business"

**Deliverables:**
- [ ] App logo (400x400px, PNG)
- [ ] App description (2-3 sentences, marketing-focused)
- [ ] Privacy policy link (or full text)
- [ ] Support email (stan@fleetbrain.ai)
- [ ] Screenshot of app in action
- [ ] Submission to Google Workspace Marketplace

**Timeline:** 1-2 weeks Google review. Start once Task 27 (hardening) is done.

**Owner:** Casey (marketplace submission) + Stan (logo/description/screenshots)

---

## TASK 26: GOOGLE CHAT SPACES DEMO FLOW (P1, Stan)

**Objective:** Streamlined process to create per-prospect Google Chat Spaces for outreach

**Current workflow (manual):**
1. Casey identifies prospect
2. Stan creates Spaces (manu ally via Google Chat UI)
3. Casey invites prospect via shareable link
4. Prospect joins → full agent available

**Automate via:**
- [ ] Script to create Space: `spaces:create` API with prospect name + description
- [ ] Auto-generate shareable link
- [ ] Template Space name: "Demo: {prospect-name}"
- [ ] Initial welcome message from Stan
- [ ] Add to CRM + tracker for follow-up

**Timeline:** ~4 hours to automate. Reduces per-prospect setup from 5 min to 30 sec.

**Owner:** Stan

---

## TASK 27: HARDEN WEBHOOK SECURITY (P2, Stan)

**Blockers:** Currently at baseline security. Public URL via Tailscale Funnel.

**Hardening checklist:**
- [ ] Re-enable systemd sandboxing: ProtectSystem=strict, ProtectHome=true, PrivateTmp=true
- [ ] Google Chat signature validation: Implement HMAC-SHA256 verification
- [ ] Rate limiting: 10 msgs/min per external user (reject 429)
- [ ] Request audit log: Log all external requests to `/var/log/chat-webhook-audit.log`
- [ ] WAF-level checks: Detect + block prompt injection patterns
- [ ] DDoS hardening review: Tailscale Funnel limits + gunicorn backlog tuning

**Timeline:** ~6 hours. Deploy before marketplace launch (Task 25).

**Owner:** Stan

---

## TASK 28: 0-VAULT ENTRY FOR STAN-FLEETBRAIN-BOT KEY (P2, Casey)

**Objective:** Secure backup of service account key per 0-vault protocol

**Steps:**
1. Encrypt service account JSON: `gpg -c < fleetbrain-stan-prod-534550cd7a84.json > stan-chat-sa-key.json.gpg`
2. Upload to **0-vault/** on casey@fleetbrain.ai Drive
3. Delete plaintext from local .env (use env var only)
4. Update setup docs: reference encrypted file path + decryption instructions
5. Verify decryption works: `gpg -d stan-chat-sa-key.json.gpg | python3 -m json.tool`

**Status:** Key is currently in 0-vault but marked as "needed". This task completes the backup.

**Owner:** Casey (GPG encryption + Drive upload) + Stan (verify + docs update)

---

## TASK 1: SMS/WEB CHAT BRIDGE RESEARCH

### Requirement Summary
Warm lead contact channel: prospect texts phone number OR clicks web chat link → connects directly to Stan (no app install, no Telegram, zero friction).

### Platform Evaluation

#### 1. **TWILIO + OpenClaw (Native Integration)**
**Best fit for current architecture**

- **SMS:** $0.0075-0.0150 per message (volume discounts available)
- **Web Chat:** Via Twilio Flex or custom webhook to OpenClaw chatCompletions endpoint
- **Cost:** Phone number: $1-3/month; Per-message: ~$0.01-0.02
- **Setup Time:** 2-3 days (OpenClaw voice-call plugin already docs'd; SMS requires webhook routing)
- **Why it works:** 
  - OpenClaw has native Twilio voice-call plugin (documented)
  - Can expose OpenClaw chatCompletions endpoint via Tailscale/ngrok for web chat
  - Webhook routing: SMS → Twilio → OpenClaw agent → response
  - No third-party intermediary; full control
- **Friction:** Minimal. Prospect texts phone # or opens webhook-generated chat link
- **From Casey:** Need Twilio AccountSID + AuthToken; decide: incoming webhook port (recommend Tailscale funnel for security)

---

#### 2. **OpenPhone (formerly OpenPhone, now Quo)**
**Viable but less ideal**

- **SMS:** Included with plan + per-message billing on higher tiers
- **Web Chat:** Not native; would need third-party bridge
- **Cost:** $15-35/mo base plan + per-call overage ($0.45-0.75)
- **Setup Time:** 1-2 days (quick onboarding)
- **Why it falls short:** 
  - No native web chat; would require separate chat tool
  - SMS included but phone numbers cost money per user
  - Better for human phone ops than AI agent routing
- **Not recommended:** Adds a second tool when Twilio can do both

---

#### 3. **Crisp**
**Good if you want a turnkey customer service platform**

- **SMS:** Yes (inbound/outbound)
- **Web Chat:** Yes (included)
- **Cost:** $45-295/mo flat per workspace
- **Setup Time:** 1 day (marketing automation flavor, not ideal for API-first ops)
- **Why it's a trade-off:**
  - All-in-one platform (chat widget + SMS + email + phone)
  - Would require building custom Crisp → OpenClaw bridge via API
  - Adds complexity; Crisp expects to handle conversations, not route to external AI
- **Good for:** If you want Crisp as the primary interface and Stan as a backend integration
- **Not ideal:** Friction—prospects still see Crisp UI, not direct Stan connection

---

#### 4. **Intercom**
**Enterprise-grade, overkill for current use case**

- **SMS:** Via add-on
- **Web Chat:** Yes (included)
- **Cost:** Seat-based + $0.99 per resolution (Fin AI)
- **Setup Time:** 2-3 days (complex configuration)
- **Why skip:** 
  - Designed for large teams; expensive for single-agent ops
  - Resolution-based billing doesn't fit warm lead model
  - Heavier lift for OpenClaw integration

---

#### 5. **Tidio**
**Hybrid option; reasonable alternative**

- **SMS:** Yes (basic integration)
- **Web Chat:** Yes (Flows + live chat widget)
- **Cost:** $24-749/mo (Starter to Plus plans)
- **Setup Time:** 1-2 days
- **Why it could work:**
  - Cheaper than Crisp; better SMS support
  - Has API + Zapier for webhooks (can route to OpenClaw via webhook)
  - Lyro AI Agent (if you wanted on-platform) is separate cost
- **Trade-off:** Still routes through Tidio inbox; would need custom webhook to push to Stan directly

---

### RECOMMENDATION: **TWILIO + OpenClaw (Native)**

**Why:**
1. **Zero friction:** Prospect texts phone # → Twilio webhook → OpenClaw agent handles it live
2. **Full ownership:** No middleman platform; direct routing
3. **Web + SMS unified:** One phone number, two channels (SMS + web chat link)
4. **Existing ecosystem:** OpenClaw already has Twilio voice-call plugin; extend to SMS
5. **Cost-effective:** ~$20-30/mo (number + low message volume); scales linearly

**Setup & Deployment:**

| Step | Time | Owner | Notes |
|------|------|-------|-------|
| Twilio account + phone # | 1 hour | Stan | Need Twilio dashboard access |
| Configure SMS webhook | 4 hours | Stan | Route incoming SMS → OpenClaw webhook |
| Deploy chatCompletions endpoint | 2 hours | Stan | Expose via Tailscale funnel (secure) |
| Test SMS + web chat flows | 2 hours | Stan + Casey | Verify message routing, response handling |
| **Total** | **~9 hours / 1-2 days** | | Can compress to same-day with parallel work |

**What Stan Needs from Casey:**
1. Twilio account creation approval + funding (use FleetBrain corporate account?)
2. Phone number allocation (pick local or toll-free; recommendation: local for warm leads)
3. Public routing decision: Tailscale funnel (recommended) vs ngrok vs other
4. Response format preference (SMS character limit vs multi-message handling)

**Files to Update:**
- OpenClaw config: Add Twilio SMS webhook path + credentials
- StanleyBot tracker.json: Create "SMS/Chat Bridge Deployment" epic with 3-4 subtasks

---

## TASK 2: LINKEDIN HEADLINES & SUMMARY FOR CASEY

### Context
Casey: Founder building AI operations for service businesses. Built working multi-agent system. Open to consulting clients + full-time role. Tone: builder, not salesman.

### LinkedIn Headline Options (120 char limit)

**Option A (Authority + Builder):**
"Founder @ FleetBrain | Building AI agents for service businesses | Multi-agent ops expert"
*Length: 95 chars | Tone: Direct, credible*

**Option B (Broader Appeal + Problem-Solver):**
"Founder @ FleetBrain | AI Operations | Enabling businesses to scale through intelligent agents"
*Length: 98 chars | Tone: Aspirational*

**Option C (Opportunity-Signal):**
"Built AI agents that work. Now scaling. Founder, advisor, or consultant? Open to the right role."
*Length: 101 chars | Tone: Flexible, entrepreneurial*

---

### LinkedIn Summary Paragraph

Casey is building FleetBrain, an AI operations company that deploys intelligent agents for service businesses—locksmith, HVAC, staffing, and beyond. After testing hundreds of correction cycles, he's cracked the prompt-engineering problem that competitors struggle with: agents that actually close deals and keep customers happy, at scale.

He's open to three paths forward: growing FleetBrain through consulting clients, joining an AI operations company as VP/CTO, or advising early-stage AI teams that want production-grade deployment. He believes the real moat isn't model weights—it's repetition and real-world feedback loops.

If you're hiring for an AI operations role, building an agent product, or need a fractional AI exec for your scaling company, reach out.

---

### Notes
- Avoided buzzwords ("leveraging," "synergistic," "disruptive")
- Grounded in specifics (correction cycles, multi-agent, service verticals)
- Clear CTAs without being salesy
- Opens door to consulting + FTE in same message
- LinkedIn algorithm rewards message personalizations in DMs, so headline + summary should let people self-select into one of three buckets

---

## TASK 3: X SCOUT - SEED POST CONCEPTS FOR @itsolz

### Theme
"What it's actually like to run your business through an AI agent" — raw, authentic, no polish.

### Seed Concept #1: The Chaos Moment
**Angle:** First time your AI agent did something you didn't expect (but it worked)

*Sample opening:*
"I set up my agent to qualify locksmith leads. Day 2, customer asks a weird question about rekeying. Agent goes off-script, explains the whole thing, customer books immediately. I watched the transcript like 'wait, that wasn't in the prompt.' Been iterating ever since. That's the real feedback loop."

**Why it works:** 
- Relatable (every founder builds things that surprise them)
- Shows iteration, not perfection
- Implies scalability without claiming it
- Engagement hook: "What's surprised you about your agent?"

---

### Seed Concept #2: The Cost Truth
**Angle:** Money saved vs. money spent (honest breakdown)

*Sample opening:*
"People ask 'how much does AI save you?' Wrong question. Better: 'what does it let you do?' We freed up 10 hours/week of phone time. Didn't fire anyone. Hired a sales person instead. Cost $400/mo in Twilio + compute. Revenue per hire: $30k/mo baseline. Math is weird when it's working."

**Why it works:**
- Anti-hype (no "10x ROI claims")
- Shows second-order effects (hiring decisions)
- Gives concrete numbers (builds credibility)
- Implies playbook without overpromising

---

### Seed Concept #3: The Messy Truth
**Angle:** What doesn't work, what you're still figuring out

*Sample opening:*
"My agent is terrible at nuance. Cold transfers work great. Upsells? Bombs. Spent 3 weeks on prompt tweaks. Then realized I wasn't collecting the right context about customer history before the conversation started. Fix: better intake forms. Problem wasn't the agent, it was me. Still learning."

**Why it works:**
- Vulnerability (founders trust founders who admit gaps)
- Shows debugging mindset (not 'AI is magic')
- Implies continuous improvement
- Positions Casey as learner + builder, not guru

---

### Deployment Notes for @itsolz
- Post 1-2x per week (Tuesday/Thursday mornings seem to land better for B2B)
- Engage with 3-5 related threads before/after each post (build micro-network)
- Threads > single tweets (X algorithm rewards threaded conversations)
- Use 1-2 relevant hashtags: #AIAgents #BusinessAutomation #Founder (but avoid #AI #startup overstuffed tags)
- Reply to comments within 2 hours (signals active, builds visibility)
- Save transcript quotes from your own work—concrete > theory

---

**Status:** All three concepts queued; ready for @itsolz publication. Casey can pick timeline + cadence.

