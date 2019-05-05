from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project.forms import StaffRelationForm
from stocks.helpers import check_user_management_access


@login_required
def attach_staff(request):

    queryset = check_user_management_access(request)

    if not queryset:
        return redirect('role-list')

    if request.method == 'POST':

        form = StaffRelationForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data['user'].id
            if not queryset.staff.filter(id=user_id).exists():
                queryset.staff.add(user_id)

            return redirect('list-staff')
    else:
        form = StaffRelationForm()

    return render(request, 'project/accounts/attach_staff.html', {'form': form})
