from django.views.generic import ListView
from project.models import Payment, Dealer
from stocks.mixins import CheckDistributorMixin


# Sipariş listeleme
class DistributorPaymentListView(CheckDistributorMixin, ListView):
    model = Payment
    template_name = "project/distributor/payment/list.html"
    context_object_name = 'payment_list'

    def get_queryset(self):

        dealer = self.request.GET.get('dealer', False)
        status = self.request.GET.get('status', False)

        queryset = self.model.objects.select_related('dealer')

        if dealer:
            queryset = queryset.filter(dealer_id=int(dealer))

        if status:
            queryset = queryset.filter(payment_accepted=status)

        return queryset.filter(distributor_id=self.role_id).order_by('-created').all()

    def get_context_data(self, **kwargs):
        context = super(DistributorPaymentListView, self).get_context_data(**kwargs)

        dealer = self.request.GET.get('dealer', False)
        context['dealers'] = Dealer.objects.filter(distributor__id=self.role_id)
        context['filter_dealer'] = int(dealer) if dealer else False

        status = self.request.GET.get('status', False)
        context['status'] = (
            ('K', 'KABUL EDİLDİ'),
            ('R', 'RED EDİLDİ'),
            ('I', 'İPTAL EDİLDİ'),
            ('B', 'BEKLEMEDE')
        )
        context['filter_status'] = status if status else False

        return context
