from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from stocks.helpers import check_user_management_access


@login_required
def list_staff(request):

    queryset = check_user_management_access(request)

    if not queryset:
        return redirect('role-list')

    context = {
        'staff_list': queryset.staff.all()
    }

    return render(request=request, template_name='project/accounts/staff_list.html', context=context)
