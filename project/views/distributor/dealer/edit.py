from django.views.generic import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Dealer
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from project.mixins import CheckDealerDistributorMixin


# bayi düzenleme
class DealerUpdateView(CheckDealerDistributorMixin, SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Dealer
    fields = ('name', 'content', 'author', 'address', 'phone', 'email', 'active')
    template_name = "project/distributor/dealer/edit.html"
    success_url = reverse_lazy('project:distributor-list-dealer')
    success_message = "%(name)s başarıyla düzenlendi."
    permission_required = ('project.manage_dealer',)
