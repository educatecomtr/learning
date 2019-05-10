from django.views.generic import ListView
from project.models import Payment, Distributor
from stocks.mixins import CheckDealerMixin


# Sipariş listeleme
class PaymentListView(CheckDealerMixin, ListView):
    model = Payment
    template_name = "project/payment/list.html"
    context_object_name = 'payment_list'

    def get_queryset(self):

        distributor = self.request.GET.get('distributor', False)
        status = self.request.GET.get('status', False)

        queryset = self.model.objects.select_related('distributor')

        if distributor:
            queryset = queryset.filter(distributor_id=int(distributor))

        if status:
            queryset = queryset.filter(payment_accepted=status)

        return queryset.filter(dealer_id=self.role_id).order_by('-created').all()

    def get_context_data(self, **kwargs):
        context = super(PaymentListView, self).get_context_data(**kwargs)

        distributor = self.request.GET.get('distributor', False)
        context['distributors'] = Distributor.objects.filter(dealers__id=self.role_id)
        context['filter_distributor'] = int(distributor) if distributor else False

        status = self.request.GET.get('status', False)
        context['status'] = (
            ('K', 'KABUL EDİLDİ'),
            ('R', 'RED EDİLDİ'),
            ('I', 'İPTAL EDİLDİ'),
            ('B', 'BEKLEMEDE')
        )
        context['filter_status'] = status if status else False

        return context
