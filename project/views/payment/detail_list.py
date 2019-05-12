from django.views.generic import ListView
from project.models import Distributor
from project.mixins import CheckDealerMixin
from django.db.models import F, Sum, FloatField, Value
from django.db.models.functions import Coalesce


# Sipariş listeleme
class PaymentDistributorListView(CheckDealerMixin, ListView):
    model = Distributor
    template_name = "project/payment/detail_list.html"
    context_object_name = 'distributor_list'

    def get_queryset(self):

        queryset = Distributor.objects.prefetch_related('received_orders', 'received_payments').filter(dealers__id=self.role_id)

        for item in queryset:

            rp = item.received_payments.filter(payment_accepted='K', dealer_id=self.role_id).aggregate(
                payment_amount=Coalesce(
                    Sum(
                        'amount',
                        output_field=FloatField()
                    ), Value(0)
                )
            )

            item.total_payment_amount = rp['payment_amount']

            rs = item.received_payments.filter(payment_accepted='B', dealer_id=self.role_id).aggregate(
                payment_amount=Coalesce(
                    Sum(
                        'amount',
                        output_field=FloatField()
                    ), Value(0)
                )
            )

            item.waiting_payment_amount = rs['payment_amount']

            ro = item.received_orders.filter(order_transfered=True, dealer_id=self.role_id).aggregate(
                order_amount=Coalesce(
                    Sum(
                        F('ordered_item__item_price') * F('ordered_item__item_count'),
                        output_field=FloatField()
                    ), Value(0)
                )
            )

            item.total_order_amount = ro['order_amount']

        return queryset






