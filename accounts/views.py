from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:panel')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role', 'VILLAGER')

        # Simple validations
        if not username or not email or not password:
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'accounts/register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'accounts/register.html')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number
        )
        
        # Log the user in
        login(request, user)
        messages.success(request, f"Registration successful! Welcome to e-Village, {user.first_name}!")
        return redirect('dashboard:panel')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:panel')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return render(request, 'accounts/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('dashboard:panel')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('dashboard:home')
