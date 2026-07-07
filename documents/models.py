from django.db import models

class DocumentGuide(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(help_text="What this certificate/document is used for")
    required_documents = models.TextField(help_text="List of documents needed for application")
    processing_time = models.CharField(max_length=100, default="15 Days")
    official_link = models.URLField(blank=True, null=True, help_text="Official application website link")

    def __str__(self):
        return self.name
