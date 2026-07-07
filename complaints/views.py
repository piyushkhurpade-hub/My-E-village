from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Complaint

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        if not title or not description:
            messages.error(request, "Please enter both title and description.")
            return render(request, 'complaints/submit.html')

        complaint = Complaint.objects.create(
            title=title,
            category=category,
            description=description,
            photo=photo,
            raised_by=request.user
        )
        messages.success(request, f"Grievance '{complaint.title}' registered successfully! Track status in your dashboard.")
        return redirect('dashboard:panel')

    return render(request, 'complaints/submit.html')

@login_required
def update_complaint(request, complaint_id):
    # Allow only Admin and Officer
    if request.user.role not in ['ADMIN', 'OFFICER'] and not request.user.is_superuser:
        messages.error(request, "You are not authorized to update complaints.")
        return redirect('dashboard:panel')

    complaint = get_object_or_404(Complaint, id=complaint_id)

    if request.method == 'POST':
        status = request.POST.get('status')
        admin_reply = request.POST.get('admin_reply')

        complaint.status = status
        complaint.admin_reply = admin_reply
        complaint.save()

        messages.success(request, f"Complaint status updated to {complaint.get_status_display()} successfully!")
        
    return redirect('dashboard:panel')
