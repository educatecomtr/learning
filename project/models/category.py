from django.db import models
from project.mixins import SlugMixin
from .product import Product


class Category(SlugMixin):
    name = models.CharField(max_length=50, verbose_name='Ad')
    products = models.ManyToManyField(Product, related_name='products', related_query_name='product', blank=True)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name
