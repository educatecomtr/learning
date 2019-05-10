from django.views.generic import DetailView
from project.models import Distributor
from stocks.mixins import CheckDealerMixin
from django.db.models import F, Sum, FloatField, Count


# Sipariş detay görüntüleme
class PaymentDistributorDetailView(CheckDealerMixin, DetailView):
    model = Distributor
    context_object_name = 'distributor'
    template_name = 'project/payment/detail.html'

    def get_context_data(self, **kwargs):

        context = super(PaymentDistributorDetailView, self).get_context_data(**kwargs)

        queryset_payment = self.object.received_payments.filter(payment_accepted='K')

        context['order_amount'] = 0
        context['order_count'] = 0
        context['payment_amount'] = 0
        context['payment_count'] = 0

        if queryset_payment is not None:
            payment = queryset_payment.aggregate(total_payment_amount=Sum('amount'), total_payment_count=Count('amount'))
            context['payment_amount'] = payment['total_payment_amount']
            context['payment_count'] = payment['total_payment_count']

        queryset_order = self.object.received_orders.filter(order_transfered=True)

        if queryset_order is not None:
            order = queryset_order.aggregate(total_order_amount=Sum(F('ordered_item__item_price')*F('ordered_item__item_count'), output_field=FloatField()), total_order_count=Count('ordered_item'))
            context['order_amount'] = order['total_order_amount']
            context['order_count'] = order['total_order_count']

        if context['order_amount'] is None:
            context['order_amount'] = 0

        if context['payment_amount'] is None:
            context['payment_amount'] = 0

        context['total_amount'] = context['payment_amount'] - context['order_amount']

        return context


