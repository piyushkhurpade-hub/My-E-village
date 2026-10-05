# Account & Billing Support Guide

## Subscription Plans & Pricing

### Plan Comparison (USD, billed annually)

| Feature | Free | Starter | Pro | Business | Enterprise |
|---------|------|---------|-----|----------|------------|
| **Monthly Price** | $0 | $12/mo | $29/mo | $79/mo | Custom |
| **Annual Price** | $0 | $120/yr | $290/yr | $790/yr | Custom |
| **Users** | 1 | 5 | 25 | 100 | Unlimited |
| **Storage** | 2 GB | 50 GB | 500 GB | 2 TB | Unlimited |
| **Projects** | 3 | 25 | 200 | 1,000 | Unlimited |
| **API Calls/mo** | 1,000 | 50,000 | 500,000 | 5M | Custom |
| **Team Collaboration** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Advanced Analytics** | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Custom Integrations** | ❌ | ❌ | 5 | 20 | Unlimited |
| **SSO (SAML/OIDC)** | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Audit Logs** | ❌ | ❌ | 30 days | 1 year | 7 years |
| **Priority Support** | Community | Email | Chat + Email | Phone + Chat | Dedicated CSM |
| **SLA** | None | 99.5% | 99.9% | 99.95% | 99.99% |
| **Custom Contract** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **On-premise Option** | ❌ | ❌ | ❌ | ❌ | ✅ |

### Regional Pricing (Annual)
- **US/Canada**: Listed above
- **EU/UK**: €10/€24/€65/€115 + VAT
- **Australia/NZ**: AUD 18/44/119/215 + GST
- **India**: ₹800/₹2,000/₹5,500/₹10,000 + GST
- **Brazil**: BRL 60/150/400/750 + taxes
- **Japan**: ¥1,500/¥3,500/¥9,500/¥17,000 + tax

---

## Billing Cycle & Payments

### Billing Dates
- **Monthly plans**: Charged on the same date each month (signup date)
- **Annual plans**: Charged on signup anniversary
- **Invoices generated**: 24 hours before charge
- **Grace period**: 7 days for failed payments before service suspension
- **Proration**: Immediate for upgrades, next cycle for downgrades

### Payment Methods by Region
| Region | Cards | Bank Transfer | Digital Wallets | Local Methods |
|--------|-------|---------------|-----------------|---------------|
| US/CA | ✅ | ✅ (Annual) | Apple/Google Pay | - |
| EU | ✅ | ✅ (SEPA) | Apple/Google Pay | iDEAL, Bancontact, Sofort |
| UK | ✅ | ✅ (BACS) | Apple/Google Pay | - |
| AU/NZ | ✅ | ✅ (BPAY) | Apple/Google Pay | - |
| India | ✅ | ✅ (NEFT/RTGS/UPI) | Google Pay, PhonePe | UPI, NetBanking |
| Brazil | ✅ | ✅ (PIX/Boleto) | Google Pay | PIX, Boleto |
| Japan | ✅ | ✅ (Annual) | Apple Pay | Konbini |

### Failed Payment Recovery
1. **Attempt 1**: Immediate retry
2. **Attempt 2**: 24 hours later + email notification
3. **Attempt 3**: 72 hours later + SMS (if phone on file)
4. **Day 7**: Account suspended, data retained 30 days
5. **Day 37**: Data purged per retention policy

Update payment method anytime at: Settings → Billing → Payment Methods

---

## Invoicing & Taxes

### Invoice Details Included
- Company legal name & address
- Your billing name & address
- VAT/GST/Tax ID (if provided)
- Invoice number & date
- Line items with descriptions
- Subtotal, tax, total in your currency
- Payment method & transaction ID
- Download as PDF from Billing History

### Tax Handling
- **US**: Sales tax applied based on ship-to address (nexus states)
- **EU**: VAT reverse charge for B2B with valid VAT ID; consumer VAT by country
- **UK**: 20% VAT for B2C; reverse charge for B2B with UK VAT number
- **Australia**: 10% GST for all
- **India**: 18% GST (CGST+SGST/IGST) with GSTIN validation
- **Canada**: GST/HST/PST by province
- **Other**: Local tax rates applied automatically

