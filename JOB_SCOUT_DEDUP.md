# Job Scout Deduplication Logic

## Overview
Prevent the job scout from surfacing the same leads repeatedly.

## Implementation

### Before Surfacing
1. Search for new job leads (via Perplexity, Exa, or manual research)
2. Extract lead metadata: company, title, location, salary, URL
3. Generate `url_hash`: deterministic ID based on company + title + location
4. Check `job_scout_seen.json` for matching `url_hash`
5. **If found:** Skip the lead (already surfaced)
6. **If new:** Add entry to `seen_jobs`, surface to Casey, update file

### Output
- **New leads found:** Surface with date and fit level (HIGH/MEDIUM/LOW)
- **No new leads:** Report "No new job leads today. Last search: [date]. Refresh jobs? Y/N"

### File Format (job_scout_seen.json)
```json
{
  "seen_jobs": [
    {
      "company": "Name",
      "title": "Role",
      "location": "City/Remote",
      "salary": "$XXX–$XXX",
      "url_hash": "unique_id",
      "surfaced_date": "YYYY-MM-DD",
      "fit": "HIGH|MEDIUM|LOW"
    }
  ]
}
```

## Testing
- Search for new jobs in automotive, logistics, and operations
- Verify no leads from previous 3 scans are re-surfaced
- Confirm "no new leads" message if all results are seen

## Related Tasks
- #20: Job scout automation (improve signal quality, add dedup)
