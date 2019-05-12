from django.views.generic import DetailView
from project.models import Distributor
from stocks.mixins import CheckDealerMixin
from django.db.models import F, Sum, FloatField, Count, Q, Value
from django.db.models.functions import Coalesce


# Sipariş detay görüntüleme
class PaymentDistributorDetailView(CheckDealerMixin, DetailView):
    model = Distributor
    context_object_name = 'distributor'
    template_name = 'project/payment/detail.html'

    def get_object(self):
        queryset = Distributor.objects.prefetch_related('received_payments', 'received_orders').filter(pk=self.kwargs['pk']).aggregate(
                total_payment_amount=Coalesce(Sum(
                    'received_payment__amount',
                    only=Q(received_payment__payment_accepted='K'),
                    output_field=FloatField()
                ), Value(0)),
                total_payment_count=Count(
                    'received_payment__amount',
                    only=Q(received_payment__payment_accepted='K'),
                    output_field=FloatField()
                ),
                total_order_amount=Coalesce(Sum(
                    F('received_order__ordered_item__item_price') * F('received_order__ordered_item__item_count'),
                    only=Q(received_order__order_transfered=True),
                    output_field=FloatField()
                ), Value(0)),
                total_order_count=Count(
                    'received_order__ordered_item',
                    only=Q(received_order__order_transfered=True)
                ),
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PaymentDistributorDetailView, self).get_context_data(**kwargs)
        query = Distributor.objects.get(pk=self.kwargs['pk'])
        context['distributor_name'] = query.name
        return context



