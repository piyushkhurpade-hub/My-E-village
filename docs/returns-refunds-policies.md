# Returns, Refunds & Policies Guide

## Money-Back Guarantee

### Eligibility
All new subscriptions include a money-back guarantee from the date of **first payment**:

| Plan | Guarantee Period | Refund Type |
|------|------------------|-------------|
| **Monthly** (Starter, Pro, Business) | 7 calendar days | Full refund to original payment method |
| **Annual** (Starter, Pro, Business) | 30 calendar days | Full refund to original payment method |
| **Enterprise** | Per contract (typically 60-90 days) | Per contract terms |
| **Free** | N/A | N/A (no payment) |
| **Add-ons** | Same as base plan | Prorated if within window |

### Conditions
- **First subscription only**: Not eligible for renewals, upgrades, or reactivations
- **One per customer**: Lifetime limit per account/entity
- **Good faith use**: Must have genuinely tried the service
- **No abuse**: Pattern of subscribe/refund/subscribe may be declined
- **Data export**: Request export before refund (Settings → Privacy → Export Data)

### Request Process
1. **Self-service** (within window): Settings → Billing → Request Refund
2. **Email**: refunds@company.com with subject "Refund Request - [Invoice #]"
3. **Chat**: Ask support agent for refund

**Required info**: Invoice number, reason (optional but helps us improve)
**Processing**: 1-2 business days approval, 5-10 business days to appear on statement
**Confirmation**: Email sent when processed

### What's NOT Refundable
- Renewal charges (auto-renew on anniversary)
- Upgrade proration charges (immediate feature access)
- Overage fees (API calls, storage, users beyond plan limits)
- Professional services (onboarding, training, custom development)
- Domain purchases, SSL certificates, third-party marketplace items
- Fees already paid to payment processors (rare, disclosed upfront)

---

## Subscription Cancellation

### Self-Service Cancellation
**Available anytime**: Settings → Billing → Subscription → Cancel Plan

**What happens**:
- **Access continues** until end of current billing period
- **No partial refund** for unused time (except money-back window)
- **Data retained** per retention policy (see below)
- **Can reactivate** anytime before period ends (one click)
- **Downgrade to Free** automatic after period ends

### Cancellation by Plan Type

| Plan | Cancellation Effect | Data Retention |
|------|---------------------|----------------|
| **Monthly** | End of current month | 30 days grace, then purge |
| **Annual** | End of current year | 30 days grace, then purge |
| **Enterprise** | Per contract (usually 30-90 day notice) | Per contract (typically 90 days) |
| **Trial** | Immediate (no charge) | 7 days after trial ends |

### Pausing Instead of Cancelling (Seasonal Businesses)
**Available**: Pro, Business, Enterprise
**Duration**: Up to 3 months per 12-month period
**Cost**: $5/month maintenance fee (covers data retention, security)
**Features**: No access during pause; read-only export available
**Auto-resume**: Automatically reactivates after pause period
**Request**: Chat support or billing@company.com (not self-service)

---

## Refunds for Specific Scenarios

### Failed Service / Extended Downtime
**SLA Credits** (automatic, no request needed):

| Plan | Monthly Uptime | Credit for < SLA |
|------|----------------|------------------|
| Free | Best effort | None |
| Starter | 99.5% | 10% monthly fee per 0.1% below |
| Pro | 99.9% | 15% monthly fee per 0.1% below |
| Business | 99.95% | 20% monthly fee per 0.1% below |
| Enterprise | 99.99% | Per contract (typically 25-50%) |

**Max credit**: 100% of monthly fee per incident
**Applied as**: Account credit for next invoice
**Notification**: Email within 24h of incident resolution

### Billing Errors
**Double charges, wrong amount, unauthorized charges**:
- Contact billing@company.com within 60 days
- Provide: Invoice #, screenshots, bank statement (redacted)
- Resolution: 3-5 business days
- Refund to original payment method

### Price Changes
**Grandfathering**: Existing customers keep current price for 12 months after increase notice
**Notification**: 60 days email + in-app banner
**Options**: Accept new price, downgrade, cancel (no penalty during notice period)

### Currency Fluctuations
- Prices set in USD, converted at billing time
- No refunds for exchange rate changes
- Annual plans lock USD price for 12 months

