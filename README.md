# e-Village: Empowering Rural Communities through Digital Connectivity

## Project Overview

**e-Village** is a comprehensive Django-based digital platform designed to empower rural communities by providing digital access to essential services, information, and governance tools. The platform bridges the digital divide in rural India by offering a centralized portal for villagers, village officers, and Gram Panchayat administrators.

---

## Core Features & Modules

### 1. User Management & Authentication (`accounts`)
- **Custom User Model** extending Django's AbstractUser
- **Role-Based Access Control (RBAC)**:
  - **Villager** (default): Basic access to view notices, schemes, marketplace, agriculture tips, health services, education resources
  - **Staff/Officer**: Can publish notices, manage complaints, view analytics
  - **Village Admin (Gram Panchayat)**: Full administrative access, user management, system configuration
- **Profile Fields**: Phone number, village name, profile picture
- **Authentication**: Session-based with secure password validation
- **Redirects**: Role-appropriate dashboard routing after login

### 2. Village Dashboard (`dashboard`)
- **Village Profile Management**: Single configurable village profile
  - Name, district, state, population
  - Infrastructure counts (schools, hospitals, water connections)
  - Panchayat head details
  - About text and contact information
- **Home View**: Aggregated statistics and quick access cards

### 3. Community Notices (`notices`)
- **Categories**: General, Health Alerts, Education, Agriculture, Gram Sabha Meetings
- **Urgency Flag**: Mark critical notices as urgent
- **Publishing**: Officers and Admins can create notices
- **Display**: Chronological listing with category badges

### 4. Government Schemes (`schemes`)
- **Categories**: Agriculture/Farmers, Education/Scholarships, Pensions, Women Empowerment, Healthcare, Employment, Others
- **Detailed Information**: Eligibility criteria, required documents, application links, deadlines
- **Publication Tracking**: Auto-timestamped publishing
- **External Links**: Direct links to official government portals

### 5. Grievance Redressal (`complaints`)
- **Categories**: Roads, Water, Electricity, Sanitation, Internet, Health, Others
- **Status Workflow**: Pending Review → In Progress → Resolved
- **Rich Submission**: Title, description, photo evidence
- **Admin Response**: Officers/Admins can add resolution replies
- **User Tracking**: Linked to authenticated user with history

### 6. Agriculture Advisory (`agriculture`)
- **Tip Categories**: Crop Advisory, Weather Alerts, Fertilizer/Soil Guidance, Pest & Disease Control
- **Crop-Specific Content**: Optional crop tagging for targeted advice
- **Media Support**: Image uploads for visual guidance
- **Mandi Prices**: Real-time crop prices per quintal (INR) by market

### 7. Health Services (`health`)
- **Service Types**: Local Doctors/Clinics, Ambulance, PHC, Vaccination Camps, Emergency Helplines
- **Contact Information**: Phone numbers, operating hours, locations
- **Descriptions**: Specializations and services offered
- **24/7 Availability Flag**: Default timing for emergency services

### 8. Education & Skills (`education`)
- **Resource Categories**: Scholarships, Study Materials, Jobs/Training, Exam Prep, School Notices
- **Multi-format Content**: Text descriptions, external links, file uploads (PDFs)
- **Timely Updates**: Chronological listing for latest opportunities

### 9. Local Marketplace (`marketplace`)
- **Categories**: Fresh Produce, Dairy/Poultry, Handicrafts, Local Services (Tailoring, Repair), Others
- **Seller Verification**: Linked to authenticated village users
- **Listing Details**: Title, description, price (INR), contact number, image
- **Availability Toggle**: Sellers can mark items as available/unavailable

### 10. Document Guides (`documents`)
- **Certificate/Document Guidance**: Purpose, required documents, processing time
- **Official Links**: Direct links to government application portals
- **Standardized Format**: Consistent processing time display (default: 15 days)

---

## Technical Architecture

### Technology Stack
- **Framework**: Django 5.2.7
- **Database**: SQLite3 (development), PostgreSQL-ready for production
- **Web Server**: Gunicorn with WhiteNoise for static files
- **Deployment**: Heroku/Render/Railway compatible (Procfile included)
- **Python**: 3.12+

