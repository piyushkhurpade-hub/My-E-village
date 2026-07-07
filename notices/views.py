from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notice

def list_notices(request):
    notices = Notice.objects.all()
    
    # Optional search filtering
    search_query = request.GET.get('search', '')
    if search_query:
        notices = notices.filter(title__icontains=search_query)

    context = {
        'notices': notices,
        'search_query': search_query,
    }
    return render(request, 'notices/list.html', context)

@login_required
def add_notice(request):
    # Restrict to admin and officer
    if request.user.role not in ['ADMIN', 'OFFICER'] and not request.user.is_superuser:
        messages.error(request, "You are not authorized to post notices.")
        return redirect('dashboard:panel')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        is_urgent = request.POST.get('is_urgent') == 'on'

        if not title or not content:
            messages.error(request, "Please enter both title and content.")
            return render(request, 'notices/add.html')

        notice = Notice.objects.create(
            title=title,
            content=content,
            category=category,
            is_urgent=is_urgent,
            published_by=request.user
        )
        messages.success(request, f"Notice '{notice.title}' posted successfully!")
        return redirect('notices:list')

    return render(request, 'notices/add.html')
