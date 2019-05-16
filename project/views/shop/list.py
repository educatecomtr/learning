from django.views.generic import ListView
from project.models import Product, Dealer
from project.mixins import CheckDealerMixin
from project.forms import ProductSearchForm
from django.db.models import Q


# ürün listeleme
class ShopListView(CheckDealerMixin, ListView):
    model = Product
    form_class = ProductSearchForm
    template_name = "project/shop/list.html"
    context_object_name = 'shop_list'
    ordering = ['-created']
    paginate_by = 9

    def get_queryset(self):
        dealer_id = self.request.session.get('role_id')

        dealer = Dealer.objects.prefetch_related('distributors').get(pk=dealer_id)
        distributor_list = dealer.distributors.values_list('id', flat=True)

        queryset = self.model.objects.filter(distributor_id__in=distributor_list, active=1)

        form = self.form_class(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(Q(name__icontains=form.cleaned_data['name']) | Q(content__icontains=form.cleaned_data['name']))

        return queryset

