from django.db import models

class VillageProfile(models.Model):
    name = models.CharField(max_length=100, default="e-Village Main")
    district = models.CharField(max_length=100, default="Pune")
    state = models.CharField(max_length=100, default="Maharashtra")
    population = models.IntegerField(default=1500)
    schools_count = models.IntegerField(default=2)
    hospitals_count = models.IntegerField(default=1)
    water_connections = models.IntegerField(default=350)
    panchayat_head = models.CharField(max_length=100, default="Sarpanch Ramesh Patil")
    about_text = models.TextField(default="Welcome to our digital village portal. We strive to empower our citizens through connectivity.")
    contact_email = models.EmailField(default="contact@evillage.gov.in")
    contact_phone = models.CharField(max_length=15, default="+91 9876543210")

    def __str__(self):
        return self.name
