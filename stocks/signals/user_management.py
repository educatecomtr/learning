from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


# Kullanıcı giriş yaptığında çalıştırılır
# Sessionda tutulan kullanıcı session bilgilerini sıfırlar.
@receiver(user_logged_in)
def user_logged_in(sender, user, request, **kwargs):
    request.session['role_page'] = False
    request.session['role_id'] = False


# Kullanıcı giriş yaptığında çalıştırılır
# Sessionda tutulan kullanıcı session bilgilerini sıfırlar.
@receiver(user_logged_out)
def user_logged_out(sender, user, request, **kwargs):
    request.session['role_page'] = False
    request.session['role_id'] = False

