from django.shortcuts import render
from .models import DocumentGuide

def list_guides(request):
    guides = DocumentGuide.objects.all()
    
    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        guides = guides.filter(name__icontains=search_query)

    context = {
        'guides': guides,
        'search_query': search_query,
    }
    return render(request, 'documents/list.html', context)
