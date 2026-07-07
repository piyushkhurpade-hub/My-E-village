import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_evillage.settings')
django.setup()

from django.contrib.auth import get_user_model
from dashboard.models import VillageProfile
from notices.models import Notice
from schemes.models import Scheme
from complaints.models import Complaint
from agriculture.models import AgricultureTip, MandiPrice
from health.models import HealthService
from education.models import EducationResource
from marketplace.models import Product
from documents.models import DocumentGuide

User = get_user_model()

def create_seed_data():
    print("Seeding database...")

    # 1. Create Users
    if not User.objects.filter(username="admin").exists():
        admin = User.objects.create_superuser("admin", "admin@evillage.gov.in", "admin123")
        admin.role = 'ADMIN'
        admin.first_name = "Sarpanch"
        admin.last_name = "Ramesh Patil"
        admin.phone_number = "9876543210"
        admin.save()
        print("Created admin user.")
    else:
        admin = User.objects.get(username="admin")

    if not User.objects.filter(username="officer").exists():
        officer = User.objects.create_user("officer", "officer@evillage.gov.in", "officer123")
        officer.role = 'OFFICER'
        officer.first_name = "Vikas"
        officer.last_name = "Shinde"
        officer.phone_number = "9876543211"
        officer.save()
        print("Created officer user.")
    else:
        officer = User.objects.get(username="officer")

    if not User.objects.filter(username="villager").exists():
        villager = User.objects.create_user("villager", "villager@gmail.com", "villager123")
        villager.role = 'VILLAGER'
        villager.first_name = "Rahul"
        villager.last_name = "Jadhav"
        villager.phone_number = "9876543212"
        villager.save()
        print("Created villager user.")
    else:
        villager = User.objects.get(username="villager")

    # 2. Create Village Profile
    VillageProfile.objects.all().delete()
    profile = VillageProfile.objects.create(
        name="e-Village Wadgaon",
        district="Pune",
        state="Maharashtra",
        population=1850,
        schools_count=3,
        hospitals_count=1,
        water_connections=420,
        panchayat_head="Sarpanch Ramesh Patil",
        about_text="Wadgaon is a progressive digital village located in the Pune district of Maharashtra. Through digital connectivity, we aim to deliver transparent governance, quality education, real-time farming support, and immediate health services directly to our villagers' fingertips.",
        contact_email="grampanchayat.wadgaon@gov.in",
        contact_phone="+91 2114 223456"
    )
    print("Created village profile.")

    # 3. Create Notices
    Notice.objects.all().delete()
    notices_data = [
        {
            "title": "Gram Sabha Meeting - July 10",
            "content": "A Gram Sabha meeting is scheduled for Friday, July 10, at 10:00 AM in the Gram Panchayat Hall. The main agenda is to discuss the new water pipeline project and village sanitation. All villagers are requested to attend.",
            "category": "MEETINGS",
            "is_urgent": True,
            "published_by": admin
        },
        {
            "title": "Free Health Checkup Camp this Sunday",
            "content": "A free health checkup and vaccination camp will be conducted at the Primary Health Centre (PHC) this Sunday, July 12, from 9:00 AM to 4:00 PM. Specialist doctors from Pune General Hospital will be available.",
            "category": "HEALTH",
            "is_urgent": False,
            "published_by": admin
        },
        {
            "title": "Water Supply Interruption Notice",
            "content": "Due to maintenance work on the main water pump, water supply to Wards 1 and 2 will be suspended tomorrow (July 6) between 10:00 AM and 2:00 PM. Please store enough water in advance.",
            "category": "GENERAL",
            "is_urgent": True,
            "published_by": officer
        },
        {
            "title": "Scholarship Form Submission Deadline Extended",
            "content": "The last date for submitting applications for the Post-Matric Scholarship for SC/ST/OBC students has been extended to July 25. Forms can be submitted at the school office or digital service center.",
            "category": "EDUCATION",
            "is_urgent": False,
            "published_by": officer
        },
        {
            "title": "Distribution of Subsidized Seeds",
            "content": "High-quality subsidized soybean and cotton seeds are now available for distribution at the Gram Panchayat Agricultural Center. Farmers must carry their 7/12 extract and Aadhaar card to collect them.",
            "category": "AGRICULTURE",
            "is_urgent": False,
            "published_by": admin
        }
    ]
    for n in notices_data:
        Notice.objects.create(**n)
    print("Created notices.")

    # 4. Create Schemes
    Scheme.objects.all().delete()
    schemes_data = [
        {
            "title": "PM Kisan Samman Nidhi",
            "category": "FARMERS",
            "description": "An initiative by the Government of India that provides up to ₹6,000 per year in three equal installments directly into the bank accounts of small and marginal farmers.",
            "eligibility": "Small and marginal farmers owning cultivable land up to 2 hectares.",
            "required_documents": "1. Land holding documents (7/12 extract)\n2. Aadhaar Card\n3. Bank Account details\n4. Mobile number linked to Aadhaar",
            "apply_link": "https://pmkisan.gov.in/",
            "last_date": date.today() + timedelta(days=60)
        },
        {
            "title": "Savitribai Phule Scholarship Scheme",
            "category": "EDUCATION",
            "description": "Financial assistance scheme to encourage education among girls from backward class categories (SC, ST, VJNT, SBC) studying in classes 5th to 10th.",
            "eligibility": "Girls belonging to SC, ST, VJNT, or SBC categories studying in government schools. No income limit.",
            "required_documents": "1. Caste Certificate\n2. Previous Year Marksheet\n3. Aadhaar Card\n4. School Bonafide Certificate",
            "apply_link": "https://mahadbt.maharashtra.gov.in/",
            "last_date": date.today() + timedelta(days=30)
        },
        {
            "title": "Sanjay Gandhi Niradhar Pension Yojana",
            "category": "PENSIONS",
            "description": "Monthly financial pension provided to destitute persons, blind, disabled, orphans, or widows who have no source of income or support.",
            "eligibility": "Residents of Maharashtra, age below 65 (unless disabled), annual family income less than ₹21,000.",
            "required_documents": "1. Age proof\n2. Income certificate\n3. Residence certificate (Domicile)\n4. Disability certificate (if applicable)\n5. Passport size photograph",
            "apply_link": "https://aaplesarkar.mahaonline.gov.in/",
            "last_date": None
        },
        {
            "title": "Ayushman Bharat - PM Jan Arogya Yojana",
            "category": "HEALTH",
            "description": "The largest health assurance scheme in the world, providing health cover of ₹5 Lakhs per family per year for secondary and tertiary care hospitalization.",
            "eligibility": "Families identified by the Socio-Economic Caste Census (SECC) database.",
            "required_documents": "1. Aadhaar Card / Ration Card\n2. Family Identity Proof\n3. PMJAY Letter or Card",
            "apply_link": "https://www.pmjay.gov.in/",
            "last_date": None
        }
    ]
    for s in schemes_data:
        Scheme.objects.create(**s)
    print("Created schemes.")

    # 5. Create Complaints
    Complaint.objects.all().delete()
    complaints_data = [
        {
            "title": "Potholes on Temple Road",
            "category": "ROADS",
            "description": "The main road connecting the Hanuman Temple to the bus stand has developed huge potholes after the recent heavy rains. It has become very dangerous for two-wheelers and children.",
            "status": "PENDING",
            "raised_by": villager,
            "admin_reply": None
        },
        {
            "title": "Water leakage near Ward 3 Tank",
            "category": "WATER",
            "description": "There is a major crack in the outlet pipe of the water tank in Ward 3. Thousands of liters of water are getting wasted daily.",
            "status": "IN_PROGRESS",
            "raised_by": villager,
            "admin_reply": "Panchayat plumber has inspected the site. The replacement pipe has been ordered and will be installed on Monday."
        },
        {
            "title": "Frequent Power Fluctuations in Evening",
            "category": "ELECTRICITY",
            "description": "Every day between 7 PM and 10 PM, we experience extreme voltage fluctuations. It is damaging home appliances like refrigerators and televisions.",
            "status": "RESOLVED",
            "raised_by": villager,
            "admin_reply": "MSEB office was notified. They have upgraded the local distribution transformer tap setting, which has stabilized the voltage. Please confirm if resolved."
        }
    ]
    for c in complaints_data:
        Complaint.objects.create(**c)
    print("Created complaints.")

    # 6. Create Agriculture Tips & Mandi Prices
    AgricultureTip.objects.all().delete()
    tips_data = [
        {
            "title": "Monsoon Crop Advisory: Soybean Planting",
            "category": "CROP",
            "content": "For optimal yield in clay-loam soils, ensure a planting depth of 3-5 cm. Apply balanced NPK (20:30:20 kg/ha) at the time of sowing. Treatment with Rhizobium culture is recommended to improve nitrogen fixation.",
            "crop_name": "Soybean"
        },
        {
            "title": "Heavy Rain Warning: 48 Hours Alert",
            "category": "WEATHER",
            "content": "The Meteorological Department has issued a yellow alert for Pune district. Expect moderate to heavy rain in the next 48 hours. Farmers are advised to clear drainage channels in fields to prevent waterlogging.",
            "crop_name": None
        },
        {
            "title": "Management of Fall Armyworm in Maize",
            "category": "PEST",
            "content": "Inspect maize crops weekly. If infestation exceeds 10%, spray Neem Seed Kernel Extract (NSKE) 5% or apply Emamectin benzoate 5% SG @ 0.4 g/liter of water in the central whorl of the plants.",
            "crop_name": "Maize"
        }
    ]
    for t in tips_data:
        AgricultureTip.objects.create(**t)

    MandiPrice.objects.all().delete()
    mandi_data = [
        {"crop_name": "Soybean", "price_per_quintal": 4550.00, "market_name": "Wadgaon Mandi"},
        {"crop_name": "Cotton (Kapas)", "price_per_quintal": 7200.00, "market_name": "Pune Mandi"},
        {"crop_name": "Onion", "price_per_quintal": 2200.00, "market_name": "Chakan Mandi"},
        {"crop_name": "Wheat", "price_per_quintal": 2450.00, "market_name": "Wadgaon Mandi"},
        {"crop_name": "Gram (Chana)", "price_per_quintal": 5300.00, "market_name": "Pune Mandi"}
    ]
    for m in mandi_data:
        MandiPrice.objects.create(**m)
    print("Created agriculture info.")

    # 7. Create Health Services
    HealthService.objects.all().delete()
    health_data = [
        {
            "name": "Wadgaon Primary Health Centre (PHC)",
            "service_type": "PHC",
            "contact_number": "+91 2114 220112",
            "timing": "8:00 AM - 6:00 PM (Emergency 24/7)",
            "location": "Near Panchayat Office, Ward 2",
            "description": "General OPD, maternal care, routine child immunization, basic blood tests, and free pharmacy for basic medicines."
        },
        {
            "name": "e-Village Emergency Ambulance",
            "service_type": "AMBULANCE",
            "contact_number": "108 / +91 9999112112",
            "timing": "24/7 Services",
            "location": "Parked at PHC Wadgaon",
            "description": "Fully equipped ambulance with oxygen support for emergency transport to Talegaon/Pune hospitals."
        },
        {
            "name": "Dr. Sunil Deshmukh (General Physician)",
            "service_type": "DOCTOR",
            "contact_number": "+91 9422001122",
            "timing": "10:00 AM - 1:00 PM, 5:00 PM - 8:00 PM",
            "location": "Deshmukh Clinic, Main Bazar Road",
            "description": "Experienced physician specializing in fever, seasonal illnesses, diabetes, and hypertension management."
        },
        {
            "name": "Child & Maternal Vaccination Camp",
            "service_type": "VACCINE",
            "contact_number": "+91 2114 220112",
            "timing": "Every Wednesday, 9:00 AM - 2:00 PM",
            "location": "Anganwadi Center 1 & 2",
            "description": "Weekly vaccination drive covering Polio, BCG, DPT, and MMR vaccines. Free health monitoring for pregnant women."
        }
    ]
    for h in health_data:
        HealthService.objects.create(**h)
    print("Created health services.")

    # 8. Create Education Resources
    EducationResource.objects.all().delete()
    edu_data = [
        {
            "title": "Pre-Matric Scholarship for Backward Class Students",
            "category": "SCHOLARSHIP",
            "description": "Scholarships for students of classes 9th and 10th belonging to scheduled castes and tribes to reduce school dropouts.",
            "link": "https://scholarships.gov.in/"
        },
        {
            "title": "Standard 10th Science Digital Study Notes",
            "category": "STUDY_MATERIAL",
            "description": "Maharashtra State Board Standard 10th Science & Technology Part 1 & 2 comprehensive chapter summaries and solved question banks.",
            "link": "https://www.maa.ac.in/"
        },
        {
            "title": "Free General Knowledge (GK) and Aptitude Mock Tests",
            "category": "EXAMS",
            "description": "Interactive online mock tests and previous papers for MPSC (Maharashtra Public Service Commission) and Police Bharti examinations.",
            "link": "https://mpsc.gov.in/"
        },
        {
            "title": "Computer Training & Tally Certification Course",
            "category": "JOBS",
            "description": "A 3-month free basic computer skills and Tally accounting certification course organized by the Block Development Office at Wadgaon Library.",
            "link": "https://www.mahaswayam.gov.in/"
        }
    ]
    for e in edu_data:
        EducationResource.objects.create(**e)
    print("Created education resources.")

    # 9. Create Products
    Product.objects.all().delete()
    products_data = [
        {
            "seller": villager,
            "title": "Fresh Organic Buffalo Milk",
            "category": "DAIRY",
            "description": "Pure, unadulterated buffalo milk available daily. Morning and evening home delivery in Ward 1 and 2.",
            "price": 65.00,
            "contact_number": "9876543212"
        },
        {
            "seller": villager,
            "title": "Handmade Wooden Kitchen Sets",
            "category": "HANDICRAFTS",
            "description": "Beautifully polished, eco-friendly wooden spoons, bowls, and spatulas handcrafted from local Neem wood. Very durable.",
            "price": 350.00,
            "contact_number": "9876543212"
        },
        {
            "seller": officer,
            "title": "Fresh Organic Tomatoes (per kg)",
            "category": "PRODUCE",
            "description": "Farm-fresh tomatoes harvested daily. Grown without synthetic chemical pesticides.",
            "price": 40.00,
            "contact_number": "9876543211"
        }
    ]
    for p in products_data:
        Product.objects.create(**p)
    print("Created marketplace products.")

    # 10. Create Document Guides
    DocumentGuide.objects.all().delete()
    docs_data = [
        {
            "name": "Income Certificate (उत्पन्नाचा दाखला)",
            "description": "An official document certifying the annual income of a family, required for school admissions, scholarships, and availing subsidized ration.",
            "required_documents": "1. Identity Proof (Aadhaar Card / Voter ID)\n2. Address Proof (Ration Card / Electricity Bill)\n3. Income Proof (Form 16 / Salary Slip / Talathi Income Report)\n4. Self-Declaration Affidavit",
            "processing_time": "15 Days",
            "official_link": "https://aaplesarkar.mahaonline.gov.in/"
        },
        {
            "name": "Caste Certificate (जातीचा दाखला)",
            "description": "A certificate establishing a person's membership in a particular caste/tribe, crucial for reserving seats in education and government jobs.",
            "required_documents": "1. Applicant's Aadhaar Card\n2. Father's Caste Certificate / TC (School Leaving Certificate)\n3. Extract of 7/12 or land record showing caste mention (for old records)\n4. Domicile Certificate of Maharashtra",
            "processing_time": "21 Days",
            "official_link": "https://aaplesarkar.mahaonline.gov.in/"
        },
        {
            "name": "Domicile Certificate (अधिवास प्रमाणपत्र)",
            "description": "Certifies that a person is a permanent resident of Maharashtra state. Essential for university admissions and state government job recruitment.",
            "required_documents": "1. Residence proof for last 15 years (Ration cards, school leaves, land records)\n2. Birth Certificate or TC\n3. Aadhaar Card\n4. Two passport size photographs",
            "processing_time": "15 Days",
            "official_link": "https://aaplesarkar.mahaonline.gov.in/"
        }
    ]
    for d in docs_data:
        DocumentGuide.objects.create(**d)
    print("Created document guides.")
    
    print("Seeding complete! Database is populated with demo data.")

if __name__ == "__main__":
    create_seed_data()
