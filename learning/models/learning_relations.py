from django.db import models
from django.contrib.auth.models import User
from learning.models import Product


class UserDetail(models.Model):

    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username + ' detail'


class Category(models.Model):
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product, related_name='categories', related_query_name='category')

