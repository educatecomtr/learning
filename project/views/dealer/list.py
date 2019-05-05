from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from project.models import Dealer
from stocks.mixins import CheckDistributorMixin


class DealerListView(CheckDistributorMixin, PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Dealer
    template_name = "project/dealer/list.html"
    context_object_name = 'dealer_list'
    ordering = ['-created']
    permission_required = ('project.manage_dealer',)

    def get_queryset(self):
        distributor_id = self.request.session.get('role_id')
        return self.model.objects.filter(distributor__id=distributor_id)

