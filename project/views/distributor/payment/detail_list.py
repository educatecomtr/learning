from django.views.generic import ListView
from project.models import Dealer
from stocks.mixins import CheckDistributorMixin
from django.db.models import F, Sum, FloatField, Q, Value
from django.db.models.functions import Coalesce


# Sipariş detay görüntüleme
class DistributorPaymentDealerListView(CheckDistributorMixin, ListView):
    model = Dealer
    context_object_name = 'dealer_list'
    template_name = 'project/distributor/payment/detail_list.html'

    def get_queryset(self):

        queryset = Dealer.objects.prefetch_related('given_orders', 'given_payments').filter(distributor__id=self.role_id)

        for item in queryset:

            rp = item.given_payments.filter(payment_accepted='K', distributor_id=self.role_id).aggregate(
                payment_amount=Coalesce(
                    Sum(
                        'amount',
                        output_field=FloatField()
                    ), Value(0)
                )
            )

            item.total_payment_amount = rp['payment_amount']

            ro = item.given_orders.filter(order_transfered=True, distributor_id=self.role_id).aggregate(
                order_amount=Coalesce(
                    Sum(
                        F('ordered_item__item_price') * F('ordered_item__item_count'),
                        output_field=FloatField()
                    ), Value(0)
                )
            )

            item.total_order_amount = ro['order_amount']

        return queryset

