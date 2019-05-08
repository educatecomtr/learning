from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Product
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from stocks.mixins import CheckDistributorMixin


# ürün ekleme
class ProductCreateView(CheckDistributorMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    fields = ('name', 'content', 'cover', 'brand', 'price', 'stock_count', 'active')
    template_name = "project/product/create.html"
    success_url = reverse_lazy('project:list-product')
    success_message = "%(name)s başarıyla oluşturuldu."
    permission_required = ('project.manage_product',)

    def form_valid(self, form):
        form.instance.distributor_id = self.request.session.get('role_id')
        return super(ProductCreateView, self).form_valid(form)





