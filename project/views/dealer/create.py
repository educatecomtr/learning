from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from project.models import Dealer, Distributor
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from stocks.mixins import CheckDistributorMixin


# bayi ekleme
class DealerCreateView(CheckDistributorMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Dealer
    fields = ('name', 'content', 'author', 'address', 'phone', 'email', 'active')
    template_name = "project/dealer/create.html"
    success_url = reverse_lazy('project:list-dealer')
    success_message = "%(name)s başarıyla oluşturuldu."
    permission_required = ('project.manage_dealer',)

    def form_valid(self, form):
        response = super(DealerCreateView, self).form_valid(form)
        # Burada distributor - bayi ilişkisi kuruluyor.
        # Bunu signal ile de yapabiliriz
        distributor_id = self.request.session.get('role_id')
        self.object.distributors.add(distributor_id)

        return response

    def get_context_data(self, **kwargs):
        context = super(DealerCreateView, self).get_context_data(**kwargs)

        distributor = Distributor.objects.prefetch_related('staff').get(pk=self.role_id)

        context['form'].fields['author'].queryset = distributor.staff.all()
        return context