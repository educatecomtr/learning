from django.views.generic import DeleteView
from project.models import Order
from project.feeds import OrderObject
from stocks.mixins import CheckDistributorObjectMixin


# Sipariş detay görüntüleme
class DistributorOrderDetailView(CheckDistributorObjectMixin, DeleteView):
    model = Order
    context_object_name = 'order'
    template_name = 'project/distributor/order/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DistributorOrderDetailView, self).get_context_data(**kwargs)

        ordered_items = self.object.ordered_items.prefetch_related('product').all()
        order_object = OrderObject(ordered_items)
        context['products'] = order_object
        return context