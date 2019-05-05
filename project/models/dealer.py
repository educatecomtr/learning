from django.db import models
from django.contrib.auth.models import User
from .company import Company


class Dealer(Company):

    staff = models.ManyToManyField(User, related_name='dealers', related_query_name='dealer', blank=True)

    class Meta:
        verbose_name = 'Bayi'
        verbose_name_plural = 'Bayiler'
        permissions = [('manage_dealer', 'Bayi yönetim izni')]
