from django.db import models
from django.conf import settings

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('PRODUCE', 'Fresh Vegetables & Crops'),
        ('DAIRY', 'Dairy & Poultry'),
        ('HANDICRAFTS', 'Handicrafts & Artworks'),
        ('SERVICES', 'Local Labor & Services (Tailoring, Repair)'),
        ('OTHERS', 'Others'),
    )
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='PRODUCE')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in INR")
    contact_number = models.CharField(max_length=15, help_text="Contact number for buyers")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - ₹{self.price}"
