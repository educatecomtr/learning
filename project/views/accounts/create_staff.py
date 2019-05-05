from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project.forms import StaffCreationForm
from django.db import transaction
from stocks.helpers import check_user_management_access


@login_required
@transaction.atomic
def create_staff(request):

    queryset = check_user_management_access(request)

    if not queryset:
        return redirect('role-list')

    if request.method == 'POST':

        form = StaffCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            role_id = request.session.get('role_id', False)
            role_page = request.session.get('role_page', False)

            if role_page == 'distributor':
                user.distributors.add(role_id)
            else:
                user.dealers.add(role_id)

            return redirect('list-staff')
    else:
        form = StaffCreationForm()

    return render(request, 'project/accounts/create_staff.html', {'form': form})
