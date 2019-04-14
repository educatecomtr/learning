from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools


class ProductManager(models.Manager):
    def active_products(self):
        return self.filter(active=1)


class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=1)


class PassiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=0)


class Product(models.Model):

    objects = ProductManager()
    actives = ActiveProductManager()
    passives = PassiveProductManager()

    # benzersiz_key = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Ürün İsmi', max_length=200)
    content = models.TextField(verbose_name='Ürün Açıklaması')
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', related_query_name='product')
    slug = models.SlugField(unique=True, editable=False)
    active = models.BooleanField(default=True)

    class Meta:
        # db_table = 'urunler'
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/product/%i/" % self.id

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not Product.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)

        super(Product, self).save()

    def delete(self):
        pass

    @property
    def summary(self):
        return self.content[:50]

    '''
    model yöneticisine taşındı
    
    @classmethod
    def active_products(cls):
        return cls.objects.filter(active=1)
    '''
    @staticmethod
    def static_summary(content):
        return content[:50]



