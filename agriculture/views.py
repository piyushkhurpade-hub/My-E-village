from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AgricultureTip, MandiPrice

def agri_home(request):
    tips = AgricultureTip.objects.all()
    mandi_prices = MandiPrice.objects.all()

    # Simple category filter for tips
    category_query = request.GET.get('category', 'ALL')
    if category_query != 'ALL':
        tips = tips.filter(category=category_query)

    context = {
        'tips': tips,
        'mandi_prices': mandi_prices,
        'category_query': category_query,
    }
    return render(request, 'agriculture/home.html', context)

@login_required
def add_tip(request):
    if request.user.role not in ['ADMIN', 'OFFICER'] and not request.user.is_superuser:
        messages.error(request, "You are not authorized to post agricultural advice.")
        return redirect('dashboard:panel')

    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        crop_name = request.POST.get('crop_name')
        image = request.FILES.get('image')

        if not title or not content:
            messages.error(request, "Please enter both title and content.")
            return render(request, 'agriculture/add_tip.html')

        tip = AgricultureTip.objects.create(
            title=title,
            category=category,
            content=content,
            crop_name=crop_name,
            image=image
        )
        messages.success(request, f"Agricultural advice '{tip.title}' published successfully!")
        return redirect('agriculture:home')

    return render(request, 'agriculture/add_tip.html')