**Provide tax ID**: Settings → Billing → Tax Information → Enter VAT/GST/Tax ID → Auto-validated via VIES/IRS/GSTN

### Invoice Customization
- Add PO number: Settings → Billing → Default PO Number
- Custom billing email: Settings → Billing → Invoice Recipients
- Multiple recipients: Add up to 5 email addresses
- Language: 12 languages supported (EN, ES, FR, DE, PT, IT, NL, JA, KO, ZH, HI, AR)

---

## Subscription Management

### Upgrading Your Plan
**Immediate effect**: 
- New limits apply instantly
- Prorated charge for remainder of cycle
- New invoice generated
- Features unlocked immediately

**Process**: Settings → Billing → Change Plan → Select Plan → Confirm

### Downgrading Your Plan
**Next-cycle effect**:
- Current plan features remain until cycle ends
- No prorated refund for unused time
- Downgrade scheduled for next billing date
- Warning if current usage exceeds new limits

**Process**: Settings → Billing → Change Plan → Select Lower Plan → Confirm

### Cancelling Subscription
**Self-service**: Settings → Billing → Subscription → Cancel Plan
- Access continues until period ends
- Export data before cancellation (Settings → Privacy → Export)
- Reactivate anytime before period ends
- No partial refunds (except money-back window)

**Money-back Guarantee**:
- Monthly: 7 days from charge
- Annual: 30 days from charge
- Enterprise: Per contract (typically 60-90 days)
- Request via: Settings → Billing → Request Refund or email billing@company.com

### Pausing Subscription (Seasonal Businesses)
- Available for Pro+ plans
- Maximum 3 months per 12-month period
- $5/month maintenance fee (covers data retention)
- No feature access during pause
- Auto-resumes after pause period
- Request via support chat or billing@company.com

---

## Team & User Management

### Adding Team Members
**Starter**: Up to 5 users (including owner)
**Pro**: Up to 25 users
**Business**: Up to 100 users
**Enterprise**: Unlimited

**Process**: Settings → Team → Invite Members → Enter emails → Assign roles → Send invites
- Invites expire in 7 days
- Pending invites count toward limit
- Bulk invite via CSV (Pro+)
- SCIM provisioning (Business+)

### User Roles & Permissions

| Permission | Owner | Admin | Member | Viewer | Guest |
|------------|-------|-------|--------|--------|-------|
| Billing access | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage users | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage integrations | ✅ | ✅ | ❌ | ❌ | ❌ |
| Create projects | ✅ | ✅ | ✅ | ❌ | ❌ |
| Edit all projects | ✅ | ✅ | Own only | View only | Invited only |
| Delete projects | ✅ | ✅ | Own only | ❌ | ❌ |
| View analytics | ✅ | ✅ | ✅ | ✅ | ❌ |
| Export data | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage API keys | ✅ | ✅ | ❌ | ❌ | ❌ |

### Changing User Roles
Settings → Team → Click user → Change Role → Select new role → Confirm
- Owner role: Only one, transferable (Settings → Team → Transfer Ownership)
- Role changes take effect immediately
- User notified via email

### Removing Team Members
Settings → Team → Click user → Remove → Confirm
- **Data ownership**: Member's content transfers to remover
- **API keys**: Member's keys revoked immediately
- **Sessions**: Active sessions terminated
- **Re-invite**: Can be re-added within 30 days with data restored

---

## Enterprise Features

### SSO Configuration (SAML 2.0 / OIDC)
**Supported IdPs**: Okta, Azure AD, Google Workspace, OneLogin, Auth0, PingIdentity, Custom SAML/OIDC

**Setup Process**:
1. Settings → Security → SSO → Configure
2. Enter IdP metadata URL or upload XML
3. Map attributes (email, first_name, last_name, groups)
4. Test with test user
5. Enable for organization
6. Optional: Enforce SSO (disable password login)

**JIT Provisioning**: Auto-create users on first login
**Group Mapping**: Map IdP groups to roles automatically
**Session Duration**: Configurable (1hr - 30 days)

### Audit Logs
**Retention**: Starter: N/A | Pro: 30 days | Business: 1 year | Enterprise: 7 years

