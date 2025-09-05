from django.contrib import admin
from .models import CarCompany, CEO, CarModel, FuelType
# Register your models here.
admin.site.register(CarCompany)
admin.site.register(CEO)
admin.site.register(CarModel)
admin.site.register(FuelType)
