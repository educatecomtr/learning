from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from project.models import Product, Dealer
from stocks.mixins import CheckDealerMixin


class ShopListView(CheckDealerMixin, LoginRequiredMixin, ListView):
    model = Product
    template_name = "project/shop/list.html"
    context_object_name = 'shop_list'
    ordering = ['-created']
    paginate_by = 9

    def get_queryset(self):
        dealer_id = self.request.session.get('role_id')

        dealer = Dealer.objects.prefetch_related('distributors').get(pk=dealer_id)
        distributor_list = dealer.distributors.values_list('id', flat=True)

        return self.model.objects.filter(distributor_id__in=distributor_list, active=1)

