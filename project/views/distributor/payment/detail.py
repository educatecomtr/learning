from django.views.generic import ListView
from project.models import Dealer
from stocks.mixins import CheckDistributorObjectMixin


# Sipariş detay görüntüleme
class DistributorPaymentDealerDetailView(CheckDistributorObjectMixin, ListView):
    model = Dealer
    context_object_name = 'order'
    template_name = 'project/distributor/payment/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DistributorPaymentDealerDetailView, self).get_context_data(**kwargs)
        context['products'] = ''
        return context