**Logged Events**:
- User login/logout (IP, device, location)
- Permission changes
- Data exports/deletes
- Configuration changes
- API key creation/usage
- Failed login attempts
- SSO events

**Access**: Settings → Security → Audit Logs
**Export**: CSV/JSON, filtered by date/user/action
**SIEM Integration**: Splunk, Datadog, Elastic, Sumo Logic (Enterprise)

### Custom Contracts & Procurement
**Enterprise includes**:
- Custom MSA/DPAs
- Custom SLA with penalties
- Volume discounts (10%+ at 500+ users)
- Multi-year pricing lock (2-5 years)
- Purchase order billing (Net 30/45/60)
- Dedicated Customer Success Manager
- Quarterly business reviews
- Custom onboarding & training
- Penetration test results sharing
- SOC 2 Type II report access
- Data processing addendum (GDPR Art. 28)
- HIPAA BAA (if applicable)
- Custom data residency (US, EU, APAC, CA)

**Contact**: enterprise@company.com or schedule at company.com/enterprise

---

## Common Billing Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Charge declined | Expired card, insufficient funds, bank block | Update payment method; contact bank |
| Double charged | Retry logic, duplicate subscription | Contact billing@company.com for refund |
| Wrong amount charged | Proration, tax change, currency fluctuation | Check invoice breakdown; contact support |
| Invoice missing | Email filtered, wrong billing email | Check spam; verify billing email in settings |
| VAT not removed | Invalid/expired VAT ID | Update valid VAT ID in Tax Settings |
| Can't downgrade | Usage exceeds lower plan limits | Reduce usage or wait for cycle end |
| Cancellation not processed | Pending payment, within contract term | Resolve payment; check contract terms |
| Team invite not sent | Limit reached, email typo | Check limit; verify email; resend |
| SSO not working | Metadata expired, attribute mismatch | Update IdP metadata; check attribute mapping |

---

## Billing Support Contacts

**General Billing**: billing@company.com | <4hr response
**Enterprise Billing**: enterprise-billing@company.com | <1hr response
**Invoice Questions**: invoices@company.com
**Tax/VAT Issues**: tax@company.com
**Refund Requests**: refunds@company.com (include invoice #)
**Payment Failures**: payments@company.com
**Procurement/POs**: procurement@company.com

**Phone (Pro+)**: +1-800-XXX-XXXX ext 2 (Mon-Fri 9am-6pm PST)
**Live Chat**: In-app billing widget (Pro+)

**Mailing Address for Checks/POs**:
TechCorp Solutions Inc.
Accounts Receivable
100 Innovation Drive
San Francisco, CA 94105
USA

**Wire Transfer Details** (Annual Enterprise only):
Bank: Silicon Valley Bank
Account: TechCorp Solutions Inc.
Routing: 121140399
Account: 3300XXXXXX
SWIFT: SVBKUS6S
Reference: Invoice # + Company Name

---

## FAQ - Billing Specific

**Q: Can I pay annually for monthly plan prices?**
A: No, annual billing requires annual plan commitment. Monthly plans are month-to-month only.

**Q: Do you offer nonprofit/educational discounts?**
A: Yes! 50% off Pro/Business for verified nonprofits (501c3/equivalent) and educational institutions. Apply at company.com/nonprofit with documentation.

**Q: Can I get a custom quote for my team?**
A: For 100+ users, contact sales@company.com for custom pricing, contract terms, and volume discounts.

**Q: What happens to my data if I don't renew?**
A: 30-day grace period with read-only access. After 30 days, data scheduled for deletion. Export anytime during grace period.

**Q: Can I transfer my subscription to another account?**
A: Contact billing@company.com. Requires verification of both account owners. One-time transfer allowed per 12 months.

**Q: Do you offer monthly billing for Enterprise?**
A: Enterprise is annual-only. Monthly available for Starter/Pro/Business.

**Q: How do I get a W-9 / tax form?**
A: Download from Settings → Billing → Tax Documents or request at tax@company.com

**Q: Can I prepay for multiple years?**
A: Enterprise: Yes, 2-5 year terms with additional discount (5-15%). Contact enterprise@company.com.

---

*Last Updated: October 2026 | Version 3.2*
*Next Review: January 2027*
*Document Owner: Billing Operations Team*