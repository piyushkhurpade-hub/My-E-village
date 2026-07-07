from django.db import models

class HealthService(models.Model):
    SERVICE_CHOICES = (
        ('DOCTOR', 'Local Doctor / Clinic'),
        ('AMBULANCE', 'Ambulance Service'),
        ('PHC', 'Primary Health Centre (PHC)'),
        ('VACCINE', 'Vaccination Camp'),
        ('EMERGENCY', 'Emergency Helpline'),
    )
    name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='PHC')
    contact_number = models.CharField(max_length=20)
    timing = models.CharField(max_length=100, default="24/7", help_text="e.g. 9:00 AM - 5:00 PM or 24/7")
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text="Services offered or medical specialization")

    class Meta:
        ordering = ['service_type', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_service_type_display()})"
