from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

def list_products(request):
    products = Product.objects.filter(is_available=True)

    # Search & Filter
    search_query = request.GET.get('search', '')
    category = request.GET.get('category', 'ALL')

    if search_query:
        products = products.filter(title__icontains=search_query)

    if category != 'ALL':
        products = products.filter(category=category)

    context = {
        'products': products,
        'search_query': search_query,
        'category_query': category,
    }
    return render(request, 'marketplace/list.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        contact_number = request.POST.get('contact_number')
        image = request.FILES.get('image')

        if not title or not price or not contact_number:
            messages.error(request, "Please enter product title, price, and contact number.")
            return render(request, 'marketplace/add.html')

        product = Product.objects.create(
            seller=request.user,
            title=title,
            category=category,
            description=description,
            price=price,
            contact_number=contact_number,
            image=image
        )
        messages.success(request, f"Marketplace product '{product.title}' listed successfully!")
        return redirect('marketplace:list')

    return render(request, 'marketplace/add.html')
