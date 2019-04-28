from django.db import models
from .company import Dealer, Distributor
from .product import Product


class Order(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Bayi')
    order_transfered = models.BooleanField(default=False, verbose_name='Nakliye Tamamlandı')
    order_cancelled = models.BooleanField(default=False, verbose_name='Sipariş İptal Edildi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sipariş Tarihi')
    updated = models.DateTimeField(auto_now=True, verbose_name='Sipariş Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Sipariş'
        verbose_name_plural = 'Siparişler'

    def __str__(self):
        return self.dealer.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Sipariş')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün')
    item_count = models.PositiveIntegerField(verbose_name='Ürün Adedi')
    item_price = models.FloatField(verbose_name='Ürün Fiyatı')

    class Meta:
        verbose_name = 'Sipariş Edilen Ürün'
        verbose_name_plural = 'Sipariş Edilen Ürünler'

    def __str__(self):
        return self.product.name


class Payment(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Bayi')
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distribütör')
    amount = models.FloatField(verbose_name='Miktar')

    class Meta:
        verbose_name = 'Ödeme'
        verbose_name_plural = 'Ödemeler'

    def __str__(self):
        return self.dealer.name
