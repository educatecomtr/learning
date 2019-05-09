from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Product
from stocks.mixins import CheckDistributorMixin


# ürün listeleme
class ProductListView(CheckDistributorMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = "project/product/list.html"
    context_object_name = 'product_list'
    ordering = ['-created']
    permission_required = ('project.manage_product',)
    paginate_by = 10

    def get_queryset(self):
        distributor_id = self.request.session.get('role_id')
        return self.model.objects.filter(distributor_id=distributor_id)

