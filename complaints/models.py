from django.db import models
from django.conf import settings

class Complaint(models.Model):
    CATEGORY_CHOICES = (
        ('ROADS', 'Roads & Infrastructure'),
        ('WATER', 'Water Supply & Quality'),
        ('ELECTRICITY', 'Electricity & Power Outages'),
        ('SANITATION', 'Sanitation & Waste Management'),
        ('INTERNET', 'Internet & Network Connectivity'),
        ('HEALTH', 'Public Health / Medical Services'),
        ('OTHERS', 'Others'),
    )
    STATUS_CHOICES = (
        ('PENDING', 'Pending Review'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHERS')
    description = models.TextField()
    photo = models.ImageField(upload_to='complaints/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    raised_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin_reply = models.TextField(blank=True, null=True, help_text="Action taken or response from Village Admin")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
