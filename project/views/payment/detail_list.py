from django.views.generic import ListView
from project.models import Payment, Distributor
from stocks.mixins import CheckDealerMixin
from django.db.models import F, Sum, FloatField, Count, Q, Value
from django.db.models.functions import Coalesce


# Sipariş listeleme
class PaymentDistributorListView(CheckDealerMixin, ListView):
    model = Distributor
    template_name = "project/payment/detail_list.html"
    context_object_name = 'distributor_list'

    def get_queryset(self):

        queryset = Distributor.objects.prefetch_related('received_orders', 'received_payments').filter(
            dealers__id=self.role_id).annotate(
                total_payment_amount=Coalesce(Sum(
                    'received_payment__amount',
                    only=Q(received_payment__payment_accepted='K'),
                    output_field=FloatField()
                ), Value(0)),
                total_order_amount=Coalesce(Sum(
                    F('received_order__ordered_item__item_price') * F('received_order__ordered_item__item_count'),
                    only=Q(received_order__order_transfered=True),
                    output_field=FloatField()
                ), Value(0))
            )

        return queryset

