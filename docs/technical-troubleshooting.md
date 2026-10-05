# Technical Troubleshooting Guide

## System Requirements

### Web Application
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Browser** | Chrome 90+, Firefox 88+, Safari 14+, Edge 90+ | Latest stable |
| **JavaScript** | ES2020 support required | Latest |
| **Cookies** | First-party required | First + third-party for analytics |
| **Local Storage** | 5 MB available | 50 MB+ |
| **Screen Resolution** | 1280×720 | 1920×1080+ |
| **Internet** | 1 Mbps | 10+ Mbps |

### Mobile App
| Platform | Minimum OS | Recommended | Architecture |
|----------|------------|-------------|--------------|
| **iOS** | iOS 14.0 | iOS 17+ | arm64 (iPhone 8+) |
| **Android** | Android 10 (API 29) | Android 14 | arm64-v8a, x86_64 |
| **Storage** | 200 MB free | 1 GB+ | - |
| **RAM** | 2 GB | 4 GB+ | - |

### API Integration
- **Protocol**: HTTPS only (TLS 1.2+)
- **Authentication**: Bearer tokens (JWT) or API Keys
- **Rate Limits**: See API docs (varies by plan)
- **Payload**: JSON (max 10 MB/request)
- **Timeouts**: 30s default, 300s max (configurable)

---

## Common Issues & Solutions

### 1. Login & Authentication Issues

#### "Invalid credentials" but password is correct
**Causes**: Caps lock, wrong email, account not verified, too many attempts
**Solutions**:
- Check caps lock / num lock
- Try email vs username
- Check email for verification link (expires 24h)
- Wait 30 min after 5 failed attempts
- Use "Forgot Password" flow
- Clear browser cookies for company.com

#### 2FA not working / lost access
**Authenticator app codes invalid**:
- Sync time on phone (Settings → General → Date/Time → Set Automatically)
- Ensure correct account in app (multiple entries possible)
- Try backup codes (saved during 2FA setup)

**Lost phone / authenticator**:
- Use backup codes (10 single-use codes)
- No backup codes? Contact support with:
  - Government-issued photo ID
  - Selfie with ID
  - Last 4 digits of payment method
  - Verification takes 24-48 hours

**SMS 2FA not receiving codes**:
- Check signal / not in airplane mode
- Ensure phone number correct in Settings → Security
- Try "Resend code" (max 3/hour)
- Carrier blocking short codes? Contact carrier
- Switch to authenticator app (more reliable)

#### Session keeps expiring / logged out randomly
**Causes**: Multiple tabs, cookie settings, VPN/proxy, browser privacy
**Solutions**:
- Don't log in same account in multiple browsers simultaneously
- Allow cookies for company.com (not just session)
- Disable "Block third-party cookies" for our domain
- VPN/proxy rotating IPs triggers security logout
- Browser extensions (Privacy Badger, uBlock) may interfere
- Corporate firewall may strip cookies

#### SSO login failing
**SAML/OIDC errors**:
- "Invalid SAML Response": IdP clock sync (NTP), metadata expired
- "User not provisioned": JIT disabled, user doesn't exist
- "Attribute mapping failed": Email/name attributes missing in IdP
- "Certificate validation failed": IdP cert expired, update in Settings → SSO

**Test**: Use IdP-initiated login vs SP-initiated. Check SAML tracer browser extension.

---

### 2. Performance & Loading Issues

#### Page loads slowly / times out
**Diagnose**:
1. Check status.company.com for incidents
2. Open DevTools (F12) → Network tab → reload
3. Look for: Red entries, long TTFB (>1s), large downloads
4. Test on different network (mobile hotspot)

**Common Causes & Fixes**:
| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Slow initial load | Cold start / CDN cache miss | Refresh; usually resolves in 30s |
| Slow dashboard | Large dataset, complex queries | Use filters; reduce date range |
| Slow file upload | Network, file size, antivirus | Compress; try wired connection |
| Slow API calls | Rate limited, heavy payload | Batch requests; check headers |
| Intermittent | WiFi interference, ISP issues | Wired connection; different DNS (1.1.1.1) |

