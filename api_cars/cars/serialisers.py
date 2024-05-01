from rest_framework import serializers
from cars.models import Car, CarModel


class CarSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('color_car', 'id', 'description_car')
       


class CarModelSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('name', 'id')
