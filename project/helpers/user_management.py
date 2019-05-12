from project.models import Distributor, Dealer


# kullanıcnın distribütör veya bayi yetkisi varmı kontrol edilir.
# eğer yetkisi varsa ilgili bayi veya distribütör bilgileri döndürülür
def check_user_management_access(request):
    role_id = request.session.get('role_id', False)
    role_page = request.session.get('role_page', False)

    if role_id is False or role_page is False:
        return False

    if role_page == 'distributor':
        queryset = Distributor.objects.get(pk=role_id)
    elif role_page == 'dealer':
        queryset = Dealer.objects.get(pk=role_id)
    else:
        return False

    if queryset.author_id != request.user.id:
        return False

    return queryset
