from django.views.generic import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Dealer
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from project.mixins import CheckDealerDistributorMixin


# bayi silme
class DealerDeleteView(CheckDealerDistributorMixin, SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Dealer
    template_name = "project/distributor/dealer/delete.html"
    success_url = reverse_lazy('project:distributor-list-dealer')
    success_message = "%(name)s başarıyla silindi."
    permission_required = ('project.manage_dealer',)
