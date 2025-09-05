from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField(unique=True)
    student_class = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.roll})"