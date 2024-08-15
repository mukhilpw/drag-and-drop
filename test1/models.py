from django.db import models

# Create your models here.
# models.py

# models.py
from django.db import models
from django.utils import timezone

class Card(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    subheading_1 = models.CharField(max_length=255, blank=True, null=True)
    subheading_2 = models.CharField(max_length=255, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True) # Automatically set to now on save

    def __str__(self):
        return self.title
