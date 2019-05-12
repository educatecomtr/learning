from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Dealer
from project.mixins import CheckDistributorMixin


# bayi listeleme
class DealerListView(CheckDistributorMixin, PermissionRequiredMixin, ListView):
    model = Dealer
    template_name = "project/distributor/dealer/list.html"
    context_object_name = 'dealer_list'
    ordering = ['-created']
    permission_required = ('project.manage_dealer',)

    def get_queryset(self):
        distributor_id = self.request.session.get('role_id')
        return self.model.objects.filter(distributor__id=distributor_id)

