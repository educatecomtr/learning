from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from project.forms import StaffPermissionForm
from django.contrib.auth.models import User, Permission


# personel yetki düzenleme
@login_required
def edit_permissions(request, pk=None):
    # Bir kullanıcıya bir bayi ve distribütörde yetki verildiğinde. Diğerlerinde de aynı yetkiye sahip oluyor.
    # Bunun için yeni bir tablo oluşturulmalı ve object id si ile birlikte orada tutulmalı.
    # Bu kursumuzda bunun örneğini yapmayacağız. Siz isterseniz örnek olması açısından yapabilirsiniz.
    # Eğer yapmak istiyorsanız ileriki derslerde benzer yapılar kuracağız ve bilgi birikimi artacak.
    # Bittiğinde yapmaya çalışmanızı tavsiye ederim.

    # Burası için yetki sorgulaması yok herkes istediği kullanıcının ayarlarını değiştirebiliyor.
    role_page = request.session.get('role_page', False)
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

            if role_page == 'distributor':
                # Dealer Permission
                dealer_permission = form.cleaned_data['dealer_permission']
                dealer_db_permission = Permission.objects.get(codename='manage_dealer')
                if dealer_permission:
                    instance.user_permissions.add(dealer_db_permission)
                else:
                    instance.user_permissions.remove(dealer_db_permission)

            return redirect('list-staff')
    else:

        product_permission = instance.has_perm('project.manage_product')
        order_permission = instance.has_perm('project.manage_order')
        payment_permission = instance.has_perm('project.manage_payment')
        dealer_permission = instance.has_perm('project.manage_dealer')

        form = StaffPermissionForm(initial={'product_permission': product_permission,
                                            'dealer_permission': dealer_permission,
                                            'order_permission': order_permission,
                                            'payment_permission': payment_permission})

        if role_page == 'dealer':
            del form.fields['dealer_permission']

    return render(request, 'project/accounts/edit_permissions.html', {'form': form})
