from django.db import models
from django.urls import reverse

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)
    
    def get_absolute_url(self):
        return reverse('student')
    