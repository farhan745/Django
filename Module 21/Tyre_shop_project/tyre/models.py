from django.db import models

# Create your models here.
from django.db import models

class Tyre(models.Model):
    tyre_name = models.CharField(max_length=100)
    tyre_size = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='tyres/', blank=True, null=True)

    def __str__(self):
        return f"{self.tyre_name} - {self.company}"
