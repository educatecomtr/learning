from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from project.forms import StaffCreationForm
from django.db import transaction
from stocks.helpers import check_superuser


@login_required
@user_passes_test(check_superuser)
@transaction.atomic
def create_staff(request):

    role_id = request.session.get('role_id', False)
    role_page = request.session.get('role_page', False)

    if role_id is False or role_page is False:
        return redirect('role-list')

    if request.method == 'POST':

        form = StaffCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            if role_page == 'distributor':
                user.distributors.add(role_id)
            else:
                user.dealers.add(role_id)

            return redirect('list-staff')
    else:
        form = StaffCreationForm()

    return render(request, 'project/accounts/create_staff.html', {'form': form})
