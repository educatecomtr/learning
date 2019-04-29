from django.contrib import admin
from .models import Dealer, Distributor, Product, Order, Brand, Category, Payment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'created', 'active')
    list_filter = ('created', 'brand','distributor','active')


class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created','active')
    list_filter = ('created', 'author','active')


class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created','active')
    list_filter = ('created', 'author','active')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','created')
    list_filter = ('created',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('dealer','order_transfered','order_cancelled','created','updated')
    list_filter = ('dealer','order_transfered','order_cancelled','created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('distributor','dealer','amount','payment_accepted','created')
    list_filter = ('distributor','dealer','amount','payment_accepted','created')


admin.site.site_header = 'STOK YÖNETİM PANELİ'
admin.site.site_title = 'bir stok yöneticisi'
admin.site.index_title = 'Stok Yönetimi'

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Payment, PaymentAdmin)

# admin.site.unregister(Group)
