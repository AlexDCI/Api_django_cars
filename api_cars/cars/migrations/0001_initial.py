# Generated by Django 5.0.4 on 2024-04-30 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_car', models.CharField(max_length=50)),
                ('relise_data', models.DateField()),
                ('prise', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description_car', models.TextField(blank=True)),
                ('car_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
            ],
        ),
    ]
