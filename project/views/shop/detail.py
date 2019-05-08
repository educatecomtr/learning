from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from project.models import Product, Dealer
from stocks.mixins import CheckDealerMixin


# ürün detayı
class ShopDetailView(CheckDealerMixin, LoginRequiredMixin, DetailView):
    model = Product
    template_name = "project/shop/detail.html"
    context_object_name = 'product'
