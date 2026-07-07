from django.db import models

class EducationResource(models.Model):
    CATEGORY_CHOICES = (
        ('SCHOLARSHIP', 'Scholarship Updates'),
        ('STUDY_MATERIAL', 'Digital Learning Resources'),
        ('JOBS', 'Local Jobs & Skill Training'),
        ('EXAMS', 'Competitive Exams Prep'),
        ('SCHOOL_NOTICE', 'School Notices & Events'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='STUDY_MATERIAL')
    description = models.TextField()
    link = models.URLField(blank=True, null=True, help_text="Direct link to resource or application portal")
    file = models.FileField(upload_to='education/', blank=True, null=True, help_text="Upload notice PDF / resources")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
