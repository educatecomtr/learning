from django.db import models
from .dealer import Dealer
from .distributor import Distributor


class Payment(models.Model):

    PAYMENT_CHOICES = (
        ('K', 'KABUL EDİLDİ'),
        ('R', 'RED EDİLDİ'),
        ('B', 'BEKLEMEDE')
    )

    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Bayi', related_name='given_payments', related_query_name='given_payment')
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distribütör', related_name='received_payments', related_query_name='received_payment')
    amount = models.FloatField(verbose_name='Miktar')
    payment_accepted = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='B', verbose_name='Ödeme Kabülü')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Ödeme Tarihi')

    class Meta:
        verbose_name = 'Ödeme'
        verbose_name_plural = 'Ödemeler'
        permissions = [('manage_payment', 'Ödeme yönetim izni')]

    def __str__(self):
        return self.dealer.name