**Browser-specific**:
- Chrome: Disable hardware acceleration (Settings → System)
- Firefox: Disable "Enhanced Tracking Protection" for site
- Safari: Disable "Prevent cross-site tracking"
- Extensions: Disable all, test, re-enable one by one

#### "Network Error" / "Failed to fetch"
**Checklist**:
- [ ] Internet working (visit other sites)
- [ ] Not on corporate VPN blocking our domains
- [ ] Firewall/antivirus not blocking *.company.com
- [ ] Browser not in "Work Offline" mode
- [ ] No proxy misconfiguration (try disable proxy)
- [ ] DNS resolving (try `nslookup api.company.com`)

**Domains to allowlist**:
- `*.company.com`
- `*.company-cdn.com`
- `*.auth.company.com`
- `cdn.jsdelivr.net` (libraries)
- `fonts.googleapis.com` / `fonts.gstatic.com`

#### Mobile app crashes / freezes
**iOS**:
- Force close: Swipe up from bottom, hold, swipe app up
- Restart phone (hold power + volume)
- Reinstall: Delete app, re-download from App Store
- Check iOS version: Settings → General → About

**Android**:
- Force stop: Settings → Apps → Company App → Force Stop
- Clear cache: Same screen → Storage → Clear Cache
- Clear storage (logs you out): Clear Storage
- Reinstall from Play Store
- Check Android System WebView updated (Play Store)

**Both**:
- Free storage >500 MB
- Background app refresh enabled
- Battery optimization disabled for app
- App permissions: Storage, Camera, Network

---

### 3. File Upload & Sync Issues

#### Upload fails / stuck at 0%
**File checks**:
- Size limit: Free 100MB, Pro 2GB, Business 10GB, Enterprise 50GB
- Type allowed: See allowed types in upload dialog
- Not corrupted: Open locally first
- Not password protected / encrypted
- Filename: No special chars, <255 chars, no leading/trailing spaces

**Network checks**:
- Stable connection (not mobile data at edge)
- No upload bandwidth cap (QoS, corporate policy)
- Try smaller file first
- Pause other uploads/cloud sync (Dropbox, OneDrive, etc.)

**Browser/App**:
- Don't navigate away during upload
- Keep tab/app in foreground
- Disable "Data Saver" modes
- Chrome: Allow "Background sync" for site

**Error codes**:
| Code | Meaning | Action |
|------|---------|--------|
| 413 | File too large | Compress or upgrade plan |
| 415 | Unsupported type | Convert to allowed format |
| 429 | Rate limited | Wait 60s, retry |
| 500 | Server error | Retry in 5 min; contact support if persists |
| 503 | Maintenance | Check status page |
| NETWORK | Connection lost | Check internet; resume upload |

#### Files not syncing / missing
**Web**: Refresh page (Cmd/Ctrl+R). Clear cache if stale.
**Mobile**: Pull to refresh. Settings → Sync → Sync Now.
**Desktop app**: Right-click tray icon → Sync Now.

**Conflict resolution**: "Conflict copy" created when same file edited offline on multiple devices. Original + conflict copy both kept. Manual merge required.

**Selective sync**: Settings → Sync → Choose folders. Unchecked folders = not downloaded locally.

---

### 4. Integration & API Issues

#### API returns 401 Unauthorized
**Causes**: Token expired, wrong token, wrong scope, IP allowlist
**Debug**:
```bash
# Test token
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.company.com/v1/user/me

# Check token expiry (JWT)
echo "YOUR_TOKEN" | cut -d. -f2 | base64 -d | jq .exp
# Convert exp timestamp: date -r <exp>
```

**Fixes**:
- Generate new API key: Settings → Developers → API Keys
- Check scopes match endpoint requirements
- Verify IP allowlist (Settings → Developers → IP Allowlist)
- Ensure `Content-Type: application/json` header

#### API returns 429 Too Many Requests
**Rate Limits by Plan**:
| Plan | Requests/min | Burst | Concurrent |
|------|--------------|-------|------------|
| Free | 60 | 10 | 2 |
| Starter | 300 | 50 | 5 |
| Pro | 1,000 | 200 | 10 |
| Business | 5,000 | 1,000 | 25 |
| Enterprise | Custom | Custom | Custom |