---

## Data Retention & Deletion

### After Cancellation / Non-Payment

| Phase | Timeline | Access | Action |
|-------|----------|--------|--------|
| **Grace Period** | Days 1-7 | Full (with banner) | Payment retry attempts |
| **Suspended** | Days 8-37 | Read-only, export only | Data intact, no writes |
| **Deletion Queue** | Days 38-67 | None | Scheduled for purge |
| **Purged** | Day 68+ | None | Irrecoverable |

### Data Export Before Deletion
**Self-service**: Settings → Privacy → Export Data
- Generates complete ZIP (JSON + CSV + files)
- Ready in 1-24 hours (email notification)
- Download link valid 7 days
- Includes: Projects, files, comments, analytics, settings

**Bulk/Enterprise**: Contact support for assisted export

### Data Deletion Request (GDPR/CCPA)
**Right to Erasure**: privacy@company.com
**Process**:
1. Verify identity (email + one more factor)
2. Confirm scope (all data or specific categories)
3. Process within 30 days (GDPR) / 45 days (CCPA)
4. Confirmation email with deletion certificate

**Exceptions** (legal retention):
- Billing records: 7 years (tax law)
- Audit logs: 1-7 years (plan dependent)
- Security logs: 1 year
- Legal holds: Until released

---

## Service-Specific Policies

### Professional Services (Onboarding, Training, Consulting)
- **Scope**: Defined in Statement of Work (SoW)
- **Payment**: 50% upfront, 50% on completion (or per milestone)
- **Cancellation**: 
  - >14 days before start: Full refund
  - 7-14 days: 50% refund
  - <7 days: No refund (resource allocation)
- **Rescheduling**: >48h notice, no fee; <48h: 25% fee
- **Deliverables**: Ownership transfers on full payment

### Marketplace / Third-Party Add-ons
- **Purchases**: Subject to vendor's refund policy
- **Company role**: Platform only, not party to transaction
- **Disputes**: Contact vendor directly via marketplace messaging
- **Platform fee**: Non-refundable (5-15% depending on volume)

### Domain Registration / SSL Certificates
- **Domains**: Non-refundable after registration (registry policy)
- **SSL**: Refundable within 30 days if not issued
- **Transfers**: 60-day lock after registration/transfer (ICANN)

### API Overage Charges
- **Notification**: Email at 80%, 95%, 100% of limit
- **Auto-upgrade**: Optional (Settings → Billing → Auto-upgrade)
- **Hard limit**: Requests fail at 100% (429 response)
- **Refunds**: Not provided for overages (usage-based)

---

## Upgrade / Downgrade Policies

### Upgrades (Immediate Effect)
- **Prorated charge**: For remainder of billing cycle
- **New limits**: Apply immediately
- **New features**: Unlocked instantly
- **Invoice**: Generated within 24 hours
- **No downgrade** until next cycle (prevents cycling)

### Downgrades (Next Cycle Effect)
- **Scheduled**: Takes effect at next billing date
- **Current features**: Remain until then
- **Usage validation**: Warns if current usage exceeds new limits
- **Grace period**: 7 days after downgrade to reduce usage
- **Forced downgrade**: If usage still exceeds after grace, auto-upgrade

### Plan Comparison for Changes
| Change | Timing | Proration | Feature Access |
|--------|--------|-----------|----------------|
| Upgrade | Immediate | Charge for remainder | New features now |
| Downgrade | Next cycle | Credit for remainder | Old features until cycle end |
| Monthly → Annual | Immediate | Credit monthly, charge annual | Annual features now |
| Annual → Monthly | Next anniversary | No credit | Monthly features at anniversary |

---

## Enterprise Contract Terms

### Standard Enterprise Agreement
**Term**: 1-5 years (multi-year discounts: 2yr 5%, 3yr 10%, 5yr 15%)
**Payment**: Annual upfront, Net 30/45/60 on PO (with credit approval)
**Auto-renewal**: Yes, unless 60-day written notice
**Price lock**: Fixed for term (no increases)

