from django.views.generic import DetailView
from project.models import Dealer, Distributor
from project.mixins import CheckDistributorMixin
from django.db.models import F, Sum, FloatField, Count, Value
from django.db.models.functions import Coalesce
from django.shortcuts import redirect


# Sipariş detay görüntüleme
class DistributorPaymentDealerDetailView(CheckDistributorMixin, DetailView):
    model = Dealer
    context_object_name = 'dealer'
    template_name = 'project/distributor/payment/detail.html'

    def get_object(self):
        # Distribütörler sadece kendi bayilerine ait ödeme detaylarını görebilmeli.
        # Kontrol edelim.
        distributor = Distributor.objects.prefetch_related('dealers').get(pk=self.role_id)
        dealer_list = distributor.dealers.values_list('id', flat=True)

        if self.kwargs['pk'] not in dealer_list:
            return redirect('role-list')

        instance = Dealer.objects.get(pk=self.kwargs['pk'])

        rp = instance.given_payments.filter(payment_accepted='K', distributor_id=self.role_id).aggregate(
            payment_amount=Coalesce(
                Sum(
                    'amount',
                    output_field=FloatField()
                ), Value(0)
            ),
            payment_count=Count(
                'id',
            )
        )

        instance.total_payment_amount = rp['payment_amount']
        instance.total_payment_count = rp['payment_count']

        rs = instance.given_payments.filter(payment_accepted='B', distributor_id=self.role_id).aggregate(
            payment_amount=Coalesce(
                Sum(
                    'amount',
                    output_field=FloatField()
                ), Value(0)
            ),
            payment_count=Count(
                'id',
            )
        )

        instance.waiting_payment_amount = rs['payment_amount']
        instance.waiting_payment_count = rs['payment_count']

        ro = instance.given_orders.filter(order_transfered=True, distributor_id=self.role_id).aggregate(
            order_amount=Coalesce(
                Sum(
                    F('ordered_item__item_price') * F('ordered_item__item_count'),
                    output_field=FloatField()
                ), Value(0)
            ),
            order_count=Count(
                'id',
            )
        )

        instance.total_order_amount = ro['order_amount']
        instance.total_order_count = ro['order_count']

        rb = instance.given_orders.filter(order_transfered=False, distributor_id=self.role_id).aggregate(
            order_amount=Coalesce(
                Sum(
                    F('ordered_item__item_price') * F('ordered_item__item_count'),
                    output_field=FloatField()
                ), Value(0)
            ),
            order_count=Count(
                'id',
            )
        )

        instance.waiting_order_amount = rb['order_amount']
        instance.waiting_order_count = rb['order_count']

        return instance

