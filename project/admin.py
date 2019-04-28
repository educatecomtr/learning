from django.contrib import admin
from .models import Dealer, Distributor, Product, Order, Brand, Category

# Register your models here.
admin.site.register(Dealer)
admin.site.register(Distributor)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Category)