### SLA Commitments
| Metric | Target | Measurement | Remedy |
|--------|--------|-------------|--------|
| Uptime | 99.99% | Monthly | Service credits (see table) |
| API Latency (p95) | <200ms | Continuous | Credit if >500ms sustained 1hr |
| Support Response (Critical) | <15 min | Per ticket | Escalation to VP Eng |
| Support Response (High) | <1 hour | Per ticket | CSM notification |
| Data Durability | 99.999999999% | Annual audit | Contractual penalty |
| RPO (Recovery Point) | <1 hour | Tested quarterly | Credit if exceeded |
| RTO (Recovery Time) | <4 hours | Tested quarterly | Credit if exceeded |

### Data Residency Options
- **US** (Virginia, Oregon) - Default
- **EU** (Frankfurt, Ireland) - GDPR optimized
- **APAC** (Singapore, Sydney, Tokyo) - Low latency Asia
- **Canada** (Toronto, Montreal) - Data sovereignty
- **Custom**: Dedicated region (Enterprise 500+ users)

### Compliance & Certifications
- SOC 2 Type II (annual)
- ISO 27001 (certified)
- GDPR (DPA included)
- HIPAA (BAA available)
- PCI DSS SAQ D (for payment handling)
- FedRAMP Moderate (in progress, 2027 target)
- CCPA/CPRA compliant

### Security Addendums
- Data Processing Addendum (standard)
- HIPAA BAA (on request)
- Standard Contractual Clauses (EU-US transfers)
- Custom security questionnaires (completed within 5 days)
- Penetration test results (summary shared, full under NDA)

---

## Dispute Resolution

### Billing Disputes
1. **Contact billing@company.com** (first attempt)
2. **Escalate to billing manager** (reply to thread with "ESCALATE")
3. **Formal dispute**: Certified letter to Legal Dept at HQ
4. **Mediation**: JAMS/AAA (costs split 50/50)
5. **Arbitration**: Binding, Santa Clara County, CA (per Terms)

### Service Disputes
- Document in writing with evidence
- CSM/Enterprise: Direct escalation path
- SLA credits: Automatic, no dispute needed
- Other: Good faith negotiation → Mediation → Arbitration

### Chargebacks
**We strongly discourage chargebacks** - they trigger:
- Account suspension during investigation
- $15-25 fee per chargeback (passed from processor)
- Potential termination for repeated chargebacks
- Loss of money-back guarantee eligibility

**Instead**: Contact billing@company.com - we resolve 99% within 48h

---

## Regional Policy Variations

### European Union (GDPR)
- **14-day cooling-off period** for digital services (Directive 2011/83/EU)
- **Right to withdraw** without reason within 14 days
- **Refund**: Within 14 days of withdrawal notice
- **Digital content exception**: Waived if download/access started with consent
- **Our implementation**: Money-back guarantee exceeds this (30 days annual)

### United Kingdom
- Same as EU (retained law)
- **Consumer Rights Act 2015**: Digital content must be as described, fit for purpose
- **Refunds**: Full refund if not as described (no time limit for this right)

### Australia (ACL)
- **Consumer Guarantees**: Acceptable quality, fit for purpose
- **Major failure**: Right to refund or replacement (no time limit)
- **Minor failure**: Repair or partial refund
- **Our policy**: Exceeds minimum guarantees

### Canada
- **Provincial laws vary** (Ontario CPA, BC BPCPA, Quebec CPA)
- **Cooling-off**: Varies by province (10-30 days for direct sales)
- **Our policy**: 30-day annual guarantee covers all

### India
- **Consumer Protection Act 2019**: Applies to digital services
- **Refunds**: Within 14 days for deficient service
- **GST**: Refunded on pro-rata basis
- **Our policy**: Compliant with 30-day annual guarantee

### Brazil (CDC)
- **Right of regret (arrependimento)**: 7 days for distance contracts
- **Full refund** including shipping (not applicable here)
- **Our policy**: 30-day annual exceeds 7-day minimum

