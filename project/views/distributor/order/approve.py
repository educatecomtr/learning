from django.views.generic import DeleteView
from stocks.mixins import CheckDealerObjectMixin
from django.contrib.messages.views import SuccessMessageMixin


# Sipariş silme
class DistributorOrderApproveView(CheckDealerObjectMixin, SuccessMessageMixin, DeleteView):
    pass
