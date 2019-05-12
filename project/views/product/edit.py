from django.views.generic import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Product
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from project.mixins import CheckDistributorObjectMixin


# ürün düzenleme
class ProductUpdateView(CheckDistributorObjectMixin, SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'content', 'cover', 'brand', 'price', 'stock_count', 'active')
    template_name = "project/product/edit.html"
    success_url = reverse_lazy('project:list-product')
    success_message = "%(name)s başarıyla düzenlendi."
    permission_required = ('project.manage_product',)

