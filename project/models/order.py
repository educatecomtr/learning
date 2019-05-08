from django.db import models
from .product import Product
from .dealer import Dealer


class Order(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Bayi')
    order_transfered = models.BooleanField(default=False, verbose_name='Nakliye Tamamlandı')
    order_cancelled = models.BooleanField(default=False, verbose_name='Sipariş İptal Edildi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sipariş Tarihi')
    updated = models.DateTimeField(auto_now=True, verbose_name='Sipariş Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Sipariş'
        verbose_name_plural = 'Siparişler'
        permissions = [('manage_order', 'Sipariş yönetim izni')]

    def __str__(self):
        return self.dealer.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Sipariş', related_name='ordered_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün')
    item_count = models.PositiveIntegerField(verbose_name='Ürün Adedi')
    item_price = models.FloatField(verbose_name='Ürün Fiyatı')

    class Meta:
        verbose_name = 'Sipariş Edilen Ürün'
        verbose_name_plural = 'Sipariş Edilen Ürünler'

    def __str__(self):
        return self.product.name

