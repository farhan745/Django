from django.db import models
import os
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
def student_directory_path(instance, filename):
    return os.path.join('student/media/',instance.name, filename)
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(upload_to = student_directory_path, null=True, blank=True)
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, # User model ke refer korlam/setting.AUTH_USER_MODEL
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_students"
    )
    def __str__(self):
        return self.name
