from django.db import models


class Car(models.Model):
    BRAND_CHOICES = (
        ('A', 'AUDI'),
        ('B', 'BMW'),
        ('M', 'MERCEDES'),
        ('V', 'VOLVO')
    )

    brand = models.CharField(max_length=1, choices=BRAND_CHOICES, default='A')
    model = models.CharField(max_length=50)
    year = models.IntegerField()

