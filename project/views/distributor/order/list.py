from django.views.generic import ListView
from project.models import Order, Dealer
from stocks.mixins import CheckDistributorMixin


# Sipariş onaylama

class DistributorOrderListView(CheckDistributorMixin, ListView):
    model = Order
    template_name = "project/distributor/order/list.html"
    context_object_name = 'order_list'

    def get_queryset(self):

        dealer = self.request.GET.get('dealer', False)
        status = self.request.GET.get('status', False)

        queryset = self.model.objects.select_related('dealer')

        if dealer:
            queryset = queryset.filter(dealer_id=int(dealer))

        if status == '1':
            queryset = queryset.filter(order_transfered=False, order_cancelled=False)
        elif status == '2':
            queryset = queryset.filter(order_transfered=True)

        return queryset.filter(distributor_id=self.role_id).order_by('-created').all()

    def get_context_data(self, **kwargs):
        context = super(DistributorOrderListView, self).get_context_data(**kwargs)

        dealers = Dealer.objects.filter(distributor__id=self.role_id)

        context['dealers'] = dealers

        dealer = self.request.GET.get('dealer', False)

        context['filter_dealer'] = False

        if dealer:
            context['filter_dealer'] = int(dealer)

        context['filter_status'] = self.request.GET.get('status', False)

        return context
