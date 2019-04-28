from django.db import models
from utils.mixins import SlugMixin
from .company import Distributor


class Brand(SlugMixin):
    name = models.CharField(max_length=25, verbose_name='Ad')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')

    class Meta:
        verbose_name = 'Marka'
        verbose_name_plural = 'Markalar'

    def __str__(self):
        return self.name


class Product(SlugMixin):
    name = models.CharField(max_length=50, verbose_name='Ad')
    content = models.TextField(verbose_name='Açıklama')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Marka')
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distribütör')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    active = models.BooleanField(default=True, verbose_name='Aktif')
    price = models.FloatField(verbose_name='Fiyat')
    stock_count = models.PositiveIntegerField(verbose_name='Stok Adedi')

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.name


class Category(SlugMixin):
    name = models.CharField(max_length=50, verbose_name='Ad')
    products = models.ManyToManyField(Product, related_name='products', related_query_name='product', blank=True)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name
