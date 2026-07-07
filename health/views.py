from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import HealthService

def list_services(request):
    services = HealthService.objects.all()

    # Search & Filter
    search_query = request.GET.get('search', '')
    service_type = request.GET.get('type', 'ALL')

    if search_query:
        services = services.filter(name__icontains=search_query)
    
    if service_type != 'ALL':
        services = services.filter(service_type=service_type)

    context = {
        'services': services,
        'search_query': search_query,
        'service_type': service_type,
    }
    return render(request, 'health/list.html', context)

@login_required
def add_service(request):
    if request.user.role not in ['ADMIN', 'OFFICER'] and not request.user.is_superuser:
        messages.error(request, "You are not authorized to add health services.")
        return redirect('dashboard:panel')

    if request.method == 'POST':
        name = request.POST.get('name')
        service_type = request.POST.get('service_type')
        contact_number = request.POST.get('contact_number')
        timing = request.POST.get('timing')
        location = request.POST.get('location')
        description = request.POST.get('description')

        if not name or not contact_number:
            messages.error(request, "Please enter name and contact number.")
            return render(request, 'health/add.html')

        service = HealthService.objects.create(
            name=name,
            service_type=service_type,
            contact_number=contact_number,
            timing=timing,
            location=location,
            description=description
        )
        messages.success(request, f"Health Service '{service.name}' added successfully!")
        return redirect('health:list')

    return render(request, 'health/add.html')
