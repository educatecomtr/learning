from django.views.generic import DetailView
from project.models import Product
from project.mixins import CheckDealerMixin
from project.forms import AddProductToShoppingCartForm


# ürün detayı
class ShopDetailView(CheckDealerMixin, DetailView):
    model = Product
    template_name = "project/shop/detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        context['form'] = AddProductToShoppingCartForm()
        return context
