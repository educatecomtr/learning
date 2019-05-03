from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from project.models import Distributor, Dealer
from django.db.models import Q


@login_required
@transaction.atomic
def create_staff(request):

    role_id = request.session.get('role_id', False)
    role_page = request.session.get('role_page', False)

    if role_id is False or role_page is False:
        return redirect('role-list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            if role_page == 'distributor':
                user.distributors.add(role_id)
            else:
                user.dealers.add(role_id)

            return redirect('role-list')
    else:
        form = UserCreationForm()

    return render(request, 'project/accounts/create_staff.html', {'form': form})


class StaffList(LoginRequiredMixin, View):

    def get(self, request):
        role_id = request.session.get('role_id', False)
        role_page = request.session.get('role_page', False)

        if role_page == 'distributor':
            queryset = Distributor.objects.prefetch_related('staff').get(pk=role_id)
        else:
            queryset = Dealer.objects.prefetch_related('staff').get(pk=role_id)

        context = {
            'staff_list': queryset.staff.all()
        }

        return render(request=request, template_name='project/accounts/staff_list.html', context=context)