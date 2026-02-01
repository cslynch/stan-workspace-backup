# Stan's Full Toolset - Experimentation Mode

**Activated:** 2026-02-01 11:27 CST  
**Status:** All tools enabled (no deny list)

---

## 🎯 Core Tools (Always Had These)

### File Operations
- **read** - Read any file (text, images)
- **write** - Create/overwrite files
- **edit** - Surgical text replacements

### Memory & Recall
- **memory_search** - Semantic search across MEMORY.md + memory/*.md
- **memory_get** - Targeted snippet reads from memory files

### Communication
- **message** - Send messages, polls, reactions, cross-channel ops

### System Control
- **exec** - Run shell commands (full pty support for interactive CLIs)
- **cron** - Schedule jobs, set reminders, wake events
- **gateway** - Restart, update, config management

---

## 🆕 NEW CAPABILITIES UNLOCKED

### Web & Research
- **web_search** - Brave Search API (fast, current info)
- **web_fetch** - Grab webpage content as markdown/text (no browser needed)
- **browser** - Full browser automation (Chrome control, screenshots, snapshots, UI interaction)

### Creative & Visual
- **canvas** - Visual/creative work (render UIs, generate images, present content)
- **tts** - Text-to-speech (convert text to audio, MEDIA paths)

### Infrastructure & Devices
- **nodes** - Control paired devices (camera, screen recording, location, notifications, run commands on remote devices)
- **process** - Manage background exec sessions (poll, write, kill)

### Multi-Agent Operations
- **agents_list** - See available agent IDs for spawning
- **sessions_list** - List all active sessions (main + sub-agents)
- **sessions_history** - Read message history from other sessions
- **sessions_send** - Send messages to other sessions
- **sessions_spawn** - Spawn background sub-agents for parallel work
- **session_status** - Usage stats for any session

---

## 💰 Cost Impact

**Before (10 tools):** ~4,400 tokens cache read, $0.0145/msg  
**After (21 tools):** ~4,900 tokens cache read, $0.0193/msg  

**Increase:** ~500 tokens, +$0.0048/msg (less than half a cent)

### Updated Projections
At 30-50 messages/day:
- **Daily:** $0.58 - $0.97
- **Monthly:** $17.40 - $29.10

**Still well within budget.** Tools are cheap. Skills were the problem.

---

## 🎪 Fun Experiments to Try

### Web Research
- Live web search → fetch content → summarize
- Monitor websites for changes
- Grab competitor pricing, news, etc.

### Browser Automation
- Screenshot websites
- Fill forms, scrape data
- Test web apps, monitor dashboards

### Visual/Creative
- Render data visualizations on canvas
- Create shareable web UIs
- Generate diagrams/charts

### Voice
- Convert updates to audio messages
- TTS for Rosa (sweet reminders via Telegram voice)

### Multi-Agent
- Spawn sub-agents for long research tasks
- Parallel processing (one agent per task)
- Background monitoring without blocking main chat

### Device Control
- Remote camera snapshots from your phone
- Screen recordings
- Location tracking
- Push notifications to devices

---

## 🔐 What's Still Safe

**No dangerous operations enabled:**
- Config changes still require your approval
- Gateway restarts log reasons
- File operations limited to workspace
- Memory operations are read-focused

**Philosophy:** Full capability, smart guardrails.

---

*Let's play.* 🧭