### Key Dependencies
```
Django==5.2.7
gunicorn==23.0.0
pillow==12.3.0 (image handling)
whitenoise==6.9.0 (static file serving)
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2026.2
```

### Project Structure
```
my_evillage/
├── my_evillage/          # Project settings & configuration
├── accounts/             # User management & authentication
├── dashboard/            # Village profile & home dashboard
├── notices/              # Community announcements
├── schemes/              # Government schemes directory
├── complaints/           # Grievance redressal system
├── agriculture/          # Farming advisory & market prices
├── health/               # Healthcare services directory
├── education/            # Educational resources & opportunities
├── marketplace/          # Local commerce platform
├── documents/            # Document application guides
├── templates/            # Base templates & shared components
├── static/               # CSS, JS, images
├── media/                # User uploads (images, documents)
├── manage.py             # Django CLI
├── requirements.txt      # Python dependencies
├── Procfile              # Process definition for deployment
├── build.sh              # Build script for CI/CD
└── .gitignore            # Git ignore rules
```

### Security Configuration
- **Environment-based Secrets**: SECRET_KEY, DEBUG, ALLOWED_HOSTS via environment variables
- **Production Hardening** (when DEBUG=False):
  - SECURE_BROWSER_XSS_FILTER
  - SECURE_CONTENT_TYPE_NOSNIFF
  - SESSION_COOKIE_SECURE
  - CSRF_COOKIE_SECURE
  - X_FRAME_OPTIONS = "DENY"
- **Password Validation**: Django's built-in validators (similarity, length, common, numeric)
- **CSRF Protection**: Enabled by default
- **Clickjacking Protection**: X-Frame-Options DENY

### Database Configuration
- **Default**: SQLite3 (`db.sqlite3` in BASE_DIR)
- **Production Ready**: Easily configurable for PostgreSQL/MySQL via DATABASES setting
- **Migrations**: All apps have initial migrations created

### Static & Media Files
- **Static**: `/static/` URL, collected to `staticfiles/` via `collectstatic`
- **Media**: `/media/` URL, stored in `media/` directory
- **WhiteNoise**: Compressed static file storage for production

### Internationalization
- **Language**: English (en-us)
- **Timezone**: Asia/Kolkata (IST)
- **I18N/L10N**: Enabled with timezone support

---

## User Policies & Guidelines

### Account Registration & Roles
1. **Self-Registration**: Villagers can register with username, email, password
2. **Role Assignment**: Default role is "Villager"; Officers/Admins assigned by existing Admins
3. **Profile Completion**: Phone number and village name encouraged for better service delivery
4. **Profile Pictures**: Optional, stored in media/profiles/

### Data Privacy & Protection
1. **Personal Data**: Username, email, phone, village name stored securely
2. **Complaint Data**: Linked to user account; visible to user and admins/officers
3. **Marketplace Listings**: Seller contact info visible to buyers
4. **No Third-Party Sharing**: Data not shared with external parties without consent
5. **Media Files**: User uploads stored locally; not publicly indexed

### Content Moderation Policies
1. **Notices**: Only Officers/Admins can publish; reviewed for relevance
2. **Complaints**: All submissions visible to admins; status updates communicated
3. **Marketplace**: Sellers responsible for accurate listings; admins can remove inappropriate content
4. **Agriculture/Health/Education**: Curated by officers; verified information preferred
5. **Schemes**: Official government information only; links to authentic portals

### Usage Policies

#### For Villagers (Citizens)
- **Access**: View all public information (notices, schemes, prices, services)
- **Participate**: Submit complaints, list marketplace items, apply for schemes
- **Responsibility**: Provide accurate information; use services responsibly
- **Support**: Contact village admin via dashboard contact info for assistance

#### For Officers (Staff)
- **Publishing**: Create notices, update schemes, add health/education/agriculture content
- **Management**: Review and update complaint statuses, respond to grievances
- **Moderation**: Monitor marketplace for policy violations
- **Accountability**: All actions logged with timestamps

#### For Village Admins (Gram Panchayat)
- **Full Control**: User role management, system configuration
- **Oversight**: Monitor all modules, view analytics
- **Communication**: Official contact point for village
- **Governance**: Ensure platform serves community needs

---

## Deployment & Operations