**Headers to monitor**:
- `X-RateLimit-Limit`: Max requests
- `X-RateLimit-Remaining`: Remaining in window
- `X-RateLimit-Reset`: Unix timestamp when reset
- `Retry-After`: Seconds to wait (on 429)

**Best practices**:
- Implement exponential backoff (1s, 2s, 4s, 8s...)
- Cache responses where possible
- Batch operations (bulk endpoints)
- Use webhooks instead of polling

#### Webhook not receiving events
**Checklist**:
- [ ] URL accessible from internet (not localhost)
- [ ] HTTPS with valid cert (not self-signed)
- [ ] Responds 2xx within 10s (else retry)
- [ ] No redirect loops (3xx)
- [ ] Firewall allows our IPs (see below)
- [ ] Signature verification passing

**Our webhook IPs** (allowlist these):
```
54.123.45.0/24
52.89.12.0/24
3.12.234.0/24
```
**Test**: Settings → Developers → Webhooks → "Send Test Event"
**Retry schedule**: 1m, 5m, 15m, 1h, 6h, 24h (max 7 days)
**Dead letter**: After 7 days, view in Settings → Developers → Webhook Logs

#### Integration (Zapier, Make, n8n) not working
- Re-authenticate connection
- Check trigger/action versions (update if deprecated)
- Test step individually
- Check task history for errors
- Our Zapier app: "Company App" (verified, updated monthly)

---

### 5. Data & Export Issues

#### Export taking too long / failing
**Limits**:
- Max export size: 5 GB (single request)
- Timeout: 30 minutes
- Concurrent exports: 1 per user

**Large exports**: Use "Schedule Export" → receive email with download link when ready (background job).

**Formats**: CSV (default), JSON, Excel (.xlsx), PDF (reports only)
**Filters**: Apply date range, project, user filters to reduce size

#### Data looks wrong / missing
**Common causes**:
- Wrong date range filter (check timezone: Settings → Profile → Timezone)
- Archived items hidden (toggle "Show archived")
- Permissions: Can't see other users' private data
- Deleted items: In trash 30 days, then permanent
- Sync delay: Up to 5 min for real-time updates

**Audit trail**: Settings → Security → Audit Logs → Filter by "Data Export" / "Data Delete"

#### Import failures (CSV, JSON)
**CSV Requirements**:
- UTF-8 encoding (not UTF-16, not ANSI)
- Headers in row 1 (exact match to field names)
- Max 50,000 rows per import
- Date format: ISO 8601 (YYYY-MM-DD) or MM/DD/YYYY
- Boolean: true/false, yes/no, 1/0
- Escaping: Double quotes for commas/newlines in fields

**Common Errors**:
| Error | Fix |
|-------|-----|
| "Invalid header: X" | Check spelling, case-sensitive |
| "Row 42: Invalid date" | Fix date format in that row |
| "Duplicate key: email" | Enable "Update existing" or remove dupes |
| "Required field missing" | Add column for required fields |
| "Encoding error" | Save as UTF-8 in Excel/Notepad++ |

---

### 6. Browser & Extension Conflicts

#### Known Problematic Extensions
| Extension | Issue | Fix |
|-----------|-------|-----|
| uBlock Origin | Blocks analytics, some buttons | Allowlist company.com |
| Privacy Badger | Blocks auth cookies | Disable for site |
| Ghostery | Blocks tracking, breaks SSO | Allowlist |
| HTTPS Everywhere | Forces HTTPS on dev/local | Disable for localhost |
| LastPass / Bitwarden | Auto-fills wrong fields | Exclude URL pattern |
| Grammarly | Interferes with rich text editors | Disable in editor |
| Dark Reader | Breaks CSS variables, charts | Disable for site |
| AdBlock Plus | Hides "Upgrade" banners | Allowlist |

**Test**: Incognito/Private mode (extensions disabled by default) → if works, it's an extension.

#### Browser-Specific Quirks
**Safari (macOS/iOS)**:
- Intelligent Tracking Prevention (ITP) deletes cookies after 7 days
- Fix: Use "Remember me" (30-day token in localStorage)
- IndexedDB may be cleared; app uses fallback

