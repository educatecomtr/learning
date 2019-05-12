from django.views.generic import UpdateView
from project.mixins import CheckDistributorObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from project.models import Order
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Sipariş silme
class DistributorOrderApproveView(CheckDistributorObjectMixin, SuccessMessageMixin, UpdateView):
    model = Order
    fields = ['order_transfered']
    template_name = 'project/distributor/order/approve.html'
    success_url = reverse_lazy('project:distributor-list-order')
    success_message = "Sipariş başarıyla güncellendi."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.order_transfered:
            return redirect('project:distributor-list-order')

        return super(DistributorOrderApproveView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.order_transfered:
            return redirect('project:distributor-list-order')

        return super(DistributorOrderApproveView, self).post(request, *args, **kwargs)
