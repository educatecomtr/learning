from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    # id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Ürün İsmi', max_length=200)
    content = models.TextField(verbose_name='Ürün Açıklaması')
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # db_table = 'urunler'
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

        def __str__(self):
            return self.name
