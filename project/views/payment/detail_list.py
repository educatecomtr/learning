from django.views.generic import ListView
from project.models import Payment, Distributor
from stocks.mixins import CheckDealerMixin


# Sipariş listeleme
class PaymentDistributorListView(CheckDealerMixin, ListView):
    model = Distributor
    template_name = "project/payment/detail_list.html"
    context_object_name = 'payment_list'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        pass
