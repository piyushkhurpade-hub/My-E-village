from django.db import models
from django.conf import settings

class Notice(models.Model):
    CATEGORY_CHOICES = (
        ('GENERAL', 'General Notice'),
        ('HEALTH', 'Health Alert / Camp'),
        ('EDUCATION', 'School / Education'),
        ('AGRICULTURE', 'Farming / Agriculture'),
        ('MEETINGS', 'Gram Sabha / Meeting'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')
    created_at = models.DateTimeField(auto_now_add=True)
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notices')
    is_urgent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