**Firefox**:
- Enhanced Tracking Protection (Strict) blocks our auth cookies
- Fix: Shield icon → "Turn off for this site"
- Container tabs isolate cookies (expected behavior)

**Chrome**:
- Third-party cookie phaseout (2024+) - we use first-party only
- Memory saver tabs discard → reloads on revisit
- Fix: Settings → Performance → Keep these sites active

**Edge**:
- Same as Chrome (Chromium-based)
- "Sleeping tabs" after 2h → reloads

---

### 7. Mobile-Specific Issues

#### Push Notifications Not Working
**iOS**:
- Settings → Notifications → Company App → Allow Notifications ON
- Settings → Focus → Do Not Disturb → OFF or allow Company App
- App Settings → Notifications → Enable all categories
- Reinstall app (resets push token)

**Android**:
- Settings → Apps → Company App → Notifications → All ON
- Battery optimization: Settings → Battery → App optimization → Company App → Don't optimize
- Background data: Settings → Apps → Company App → Mobile data → Background data ON
- Do Not Disturb: Allow exceptions for Company App

**Both**:
- In-app: Settings → Notifications → Check all toggles
- Test: Settings → Notifications → "Send Test Notification"
- Token refresh: Log out → Log in (generates new push token)

#### Offline Mode Issues
**Web**: Enable in Settings → Offline → "Available offline" for specific projects
- Requires Service Worker (HTTPS only)
- Storage quota: Browser dependent (usually 50-500 MB)
- Sync on reconnect: Automatic, shows pending count

**Mobile**: Always on for cached data
- View/edit cached items offline
- Changes queue → sync on connection
- Conflict handling: See "Files not syncing"

---

### 8. Diagnostic Information to Collect

When contacting support, include:

**Always**:
- Browser + version (Chrome 120.0.6099.129)
- OS + version (macOS 14.2, Windows 11 23H2)
- Plan type (Free/Starter/Pro/Business/Enterprise)
- Time of issue (with timezone)
- Steps to reproduce (numbered list)
- Screenshot/video of error

**If applicable**:
- Network tab HAR file (DevTools → Network → Export HAR)
- Console errors (DevTools → Console → Save as...)
- API request/response (copy from Network tab)
- Mobile: App version (Settings → About), device model
- Error ID (shown on error pages: `ERR-XXXXXXXX`)

**HAR file capture**:
1. Open DevTools (F12)
2. Network tab → Check "Preserve log"
3. Reproduce issue
4. Right-click any request → "Save all as HAR with content"
5. Attach to support ticket (sanitizes auth headers automatically)

---

## Status Page & Incident Communication

### status.company.com
- Real-time system status
- Incident history (90 days)
- Scheduled maintenance calendar
- RSS/Atom feed for monitoring
- Webhook for custom alerts
- Status badge for your dashboard

### Incident Severity Levels
| Level | Name | Response | Communication |
|-------|------|----------|---------------|
| SEV-1 | Critical Outage | <15 min | Status page, email, SMS (Enterprise), social |
| SEV-2 | Major Degradation | <30 min | Status page, email (affected users) |
| SEV-3 | Minor Issue | <2 hours | Status page, in-app banner |
| SEV-4 | Cosmetic/Low | <24 hours | In-app banner only |

### Maintenance Windows
- **Weekly**: Sundays 2:00-4:00 AM UTC (low traffic)
- **Monthly**: First Sunday 12:00-4:00 AM UTC (larger updates)
- **Emergency**: As needed, <1 hour notice
- **Notification**: 7 days email, 24h in-app, status page

---

## Escalation Paths

### Standard Support (All Plans)
1. **Self-service**: Help center, community forum
2. **Chat/Email**: Support team (SLA per plan)
3. **Senior Support**: Request escalation in chat/email
4. **Engineering**: Senior support escalates if bug confirmed

### Enterprise Escalation
1. **CSM** (Customer Success Manager) - Primary contact
2. **Technical Account Manager** - For technical issues
3. **Engineering Lead** - For SEV-1/2, via CSM
4. **VP Engineering** - For critical business impact
5. **Executive** - For contract/SLA disputes

**Emergency Hotline** (Enterprise only): +1-800-XXX-XXXX ext 9
- 24/7/365 for SEV-1 only
- Direct to on-call engineer

