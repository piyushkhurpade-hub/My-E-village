from django.db import models

class Scheme(models.Model):
    CATEGORY_CHOICES = (
        ('FARMERS', 'Agriculture / Farmers'),
        ('EDUCATION', 'Scholarships & Education'),
        ('PENSIONS', 'Social Security & Pensions'),
        ('WOMEN', 'Women Empowerment'),
        ('HEALTH', 'Healthcare & Subsidies'),
        ('EMPLOYMENT', 'Employment & Skill Development'),
        ('OTHERS', 'Others'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHERS')
    description = models.TextField()
    eligibility = models.TextField(help_text="Eligibility criteria (who can apply)")
    required_documents = models.TextField(help_text="List of documents required")
    apply_link = models.URLField(blank=True, null=True, help_text="Link to external application portal")
    last_date = models.DateField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
