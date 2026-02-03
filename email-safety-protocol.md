# Email Safety Protocol: Gmail Integration for Stan
**Created:** 2026-02-02 21:58 CST  
**Risk Level:** High (Gmail account lockout possible)  
**Status:** Research phase, awaiting Casey approval

---

## The Problem (History)

Stan's previous Gmail account was shut down by Gmail's automated bot detection. This is a real and documented issue:

**Why Gmail Bans Bots:**
- Unusual access patterns (accessing from new IP, high request volume)
- Automated actions that look like account compromise
- Lack of proper OAuth/authentication
- Mass email operations or suspicious forwarding

**What We Must Avoid:**
- Password-based authentication (looks like compromise)
- Frequent polling (> 1 request per minute)
- Real-time email processing
- Email forwarding or modification
- Accessing from suspicious IP ranges
- High volume of new API requests

---

## Strategy: Conservative Gmail Integration

### Principle
Treat Casey's Gmail like a VIP service: minimal access, maximum transparency, easy kill-switch.

### Implementation Rules

#### 1. Authentication (OAuth 2.0 Only)
```
✅ Use Google OAuth 2.0 (User Context)
❌ Never use password authentication
❌ Never use service account
❌ Never cache credentials indefinitely
```

**How it works:**
1. Stan initiates OAuth flow
2. Casey logs in to Google (proves identity)
3. Casey explicitly grants permissions
4. Stan gets time-limited token (refresh as needed)
5. Casey can revoke access anytime in Google Account settings

#### 2. Permissions (Minimal)
```
Request ONLY:
✓ gmail.readonly (read-only access)
✓ Label-specific access (if Gmail supports)
✓ Never request gmail.modify (write/delete)
✓ Never request gmail.send (composing emails)
✓ Never request gmail.settings.basic (configuration)
```

**What Stan CAN do:**
- Read emails from specific labels
- Search by from/to/subject
- Extract metadata (sender, timestamp, subject)
- Skip email content unless critical

**What Stan CANNOT do:**
- Delete or archive emails
- Mark as read/unread
- Create filters
- Forward emails
- Reply/send emails
- Access attachments
- Modify settings

#### 3. Polling Strategy (Infrequent)
```
Current Gmail API limits (free tier):
- 100 queries per 100 seconds
- 1.5 million requests per day (shared)

Safe pattern for Stan:
- Check mail labels: 1 request per hour (not real-time)
- Search: 1 request per day (for urgent filters)
- Total: ~24 requests/day = 0.0002% of daily limit
```

**This means:**
- Stan reads Casey's email ~once per hour
- "Urgent" emails still take 1 hour to detect (acceptable for non-emergency)
- Consistent, predictable pattern (looks legitimate to Gmail)
- Never triggers rate limiting

#### 4. Monitored Labels Only
```
Ask Casey: "Which Gmail labels should I monitor?"

Examples (Casey decides):
✓ "Urgent" label
✓ "From Rosa" label
✓ "From Jeff" label
✓ "VIP" label
✓ Custom label X, Y, Z

Not monitored:
✗ All mail
✗ Promotional
✗ Social
✗ Spam
```

**This gives Casey:**
- Control over what Stan sees
- Privacy (personal/sensitive stuff not monitored)
- Predictable behavior (Stan only cares about labels Casey whitelists)

#### 5. Transparency + Kill-Switch
```
What Casey will see:
✓ Log: "Checked email at 10:00am, found 2 urgent messages"
✓ Alert: "Stan tried to access email, but Gmail flagged it - disabled"
✓ Control: One click in Google Account to revoke Stan's access

If Gmail flags account:
✓ Immediately alert Casey
✓ Automatically disable email monitoring
✓ Never retry (wait for Casey's manual intervention)
✓ Log everything for troubleshooting
```

#### 6. User-Agent Transparency
```
HTTP header identifies Stan:
User-Agent: "OpenClaw-Stan/1.0 (+http://openclaw.ai; bot@casey)"

This tells Gmail:
✓ What this is (automated)
✓ Who owns it (Casey)
✓ What it is (legitimate service)
✓ Where to complain (contact info)
```

#### 7. Conservative Error Handling
```
If Gmail returns:
- 403 Forbidden → User revoked token → Stop immediately
- 429 Too Many Requests → Rate limited → Back off for 1 hour
- 5xx Server Error → Gmail down → Retry with 1-hour delay
- Security Warning → Account flagged → Disable and alert Casey
```

---

## Implementation Checklist

### Before Activation
- [ ] Casey reviews this protocol
- [ ] Casey lists labels to monitor (explicit whitelist)
- [ ] Casey authorizes email access (OAuth grant)
- [ ] Stan implements kill-switch logic
- [ ] Stan implements error handling + alerts

### During Activation
- [ ] First check: Is it working?
- [ ] Second check: Did Gmail flag anything?
- [ ] Third check: Can we revoke access cleanly?
- [ ] Fourth check: Is data parsing correct?

### Ongoing Monitoring
- [ ] Daily: Check for Gmail security warnings
- [ ] Daily: Log email check success/failure
- [ ] Weekly: Report on email monitoring activity
- [ ] Monthly: Audit Gmail permissions (ensure nothing was expanded)

---

## What Stan Will Do (With Email Access)

### Morning Briefing (7am)
Extract from whitelisted labels:
- VIP/Urgent emails from last 24 hours
- From/To information
- Subject line
- Timestamp
- Send summary to Casey: "3 urgent emails since yesterday. From Rosa (2), From Jeff (1)."

### Throughout Day
When Casey asks "Any new urgent emails?":
- Stan checks monitored labels
- Returns summary in <2 seconds
- Does NOT read full content (privacy)
- Only flags: sender, subject, timestamp

### That's It
- NO automated replies
- NO email modifications  
- NO forwarding
- NO filtering

---

## Cost & Performance

**API Cost:**
- 24 email checks/day × $0.0001 per query = $0.0024/day = $0.07/month
- Negligible impact on budget

**Performance:**
- One check every hour
- 100-500ms response time
- No blocking (runs in background)
- Automatic failure handling

---

## Risk Mitigation Summary

| Risk | Mitigation |
|------|-----------|
| Gmail detects bot | OAuth 2.0 + transparent user-agent + infrequent polling |
| Casey locked out | Kill-switch + immediate alert if flagged |
| Privacy breach | Labels-only whitelist + read-only access |
| Email corruption | No write/delete permissions |
| Rate limiting | Carefully spaced requests (24/day) |
| Account compromise | OAuth tokens time-limited + refreshable |

---

## Open Questions for Casey

1. **Which labels should I monitor?** (Explicit list)
2. **What time should I check?** (Once per hour, or different schedule?)
3. **Alert me for what keywords?** (Just sender-based, or content search too?)
4. **Can I read email content, or just metadata?** (Subject/from/time only, or full body?)
5. **What's the kill-switch?** (How do you want to disable this if something goes wrong?)

---

**Status:** Ready for Casey's approval + label whitelist.  
**Next:** Once Casey approves, implement OAuth flow and test with 1 monitored label.
