from django.db import models

# Create your models here.

#################   Abstract base classes inheritance  ################

class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Student(CommonInfo):
    fees = models.IntegerField()
    date = None
    
class Teacher(CommonInfo):
    salary = models.IntegerField()


