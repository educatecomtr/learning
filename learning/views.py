from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from learning.models import Product, Category, UserDetail

product = Product.objects.first()
print(product.author.name)

product = Product.objects.select_related('author').first()
print(product.author.name)


products = Product.objects.all()
for p in products:
    print(p.author.name)

products = Product.objects.select_related('author').all()
for p in products:
    print(p.author.name)


users = User.objects.all()
for u in users:
    print(u.products)

users = User.objects.prefetch_related('products').all()
for u in users:
    print(u.products)
