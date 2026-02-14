# Skill: Application Tracker

## Purpose
Maintain applications.json as the single source of truth for Casey's job search.
Tracks every lead from surfaced → applied → interviewing → offer/rejected/withdrawn.
Generates weekly summaries and flags stale applications for follow-up.

## Data File
- **Local:** D:\StanleyBot\applications.json
- **Drive sync:** Auto via Google Drive for Desktop (casey@fleetbrain.ai)
- **Drive file ID:** TBD (will populate after first sync confirms)

## Schema — Application Entry
```json
{
  "id": "APP-001",
  "company": "Anthropic",
  "role": "Enterprise Account Executive",
  "location": "Remote (US)",
  "comp": "$180K-$220K OTE",
  "link": "https://...",
  "source": "LinkedIn Jobs",
  "fit_score": "HIGH",
  "fit_notes": "AI company, enterprise sales cycle, consultative selling emphasized. Casey has contact (Eric H) at adjacent org.",
  "contact_match": "Eric Hendricks — former Red Hat, now in AI adjacent role",
  "status": "Surfaced",
  "dates": {
    "surfaced": "2026-02-13",
    "applied": null,
    "response": null,
    "interview_1": null,
    "interview_2": null,
    "offer": null,
    "closed": null
  },
  "notes": "",
  "next_action": "Casey review — APPLY / TRACK / SKIP",
  "next_action_date": "2026-02-14",
  "materials": {
    "cover_letter": null,
    "outreach_draft": null,
    "prep_briefing": null
  }
}
```

## Status Values
| Status | Meaning |
|--------|---------|
| Surfaced | Job Scout found it, awaiting Casey decision |
| Watching | Casey said TRACK — check periodically for updates |
| Applying | Casey said APPLY — drafting materials |
| Applied | Application submitted |
| Response | Heard back (positive or negative) |
| Interview | Active interview process |
| Offer | Offer received |
| Rejected | They said no |
| Withdrawn | Casey pulled out |
| Skipped | Casey said SKIP on initial surface |

## Execution — Stan (Daily, embedded in Job Scout)
1. After surfacing new leads, append them to applications.json with status "Surfaced"
2. Scan existing applications for follow-up triggers:
   - Applied > 7 days ago with no Response → flag in Telegram
   - Interview scheduled within 48 hours → generate prep briefing
   - Watching entries > 14 days old → re-check if role is still open
3. Include application pipeline summary in daily Telegram delivery:
   ```
   📊 Pipeline: [X] active, [Y] awaiting response, [Z] interviewing
   ⚠️ Follow-up needed: [company — role, applied X days ago]
   ```

## Execution — SuperStan
- Can query applications.json on demand: "what's my pipeline look like" or "status on [company]"
- Can add entries manually when Casey finds roles outside the scout
- Can generate prep briefings for interviews using research-log + contacts.json + web research

## Weekly Summary (Sundays, appended to daily briefing)
```
📊 WEEKLY JOB SEARCH SUMMARY

New leads surfaced: [X]
Applications submitted: [X]
Responses received: [X]
Interviews scheduled: [X]
Pipeline total: [X] active

Top priority this week:
- [Company — Role — next action]
- [Company — Role — next action]

Stale (no activity >7 days):
- [Company — Role — last status — days since update]
```

## Rules
- Never modify status without Casey's instruction (except Surfaced → auto on scout)
- Never delete entries. Rejected/Skipped/Withdrawn stay for historical tracking.
- Dedup by company + role title. If same company posts similar role later, create new entry with reference to old one.
- All prep briefings saved to materials.prep_briefing field as Drive file path
- Cover letters and outreach drafts require Casey approval before use

## Status
ACTIVE — skill definition complete. applications.json initialized. Requires Stan cron integration with job-scout.md.
