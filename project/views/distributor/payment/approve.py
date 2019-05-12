from django.views.generic import UpdateView
from project.mixins import CheckDistributorObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from project.models import Payment
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Sipariş silme
class DistributorPaymentApproveView(CheckDistributorObjectMixin, SuccessMessageMixin, UpdateView):
    model = Payment
    fields = ['payment_accepted']
    template_name = 'project/distributor/payment/approve.html'
    success_url = reverse_lazy('project:distributor-list-payment')
    success_message = "Ödeme başarıyla onaylandı."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.payment_accepted != 'B':
            return redirect('project:distributor-list-payment')

        return super(DistributorPaymentApproveView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.payment_accepted != 'B':
            return redirect('project:distributor-list-payment')

        return super(DistributorPaymentApproveView, self).post(request, *args, **kwargs)
