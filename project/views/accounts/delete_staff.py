from project.models import Distributor, Dealer
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from stocks.helpers import check_superuser


@login_required
@user_passes_test(check_superuser)
def delete_staff(request, pk=None):
    role_id = request.session.get('role_id', False)
    role_page = request.session.get('role_page', False)

    if role_page == 'distributor':
        item = Distributor.objects.get(pk=role_id)
    else:
        item = Dealer.objects.get(pk=role_id)

    item.staff.remove(pk)

    return redirect('list-staff')
