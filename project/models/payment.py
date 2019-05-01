from django.db import models
from .dealer import Dealer
from .distributor import Distributor


class Payment(models.Model):

    PAYMENT_CHOICES = (
        ('K', 'KABUL EDİLDİ'),
        ('R', 'RED EDİLDİ'),
        ('I', 'İPTAL EDİLDİ'),
        ('B', 'BEKLEMEDE')
    )

    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Bayi')
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distribütör')
    amount = models.FloatField(verbose_name='Miktar')
    payment_accepted = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='B', verbose_name='Ödeme Kabülü')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Ödeme Tarihi')

    class Meta:
        verbose_name = 'Ödeme'
        verbose_name_plural = 'Ödemeler'

    def __str__(self):
        return self.dealer.name
