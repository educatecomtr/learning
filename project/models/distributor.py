from django.db import models
from .company import Company
from .dealer import Dealer
from django.contrib.auth.models import User


class Distributor(Company):
    dealers = models.ManyToManyField(Dealer, related_name='distributors', related_query_name='distributor', blank=True)
    staff = models.ManyToManyField(User, related_name='distributors', related_query_name='distributor', blank=True)

    class Meta:
        verbose_name = 'Distribütör'
        verbose_name_plural = 'Distribütörler'

