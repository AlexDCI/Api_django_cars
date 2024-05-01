from django.contrib import admin

from cars.models import Car, CarModel

admin.site.register(Car)

admin.site.register(CarModel)