---

## Useful Commands & Tools

### Browser DevTools Shortcuts
| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open DevTools | F12 / Ctrl+Shift+I | Cmd+Opt+I |
| Console | Ctrl+Shift+J | Cmd+Opt+J |
| Network | Ctrl+Shift+E | Cmd+Opt+E |
| Application (Storage) | Ctrl+Shift+A | Cmd+Opt+A |
| Device Toolbar | Ctrl+Shift+M | Cmd+Shift+M |
| Clear Cache (hard reload) | Ctrl+Shift+R | Cmd+Shift+R |

### Command Line Health Checks
```bash
# DNS resolution
nslookup api.company.com
dig api.company.com

# TLS certificate
openssl s_client -connect api.company.com:443 -servername api.company.com < /dev/null

# Latency
ping api.company.com
traceroute api.company.com

# HTTP response
curl -I https://api.company.com/health
curl -w "\nDNS: %{time_namelookup}\nConnect: %{time_connect}\nTTFB: %{time_starttransfer}\nTotal: %{time_total}\n" -o /dev/null -s https://api.company.com/health
```

### Log Locations (Desktop App)
| OS | Path |
|----|------|
| Windows | `%APPDATA%\CompanyApp\logs\` |
| macOS | `~/Library/Logs/CompanyApp/` |
| Linux | `~/.config/CompanyApp/logs/` |

---

## Contacting Technical Support

**Before contacting**: Try self-service → Help Center → Search error message

**Channels**:
| Channel | Availability | Best For |
|---------|--------------|----------|
| **Live Chat** | Mon-Fri 6am-10pm UTC, Sat-Sun 8am-8pm UTC | Quick questions, config help |
| **Email** | 24/7 | Complex issues, logs, screenshots |
| **Phone** | Pro+ Mon-Fri 9am-6pm PST | Urgent, SEV-2+ |
| **Community** | 24/7 | Feature requests, peer help |
| **Status Page** | Real-time | Outage confirmation |

**Email Template**:
```
Subject: [Plan] Brief Issue Summary - ERR-XXXXXXXX

Plan: Pro
Browser: Chrome 120.0.6099.129 / macOS 14.2
Time: 2026-10-05 14:30 UTC
Error ID: ERR-XXXXXXXX (if shown)

Steps to reproduce:
1. Go to Dashboard
2. Click "Export Data"
3. Select CSV, Date Range: Last 30 days
4. Click Export
5. Error appears after 30s

Expected: CSV download starts
Actual: "Network Error" toast, no file

Attached: HAR file, screenshot, console logs
```

---

## Version-Specific Known Issues

### Current Version: 4.12.0 (Released 2026-09-15)
**Fixed in this version**:
- Memory leak in dashboard charts (affected Pro+ with >50 projects)
- SSO logout loop with Okta (specific SAML config)
- Mobile app crash on iOS 17.2 when taking photo
- API 500 on bulk delete >1000 items

**Known Issues (to be fixed in 4.13.0)**:
- Safari 17: Drag-drop in Kanban board fails intermittently
- Firefox: Dark mode flashes light on navigation
- Excel export: Dates off by 1 day in some timezones
- Webhook retries: Duplicate events possible during maintenance

**Workarounds in Help Center**: help.company.com/known-issues

---

## Security Incident Response

### If You Suspect Compromise
1. **Immediately**: Change password, revoke all sessions (Settings → Security)
2. **Enable 2FA** if not already enabled
3. **Check** Audit Logs for unauthorized access
4. **Rotate** all API keys (Settings → Developers)
5. **Contact** security@company.com with details
6. **Monitor** for unusual activity

### Phishing Awareness
**We will NEVER**:
- Ask for password via email/chat
- Send login links unsolicited
- Request 2FA codes
- Ask for payment info via email

**Verify emails**:
- From: @company.com only (not @company-support.com, etc.)
- Links: Hover to verify company.com domain
- Urgency: We don't threaten immediate account closure

**Report phishing**: Forward to phishing@company.com

---

*Last Updated: October 2026 | Version 4.12*
*Next Review: Monthly with each release*
*Document Owner: Platform Engineering Team*
*Technical Accuracy Verified: 2026-10-05*