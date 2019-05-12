from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project.forms import StaffUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from project.helpers import check_user_management_access


# personel düzenleme
@login_required
def edit_staff(request, pk=None):

    queryset = check_user_management_access(request)

    if not queryset:
        return redirect('role-list')

    instance = User.objects.get(pk=pk)

    if not queryset.staff.filter(id=instance.id).exists():
        return redirect('role-list')

    if request.POST:

        form = StaffUpdateForm(request.POST, instance=instance)

        if form.is_valid():
            password = form.cleaned_data['edit_password']

            if password:
                try:
                    validate_password(password, instance)

                    user = form.save(commit=False)
                    user.set_password(password)
                    user.save()
                    return redirect('list-staff')

                except ValidationError as error:
                    form.add_error('edit_password', error)
            else:
                user = form.save()
                return redirect('list-staff')
    else:
        form = StaffUpdateForm(instance=instance)

    return render(request, 'project/accounts/edit_staff.html', {'form': form})
