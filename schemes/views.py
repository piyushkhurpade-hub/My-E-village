from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Scheme

def list_schemes(request):
    schemes = Scheme.objects.all()

    # Search & Filter
    search_query = request.GET.get('search', '')
    category_query = request.GET.get('category', 'ALL')

    if search_query:
        schemes = schemes.filter(title__icontains=search_query)
    
    if category_query != 'ALL':
        schemes = schemes.filter(category=category_query)

    context = {
        'schemes': schemes,
        'search_query': search_query,
        'category_query': category_query,
    }
    return render(request, 'schemes/list.html', context)

def scheme_detail(request, scheme_id):
    scheme = get_object_or_404(Scheme, id=scheme_id)
    return render(request, 'schemes/detail.html', {'scheme': scheme})

@login_required
def add_scheme(request):
    if request.user.role not in ['ADMIN', 'OFFICER'] and not request.user.is_superuser:
        messages.error(request, "You are not authorized to publish schemes.")
        return redirect('dashboard:panel')

    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        eligibility = request.POST.get('eligibility')
        required_documents = request.POST.get('required_documents')
        apply_link = request.POST.get('apply_link')
        last_date = request.POST.get('last_date') or None

        if not title or not description or not eligibility or not required_documents:
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'schemes/add.html')

        scheme = Scheme.objects.create(
            title=title,
            category=category,
            description=description,
            eligibility=eligibility,
            required_documents=required_documents,
            apply_link=apply_link,
            last_date=last_date
        )
        messages.success(request, f"Government Scheme '{scheme.title}' published successfully!")
        return redirect('schemes:list')

    return render(request, 'schemes/add.html')
