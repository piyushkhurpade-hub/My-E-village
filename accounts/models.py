from django.db import models
from django.contrib.auth.models import AbstractUser

# We will extend AbstractUser to support custom fields and role-based permissions.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('VILLAGER', 'Villager'),
        ('OFFICER', 'Staff/Officer'),
        ('ADMIN', 'Village Admin (Gram Panchayat)'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='VILLAGER')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    village_name = models.CharField(max_length=100, default='e-Village Main')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def is_village_admin(self):
        return self.role == 'ADMIN' or self.is_superuser

    def is_officer(self):
        return self.role in ['OFFICER', 'ADMIN'] or self.is_staff or self.is_superuser

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
