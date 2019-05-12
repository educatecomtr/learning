from django.db import models
from project.mixins import SlugMixin


class Brand(SlugMixin):
    name = models.CharField(max_length=25, verbose_name='Ad')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')

    class Meta:
        verbose_name = 'Marka'
        verbose_name_plural = 'Markalar'

    def __str__(self):
        return self.name
