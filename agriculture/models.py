from django.db import models

class AgricultureTip(models.Model):
    CATEGORY_CHOICES = (
        ('CROP', 'Crop Advisory'),
        ('WEATHER', 'Weather Alert'),
        ('FERTILIZER', 'Fertilizer & Soil Guidance'),
        ('PEST', 'Pest & Disease Control'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='CROP')
    content = models.TextField()
    crop_name = models.CharField(max_length=100, blank=True, null=True, help_text="e-Village specific crop (optional)")
    image = models.ImageField(upload_to='agriculture/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class MandiPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    price_per_quintal = models.DecimalField(max_length=10, decimal_places=2, max_digits=10, help_text="Price in INR")
    market_name = models.CharField(max_length=100, default="Local Mandi")
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['crop_name']

    def __str__(self):
        return f"{self.crop_name} - ₹{self.price_per_quintal}/q ({self.market_name})"
