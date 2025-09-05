from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50,verbose_name="Student Name")
    roll = models.IntegerField(unique=True,verbose_name="ID number")
    age = models.IntegerField(null=True,verbose_name="Age")
    city = models.CharField(max_length=50,verbose_name="City Name")
    def __str__(self):
        return f"{self.name}({self.roll})"
    