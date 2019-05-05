from project.models import Distributor, Dealer
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from stocks.helpers import check_superuser


@login_required
@user_passes_test(check_superuser)
def list_staff(request):
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
