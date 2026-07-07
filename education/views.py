from django.shortcuts import render
from .models import EducationResource

def list_resources(request):
    resources = EducationResource.objects.all()

    # Search & Filter
    search_query = request.GET.get('search', '')
    category = request.GET.get('category', 'ALL')

    if search_query:
        resources = resources.filter(title__icontains=search_query)

    if category != 'ALL':
        resources = resources.filter(category=category)

    context = {
        'resources': resources,
        'search_query': search_query,
        'category_query': category,
    }
    return render(request, 'education/list.html', context)
