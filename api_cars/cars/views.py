from django.shortcuts import render
from rest_framework import generics
from cars.models import Car, CarModel
from cars.serialisers import CarSerialiser, CarModelSerialiser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict



class CarAPIViews(APIView):
    def get(self, request):
        lst = Car.objects.all().values()
        return Response({'posts': list(lst)})
    
    def post(self, request):
    # Retrieve the CarModel instance corresponding to the model ID (e.g., 'Lamborghini')
        car_model_id = request.data['id']
        car_model_instance = CarModel.objects.get(id=car_model_id)

    # Create a new Car instance with the retrieved CarModel instance
        post_new = Car.objects.create(
        color_car=request.data['color_car'],
        relise_data=request.data['relise_data'],
        prise=request.data['prise'],
        car_model=car_model_instance,  # Pass the CarModel instance here
        description_car=request.data['description_car']
    )

        return Response({'post': model_to_dict(post_new)})


# class CarAPIViews(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerialiser


class CarModelAPIViews(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerialiser