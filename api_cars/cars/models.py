from django.db import models


class Car(models.Model):
    color_car = models.CharField(max_length=50)
    relise_data = models.DateField()
    prise = models.DecimalField(max_digits=10, decimal_places=2)
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE, null=True)
    description_car = models.TextField(blank=True)

    


class CarModel(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    

