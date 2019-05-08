from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from project.models import Product, Dealer
from stocks.mixins import CheckDealerMixin
from django.views.generic.edit import FormMixin
from project.forms import AddProductToShoppingCartForm


# ürün detayı
class ShopDetailView(CheckDealerMixin, LoginRequiredMixin, FormMixin, DetailView):
    model = Product
    template_name = "project/shop/detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        context['form'] = AddProductToShoppingCartForm()
        return context