### California (CCPA/CPRA)
- **Right to delete**: Verified requests within 45 days
- **Right to know**: Data categories collected
- **Right to opt-out**: Sale of personal info (we don't sell)
- **Non-discrimination**: Can't deny service for exercising rights

---

## Policy Change Notifications

### How We Communicate Changes
- **Email**: Primary (to billing email on file)
- **In-app banner**: 30 days before effective
- **Blog post**: For significant changes
- **API changelog**: For developer-facing changes

### Notice Periods
| Change Type | Notice | Opt-out |
|-------------|--------|---------|
| Price increase | 60 days | Cancel without penalty during notice |
| Feature removal | 90 days | Export data, cancel |
| Policy update | 30 days | Accept or cancel |
| SLA change | 90 days | Enterprise: contract amendment |
| Data processing | 30 days | DPA amendment |

### Version Control
All policies versioned at: policies.company.com
- Current version linked in footer of all emails
- Changelog with diff view
- RSS feed for policy changes

---

## Quick Reference: Refund Eligibility Checklist

**✅ Likely Approved**:
- [ ] Within money-back window (7d monthly / 30d annual)
- [ ] First subscription for this account
- [ ] Requested via self-service or email
- [ ] No prior refunds for this entity

**⚠️ Case-by-Case**:
- [ ] Just outside window (1-3 days) - ask for exception
- [ ] Service issues documented (downtime, bugs)
- [ ] Billing error (wrong amount, double charge)
- [ ] Upgrade immediately downgraded (within 24h)

**❌ Typically Declined**:
- [ ] Renewal charge (not first payment)
- [ ] Outside window (>30 days annual, >7 days monthly)
- [ ] Previous refund on this account
- [ ] Overage fees (API, storage, users)
- [ ] Professional services rendered
- [ ] Domain/SSL purchases
- [ ] Chargeback filed instead of request

---

## Contact Information for Policy Questions

| Topic | Email | Phone | SLA |
|-------|-------|-------|-----|
| **Refunds** | refunds@company.com | +1-800-XXX-XXXX ext 3 | 48h |
| **Cancellations** | cancellations@company.com | Same | 24h |
| **Billing Errors** | billing@company.com | Same | 4h |
| **Data Deletion** | privacy@company.com | N/A | 30d (GDPR) |
| **Enterprise Contracts** | legal@company.com | +1-800-XXX-XXXX ext 5 | 5 days |
| **SLA Credits** | sla@company.com | N/A | Auto-applied |
| **Chargebacks** | chargebacks@company.com | N/A | 10 days |
| **Policy Questions** | policy@company.com | N/A | 5 days |

**Mailing Address**:
TechCorp Solutions Inc.
Legal & Compliance Department
100 Innovation Drive
San Francisco, CA 94105
USA

---

## Frequently Asked Policy Questions

**Q: Can I get a refund if I forgot to cancel before renewal?**
A: Renewals are not eligible for money-back guarantee. However, if you contact us within 7 days of renewal, we may offer a one-time courtesy refund (not guaranteed).

**Q: I upgraded by accident. Can I reverse it?**
A: Yes, if within 24 hours. Contact support immediately. We'll downgrade and credit the prorated difference.

**Q: My trial ended and I was charged. Can I get a refund?**
A: Trial conversions are considered first payments. 7-day (monthly) or 30-day (annual) money-back applies from charge date.

**Q: Can I transfer my remaining subscription time to another account?**
A: Not directly. Cancel current (access continues), new account subscribes. Contact billing for coordination.

**Q: Do you offer prorated refunds if I cancel mid-cycle?**
A: No, except within money-back window. Access continues until period ends.

**Q: What if my credit card expired and payment failed?**
A: 7-day grace period with retries. Then suspended (read-only 30 days). Update payment to restore.

**Q: Can I pause my subscription for vacation?**
A: Pro+ plans: Yes, up to 3 months/year for $5/month. Contact support.

**Q: Are fees refundable if I dispute a charge with my bank?**
A: Chargebacks incur $15-25 fee and suspend account. Contact us first - we resolve faster.

**Q: Does the money-back guarantee apply to add-ons?**
A: Yes, same window as base plan. Prorated if base plan refunded.

**Q: What happens to my custom domain if I cancel?**
A: Domain remains yours (registered to you). DNS points to us until you change it. We release it from our system.

---

*Last Updated: October 2026 | Version 2.8*
*Next Review: January 2027*
*Document Owner: Legal & Billing Operations*
*Legal Review: Quarterly*
*Approved By: General Counsel*