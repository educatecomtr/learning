from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from project.forms import StaffPermissionForm
from django.contrib.auth.models import User, Permission


@login_required
def edit_permissions(request, pk=None):

    instance = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = StaffPermissionForm(request.POST)

        if form.is_valid():
            # Product Permission
            product_permission = form.cleaned_data['product_permission']
            product_db_permission = Permission.objects.get(codename='manage_product')
            if product_permission:
                instance.user_permissions.add(product_db_permission)
            else:
                instance.user_permissions.remove(product_db_permission)

            # Dealer Permission
            dealer_permission = form.cleaned_data['dealer_permission']
            dealer_db_permission = Permission.objects.get(codename='manage_dealer')
            if dealer_permission:
                instance.user_permissions.add(dealer_db_permission)
            else:
                instance.user_permissions.remove(dealer_db_permission)

            # Order Permission
            order_permission = form.cleaned_data['order_permission']
            order_db_permission = Permission.objects.get(codename='manage_order')
            if order_permission:
                instance.user_permissions.add(order_db_permission)
            else:
                instance.user_permissions.remove(order_db_permission)

            # Payment Permission
            payment_permission = form.cleaned_data['payment_permission']
            payment_db_permission = Permission.objects.get(codename='manage_payment')
            if payment_permission:
                instance.user_permissions.add(payment_db_permission)
            else:
                instance.user_permissions.remove(payment_db_permission)

            return redirect('list-staff')
    else:

        product_permission = instance.has_perm('project.manage_product')
        dealer_permission = instance.has_perm('project.manage_dealer')
        order_permission = instance.has_perm('project.manage_order')
        payment_permission = instance.has_perm('project.manage_payment')

        form = StaffPermissionForm(initial={'product_permission': product_permission,
                                            'dealer_permission': dealer_permission,
                                            'order_permission': order_permission,
                                            'payment_permission': payment_permission})

    return render(request, 'project/accounts/edit_permissions.html', {'form': form})
