from django.contrib import admin
from .models import Dealer, Distributor, Product, Order, Brand, Category


class ProductAdmin(admin.ModelAdmin):
    # fields = ('name',)
    # readonly_fields = ('name', )
    exclude = ('slug', )
    list_display = ('name', 'created')
    list_filter = ('created',)
    change_list_template = 'admin/learning/products_change_list.html'


admin.site.site_header = 'Stok Yönetimi'

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Dealer)
admin.site.register(Distributor)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Category)

# admin.site.unregister(Group)
