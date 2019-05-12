from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from project.helpers import check_user_management_access


# personel silme
@login_required
def delete_staff(request, pk=None):

    # BURADA KULLANICI SİLİNMİYOR İLİŞKİSİ SİLİNİYOR. SİLME İŞLEMİ ADMİN PANELDEN YAPILSIN.
    queryset = check_user_management_access(request)

    if not queryset:
        return redirect('role-list')

    if queryset.staff.filter(id=pk).exists():
        queryset.staff.remove(pk)

    return redirect('list-staff')
