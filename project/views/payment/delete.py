from django.views.generic import DeleteView
from project.mixins import CheckDealerObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from project.models import Payment
from django.urls import reverse_lazy


# Sipariş silme
class PaymentDeleteView(CheckDealerObjectMixin, SuccessMessageMixin, DeleteView):
        model = Payment
        template_name = "project/payment/delete.html"
        success_url = reverse_lazy('project:list-payment')
        success_message = 'Ödeme başarıyla iptal edildi.'