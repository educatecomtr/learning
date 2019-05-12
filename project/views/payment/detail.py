from django.views.generic import DetailView
from project.models import Distributor, Dealer
from stocks.mixins import CheckDealerMixin
from django.db.models import F, Sum, FloatField, Count, Value
from django.db.models.functions import Coalesce
from django.shortcuts import redirect


# Sipariş detay görüntüleme
class PaymentDistributorDetailView(CheckDealerMixin, DetailView):
    model = Distributor
    context_object_name = 'distributor'
    template_name = 'project/payment/detail.html'

    def get_object(self):

        # Bayiler sadece kendi distribütörlerine ait ödeme detaylarını görebilmeli.
        # Kontrol edelim.
        dealer = Dealer.objects.prefetch_related('distributors').get(pk=self.role_id)
        distributor_list = dealer.distributors.values_list('id', flat=True)

        if self.kwargs['pk'] not in distributor_list:
            return redirect('role-list')

        instance = Distributor.objects.get(pk=self.kwargs['pk'])

        rp = instance.received_payments.filter(payment_accepted='K', dealer_id=self.role_id).aggregate(
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

        rs = instance.received_payments.filter(payment_accepted='B', dealer_id=self.role_id).aggregate(
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

        ro = instance.received_orders.filter(order_transfered=True, dealer_id=self.role_id).aggregate(
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

        rb = instance.received_orders.filter(order_transfered=False, dealer_id=self.role_id).aggregate(
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