### Local Development Setup
```bash
# Clone repository
git clone <repository-url>
cd "My e-Village – Empowering Rural Communities through Digital Connectivity"

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

### Production Deployment
```bash
# Build script (build.sh)
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --no-input

# Run with Gunicorn (Procfile)
gunicorn my_evillage.wsgi:application --bind 0.0.0.0:$PORT
```

### Environment Variables Required
| Variable | Description | Default |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | (insecure default) |
| DEBUG | Debug mode (True/False) | False |
| ALLOWED_HOSTS | Comma-separated hosts | localhost,127.0.0.1 |

### Database Backup (Production)
```bash
# SQLite backup
cp db.sqlite3 backups/db_$(date +%Y%m%d).sqlite3

# PostgreSQL (when configured)
pg_dump -U user -d evillage > backup_$(date +%Y%m%d).sql
```

---

## API & Integration Notes

### Current State
- **No REST API**: Traditional Django template-rendered views
- **Session Authentication**: Browser-based, not token-based
- **Admin Interface**: Django Admin at `/admin/` for content management

### Future API Considerations
- Django REST Framework integration for mobile apps
- Token-based authentication for third-party integrations
- Webhook support for scheme/complaint updates

---

## Support & Maintenance

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Static files not loading | Run `python manage.py collectstatic`; check STATIC_ROOT |
| Media uploads failing | Verify MEDIA_ROOT permissions; check disk space |
| Migration errors | Check database connectivity; run `python manage.py makemigrations` |
| Login redirect loops | Verify LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL in settings |
| Permission denied | Check user role; verify is_officer/is_village_admin methods |

### Monitoring Recommendations
- **Application Logs**: Django logging to file/syslog
- **Error Tracking**: Sentry integration (add `sentry-sdk` to requirements)
- **Performance**: Monitor database query counts, response times
- **Uptime**: Health check endpoint for load balancers

### Update Procedures
1. Pull latest code
2. Install new dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Collect static: `python manage.py collectstatic --no-input`
5. Restart Gunicorn workers

---

## Contributing Guidelines

### Development Workflow
1. Fork repository
2. Create feature branch: `git checkout -b feature/description`
3. Write code with tests
4. Run tests: `python manage.py test`
5. Submit pull request

### Code Standards
- Follow PEP 8 (use `ruff` or `flake8`)
- Type hints encouraged for new code
- Docstrings for public methods
- Migrations for all model changes

### Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts agriculture marketplace
```

---

## License & Legal

### Usage Rights
- **Internal Use**: Gram Panchayat / Village Administration
- **Open Source Components**: Django, Pillow, Gunicorn, WhiteNoise (respective licenses)
- **Custom Code**: Proprietary to e-Village project

### Compliance
- **Data Localization**: SQLite/PostgreSQL on Indian servers recommended
- **Government Guidelines**: Aligns with Digital India, e-GramSwaraj initiatives
- **Accessibility**: Semantic HTML, alt text for images (WCAG 2.1 AA target)

---

## Contact & Support

### Project Maintainers
- **Primary Contact**: Village Admin (Gram Panchayat)
- **Technical Support**: Development team / System integrator
- **Official Email**: contact@evillage.gov.in (configured in VillageProfile)
- **Phone**: +91 9876543210 (configured in VillageProfile)

### Documentation for RAG-Based Customer Support
This README serves as the primary knowledge base for the RAG application. Key query categories:

1. **Account Issues**: Registration, login, role changes, password reset
2. **Complaint Tracking**: Status check, escalation, response times
3. **Scheme Information**: Eligibility, documents, deadlines, application links
4. **Marketplace**: Listing items, contacting sellers, reporting issues
5. **Agriculture**: Crop tips, mandi prices, pest control, weather alerts
6. **Health Services**: Finding doctors, ambulance, vaccination camps
7. **Education**: Scholarships, study materials, job training, exam dates
8. **Documents**: Certificate guides, required papers, processing times
9. **Technical**: Platform access, browser support, mobile usage

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026 | Initial release with all 10 core modules |

---

*Last Updated: October 5, 2026*
*Platform: Django 5.2.7 | Python 3.12+*
*Deployment Target: Rural Digital Infrastructure*