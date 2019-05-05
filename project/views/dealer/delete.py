from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from project.models import Dealer
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from stocks.mixins import CheckDealerDistributorMixin


class DealerDeleteView(CheckDealerDistributorMixin, SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Dealer
    template_name = "project/dealer/delete.html"
    success_url = reverse_lazy('project:list-dealer')
    success_message = "%(name)s başarıyla silindi."
    permission_required = ('project.manage_dealer',)
