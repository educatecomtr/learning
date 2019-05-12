from django.views.generic import DeleteView
from project.models import Order
from django.urls import reverse_lazy
from project.mixins import CheckDealerObjectMixin
from django.contrib.messages.views import SuccessMessageMixin


# Sipariş silme
class OrderDeleteView(CheckDealerObjectMixin, SuccessMessageMixin, DeleteView):
    model = Order
    template_name = "project/order/delete.html"
    success_url = reverse_lazy('project:list-order')
    success_message = 'Sipariş başarıyla iptal edildi.'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        items = self.object.ordered_items.all()

        for item in items:
            item.product.stock_count = item.item_count + item.product.stock_count
            item.product.save()

        return super(OrderDeleteView, self).delete(request, *args, **kwargs)

