from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from project.models import Dealer
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from stocks.mixins import CheckDealerDistributorMixin


# bayi düzenleme
class DealerUpdateView(CheckDealerDistributorMixin, SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Dealer
    fields = ('name', 'content', 'author', 'address', 'phone', 'email', 'active')
    template_name = "project/dealer/edit.html"
    success_url = reverse_lazy('project:list-dealer')
    success_message = "%(name)s başarıyla düzenlendi."
    permission_required = ('project.manage_dealer',)
