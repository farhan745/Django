from django.db import models

# Create your models here.
#One to One relationship
#car COmpany and CEO
class CarCompany(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class CEO(models.Model):        #weak entity
    name = models.CharField(max_length=100)
    car_company = models.OneToOneField(CarCompany, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
#One to MAny
class CarModel(models.Model):
    name = models.CharField(max_length=100)
    car_company = models.ForeignKey(CarCompany, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class FuelType(models.Model):
    name = models.CharField(max_length=100)
    car_models = models.ManyToManyField(CarModel)
    def __str__(self):
        return self.name