from django.views.generic import DeleteView
from project.models import Order
from django.urls import reverse_lazy
from stocks.mixins import CheckDistributorObjectMixin
from django.contrib.messages.views import SuccessMessageMixin


# Sipariş silme
class DistributorOrderDeleteView(CheckDistributorObjectMixin, SuccessMessageMixin, DeleteView):
    model = Order
    template_name = "project/distributor/order/delete.html"
    success_url = reverse_lazy('project:distributor-list-order')
    success_message = 'Sipariş başarıyla iptal edildi.'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        items = self.object.ordered_items.all()

        for item in items:
            item.product.stock_count = item.item_count + item.product.stock_count
            item.product.save()

        return super(DistributorOrderDeleteView, self).delete(request, *args, **kwargs)

