from django.views.generic import CreateView
from project.models import Payment
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from project.mixins import CheckDealerMixin


# bayi ekleme
class PaymentCreateView(CheckDealerMixin, SuccessMessageMixin, CreateView):
    model = Payment
    fields = ('amount', 'distributor')
    template_name = "project/payment/create.html"
    success_url = reverse_lazy('project:list-payment')
    success_message = "Ödeme kaydı başarıyla oluşturuldu."

    def form_valid(self, form):

        form.instance.payment_accepted = 'B'
        form.instance.dealer_id = self.role_id

        response = super(PaymentCreateView, self).form_valid(form)

        return response
