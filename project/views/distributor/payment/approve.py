from django.views.generic import UpdateView
from stocks.mixins import CheckDistributorObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from project.models import Payment
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Sipariş silme
class DistributorPaymentApproveView(CheckDistributorObjectMixin, SuccessMessageMixin, UpdateView):
    model = Payment
    fields = ['order_transfered']
    template_name = 'project/distributor/payment/approve.html'
    success_url = reverse_lazy('project:distributor-payment-order')
    success_message = "Sipariş başarıyla güncellendi."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.order_transfered:
            return redirect('project:distributor-list-order')

        return super(DistributorPaymentApproveView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.order_transfered:
            return redirect('project:distributor-list-order')

        return super(DistributorPaymentApproveView, self).post(request, *args, **kwargs)
