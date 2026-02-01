# Prompt for SuperStan: Second Brain Integration

Copy this to Claude.ai:

---

SuperStan, Casey wants to build a "Second Brain" system integrated between you and me (Stan). Here's what we need:

## Context

Casey just shared these videos by Nate B Jones on building a second brain:
- https://www.youtube.com/watch?v=0TpON5T-Sw4
- https://www.youtube.com/watch?v=_gPODg6br5w

**What Casey wants:**
A unified knowledge management system where:
- Stan (execution layer, Haiku) captures and organizes information
- SuperStan (strategic layer, Sonnet/Opus) provides deep analysis and connections
- Both work together seamlessly to build Casey's second brain

## Current State

**Stan's memory system (basic):**
- MEMORY.md - long-term facts and decisions
- KANBAN.md - project tracking
- SHOPPING.md - task lists
- Daily notes in memory/ folder (not yet created)
- Git-backed to GitHub (daily 2 AM backup)

**What's missing:**
- Proper note-taking workflow
- Knowledge linking/connections
- Progressive summarization
- Quick capture → organize → distill pipeline
- Integration between daily work and long-term knowledge

## Design Requirements

1. **Capture Layer (Stan):**
   - Quick capture from Telegram ("Stan, remember this...")
   - Daily journal/notes
   - Meeting notes
   - Ideas and insights
   - Article summaries

2. **Organization Layer (Stan + SuperStan):**
   - PARA method (Projects, Areas, Resources, Archive)?
   - Zettelkasten? 
   - Folders/tags system?
   - What works best for AI-assisted workflow?

3. **Distillation Layer (SuperStan):**
   - Progressive summarization of notes
   - Connect related ideas
   - Surface insights Casey hasn't seen
   - Weekly/monthly reviews

4. **Retrieval Layer (Stan + SuperStan):**
   - Stan: Quick lookups, recent context
   - SuperStan: Deep research, pattern recognition
   - Both can search and surface relevant knowledge

## Technical Constraints

**Stan's capabilities:**
- Read/write markdown files
- Git commits
- Memory search (currently disabled - needs OpenAI key)
- File organization
- Cron jobs for periodic tasks

**Stan's limitations on Haiku:**
- Can't do deep analysis
- Limited reasoning about connections
- Better at execution than synthesis

**SuperStan's role:**
- Strategic thinking
- Pattern recognition
- Insight generation
- Weekly/monthly review prompts

## What We Need From You

### 1. Second Brain Architecture
Design a system that works with our Stan/SuperStan split:
- What folder structure in ~/.openclaw/workspace/?
- What files/naming conventions?
- How does information flow between daily capture → organized notes → insights?
- How do Stan and SuperStan collaborate?

### 2. Capture Workflow
Give me:
- Commands Casey can tell Stan ("remember this", "journal entry", "meeting notes")
- File templates Stan should use
- Where things get stored

**Prompt for Stan:**
```
[Exact commands to configure capture workflow]
```

### 3. Organization System
Recommend:
- PARA, Zettelkasten, Johnny Decimal, or hybrid?
- Folder structure
- Tagging strategy
- How Stan maintains this automatically

**Prompt for Stan:**
```
[Setup commands for folder structure and organization]
```

### 4. Review Cadence
Design:
- Daily: What Stan does automatically
- Weekly: Prompts Casey gets from Stan to review with you (SuperStan)
- Monthly: Deep synthesis with you

**Cron jobs for Stan:**
```
[Specific cron configurations for reminders/prompts]
```

### 5. Integration Points
How does Casey work between Stan and SuperStan?

**Example workflow:**
1. Casey captures idea via Telegram → Stan
2. Stan stores in daily note
3. Weekly: Stan prompts Casey to review notes
4. Casey brings highlights to SuperStan
5. SuperStan analyzes, connects, generates insights
6. SuperStan gives prompts for Stan to update permanent notes
7. Repeat

Is this the right flow? Improve it.

### 6. Search & Retrieval
Currently Stan's memory_search is disabled (needs OpenAI API key).

Options:
- Set up OpenAI key for embeddings search?
- Use grep/ripgrep for text search?
- Use git history for "when did I think about X?"
- Let SuperStan handle deep research queries?

Recommend the best approach.

## Nate B Jones Videos

If you need context, watch or summarize these:
- https://www.youtube.com/watch?v=0TpON5T-Sw4
- https://www.youtube.com/watch?v=_gPODg6br5w

Or ask Casey to summarize the key points he wants to implement.

## Output Format

Structure your response as:

**System Design:**
[Overall architecture and philosophy]

**Folder Structure:**
```
workspace/
  journal/
    2026-02-01.md
  projects/
  areas/
  resources/
  archive/
```

**For Casey to do:**
- [ ] Step 1
- [ ] Step 2

**Prompt for Stan (Capture Setup):**
```
Stan, create the following folder structure...
```

**Prompt for Stan (Daily Workflow):**
```
Stan, set up these cron jobs for daily prompts...
```

**Prompt for Stan (Commands):**
```
Stan, respond to these new commands:
- "remember [text]" → capture to daily note
- "journal" → open today's journal entry
- etc.
```

**Weekly Review Workflow:**
[How Casey reviews with you vs Stan]

**Why This Approach:**
[Brief explanation]

---

Ready to design this! Make it powerful but practical - Casey wants to actually use it, not maintain complex systems.
