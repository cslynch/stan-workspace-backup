# MEMORY.md - Long-Term Memory

## Casey & Rosa

- **Relationship:** 1.5 years together
- **Future:** Engagement is coming. Casey will want help planning it. (Not today, but he wants me to remember.)
- **Personality:** Rosa appreciates romance, doesn't need alcohol to have a good time
- **Notes:** First date night was 2026-01-30 at Brenner's (5:30 PM)
- **Valentine's Day 2026:** Casey needs help planning something special. Keep on him about this. (Date: Feb 14, 2026)

## Business: OpenBot / AI Backend Service

### The Core Idea
We're building an AI-powered business operations platform where I (Stan) handle logistics, client communication, and workflow management for service businesses. The differentiator: business owners get a real conversational AI partner (me) to run their operations, not just static software. Starting with locksmith services (RapidKey), scalable to HVAC, maintenance, and other service types across any geography. Revenue model: take a cut per job (Greenfield) or tiered subscription (Brownfield/established businesses).

### Team Structure
- **Casey:** Founder, system owner. All system-level decisions (model changes, config, architecture, security) require Casey's approval.
- **Jeff:** Cofounder. Full authority on business operations, strategy, pricing, workflows, new service ideas. Cannot make system-level changes.

### Access Control Boundary
- **Casey only:** Model/reasoning changes, gateway config, core architecture, security settings
- **Jeff full access:** Business operations, pricing, workflows, marketing, sales, documentation, service expansion ideas

### Platform Architecture (Multi-Agent System)

**Customer Agents (Worker Layer):**
- Each customer gets their own AI agent with custom name, personality, business context
- Run on AWS VMs: small customers share VMs, large customers get dedicated instances
- Sandboxed environments to prevent data leakage between customers
- Each agent manages one business's operations (scheduling, dispatching, customer communication)

**Stan (MANO Layer - Management & Orchestration):**
- I sit above all customer agents as the master brain
- Monitor fleet health, spawn/manage customer agents
- Provide dashboard for Casey & Jeff (all agents + business stats)
- Customer agents report analytics to me (aggregated, anonymized)

**Data Strategy:**
- **Flows UP to Stan (aggregated, anonymized):** Jobs completed, revenue, conversion rates, response times, customer satisfaction patterns, service performance, geographic demand, operational bottlenecks
- **Stays ISOLATED in customer sandboxes:** Customer names/addresses/phones, specific job details, conversations, pricing specifics, business financials
- **Key principle:** I get *patterns*, not *people*. Analytics without exposure.
- **Future:** Optional "insight network" where customers can opt-in to learn from aggregated patterns across the fleet

**Name Ideas (better than "Office-Manager-as-a-Service"):**
- OpsMind (Operations + AI Mind)
- BackOffice.ai (direct value prop)
- FleetMind (for service fleets)
- Dispatch.ai (simple, operational)
- CommandPost (military precision)

### Go-to-Market Strategy

**Phase 1 (Friendly Beta - Current):**
- Start with friendlies (free beta customers)
- Manual customer agent setup (Casey/Jeff provision)
- Simple analytics dashboard (jobs, revenue, uptime)
- One-on-one support, iterate fast
- Build for scale from day one, but keep it simple initially

**Phase 2 (Productized):**
- Self-service onboarding flow
- Customer customizes their agent (name, personality, hours)
- Auto-provisioning to shared VMs
- Tiered pricing kicks in

**Phase 3 (Platform):**
- Web signup, full self-service
- Aggregated insights ("Top HVAC shops average 8.2 jobs/day")
- Marketplace (integrations, add-ons)
- Scale across multiple verticals

**Target Market:**
- Primary: Service businesses (locksmith, HVAC, concrete, maintenance)
- Jeff's concrete and HVAC contacts are early prospects
- They struggle with operations management (scheduling, dispatching, customer communication)
- Value prop: AI "employee" who never sleeps, doesn't call in sick, handles operational chaos

---

*Data is king. Start simple, build for scale.*
