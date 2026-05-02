from django.db import models
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    focus_area = models.CharField(max_length=50) # e.g., 'Education', 'Health'
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
