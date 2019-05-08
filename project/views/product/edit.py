from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from project.models import Product
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from stocks.mixins import CheckProductDistributorMixin


# ürün düzenleme
class ProductUpdateView(CheckProductDistributorMixin, SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'content', 'cover', 'brand', 'price', 'stock_count', 'active')
    template_name = "project/product/edit.html"
    success_url = reverse_lazy('project:list-product')
    success_message = "%(name)s başarıyla düzenlendi."
    permission_required = ('project.manage_product',)

