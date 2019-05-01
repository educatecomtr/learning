from django.db import models
from django.contrib.auth.models import User
from utils.mixins import SlugMixin


class Company(SlugMixin):
    name = models.CharField(max_length=50, verbose_name='Ad')
    content = models.TextField(verbose_name='Açıklama')
    address = models.TextField(verbose_name='Adres')
    phone = models.CharField(max_length=11, verbose_name='Telefon')
    email = models.EmailField(verbose_name='E-Posta')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yetkili')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    active = models.BooleanField(default=True, verbose_name='Aktif')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

