from django.views.generic import ListView
from project.models import Order, Distributor
from stocks.mixins import CheckDealerMixin


# Sipariş onaylama
class OrderListView(CheckDealerMixin, ListView):
    model = Order
    template_name = "project/order/list.html"
    context_object_name = 'order_list'

    def get_queryset(self):

        distributor = self.request.GET.get('distributor', False)
        status = self.request.GET.get('status', False)

        queryset = self.model.objects.select_related('distributor')

        if distributor:
            queryset = queryset.filter(distributor_id=int(distributor))

        if status == '1':
            queryset = queryset.filter(order_transfered=False, order_cancelled=False)
        elif status == '2':
            queryset = queryset.filter(order_transfered=False, order_cancelled=True)
        elif status == '3':
            queryset = queryset.filter(order_transfered=True)

        return queryset.order_by('-created').all()

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)

        distributors = Distributor.objects.filter(dealers__id=self.role_id)

        context['distributors'] = distributors

        distributor = self.request.GET.get('distributor', False)

        context['filter_distributor'] = False

        if distributor:
            context['filter_distributor'] = int(distributor)

        status = self.request.GET.get('status', False)
        context['filter_status'] = self.request.GET.get('status', False)

        return context
