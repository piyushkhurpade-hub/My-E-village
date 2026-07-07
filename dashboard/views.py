from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import VillageProfile
from notices.models import Notice
from schemes.models import Scheme
from complaints.models import Complaint
from agriculture.models import AgricultureTip, MandiPrice
from health.models import HealthService
from marketplace.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    # Fetch or create default profile
    profile = VillageProfile.objects.first()
    if not profile:
        profile = VillageProfile.objects.create()

    # Fetch latest notices (limit to 3)
    latest_notices = Notice.objects.all()[:3]
    
    # Fetch schemes (limit to 3)
    latest_schemes = Scheme.objects.all()[:3]

    # Fetch some Mandi prices
    mandi_prices = MandiPrice.objects.all()[:4]

    # Fetch emergency contacts
    emergency_contacts = HealthService.objects.filter(service_type__in=['AMBULANCE', 'EMERGENCY'])[:3]

    context = {
        'profile': profile,
        'latest_notices': latest_notices,
        'latest_schemes': latest_schemes,
        'mandi_prices': mandi_prices,
        'emergency_contacts': emergency_contacts,
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def panel(request):
    user = request.user
    
    if user.role == 'ADMIN' or user.is_superuser:
        # Admin Dashboard
        total_villagers = User.objects.filter(role='VILLAGER').count()
        total_complaints = Complaint.objects.count()
        pending_complaints_count = Complaint.objects.filter(status='PENDING').count()
        in_progress_complaints_count = Complaint.objects.filter(status='IN_PROGRESS').count()
        resolved_complaints_count = Complaint.objects.filter(status='RESOLVED').count()
        total_notices = Notice.objects.count()
        total_schemes = Scheme.objects.count()
        total_products = Product.objects.count()

        recent_complaints = Complaint.objects.all()[:6]
        recent_products = Product.objects.all()[:6]

        context = {
            'total_villagers': total_villagers,
            'total_complaints': total_complaints,
            'pending_complaints_count': pending_complaints_count,
            'in_progress_complaints_count': in_progress_complaints_count,
            'resolved_complaints_count': resolved_complaints_count,
            'total_notices': total_notices,
            'total_schemes': total_schemes,
            'total_products': total_products,
            'recent_complaints': recent_complaints,
            'recent_products': recent_products,
        }
        return render(request, 'dashboard/admin_panel.html', context)

    elif user.role == 'OFFICER':
        # Staff/Officer Dashboard
        total_complaints = Complaint.objects.count()
        pending_complaints_count = Complaint.objects.filter(status='PENDING').count()
        in_progress_complaints_count = Complaint.objects.filter(status='IN_PROGRESS').count()
        total_notices = Notice.objects.filter(published_by=user).count()

        recent_complaints = Complaint.objects.filter(status__in=['PENDING', 'IN_PROGRESS'])[:6]

        context = {
            'total_complaints': total_complaints,
            'pending_complaints_count': pending_complaints_count,
            'in_progress_complaints_count': in_progress_complaints_count,
            'total_notices': total_notices,
            'recent_complaints': recent_complaints,
        }
        return render(request, 'dashboard/officer_panel.html', context)

    else:
        # Villager Dashboard
        my_complaints = Complaint.objects.filter(raised_by=user)
        my_products = Product.objects.filter(seller=user)

        context = {
            'my_complaints': my_complaints,
            'my_products': my_products,
        }
        return render(request, 'dashboard/villager_panel.html', context)
