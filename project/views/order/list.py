from django.views.generic import ListView
from project.models import Order


# Sipariş onaylama
class OrderListView(ListView):
    model = Order
    template_name = "project/order/list.html"
    context_object_name = 'product_list'
    ordering = ['-created']

    def get_queryset(self):
        return self.model.select_related('distributor').all()
