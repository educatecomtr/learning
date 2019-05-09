from django.views import View
from django.shortcuts import render, redirect
from project.models import Distributor
from django.contrib import messages
from project.forms import DealerRelationForm
from stocks.mixins import CheckDistributorMixin


class DealerRelationView(CheckDistributorMixin, View):
    success_message = 'Bayi başarıyla ilişkilendirildi.'
    error_message = 'Bayi ilişkilendirilemedi.'

    def get(self, request):
        form = DealerRelationForm()

        return render(request, 'project/dealer/attach.html', {'form': form})

    def post(self, request):
        form = DealerRelationForm(request.POST)

        if form.is_valid():
            dealer_id = form.cleaned_data['dealer'].id
            distributor = Distributor.objects.prefetch_related('dealers').get(pk=self.role_id)

            if not distributor.dealers.filter(id=dealer_id).exists():
                distributor.dealers.add(dealer_id)
                messages.success(self.request, self.success_message)
            else:
                messages.error(self.request, self.error_message)

            return redirect('project:list-dealer')

        return render(request, 'project/dealer/attach.html', {'form': form})
