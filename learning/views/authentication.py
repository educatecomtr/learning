from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views import View


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Kullanıcı girişi yapılmış
        pass
    else:
        # Kullanıcı girişi yapılmamış.
        pass


def logout(request):
    logout(request)


@login_required(login_url='/accounts/login/')
def view_profile(request):
    pass


class ViewProfile(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self):
        pass


def auth_method(request):

    if request.user.is_authenticated:
        # Do something for authenticated users.
        pass
    else:
        # Do something for anonymous users.
        pass


def email_check(user):
    return user.email.endswith('@example.com')


@user_passes_test(email_check, login_url='/login/')
def my_view(request):
    pass


class MyView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.email.endswith('@example.com')


class MyView(PermissionRequiredMixin, View):
    permission_required = 'learning.add_product'
    # çoğul yetki için
    permission_required = ('learning.add_product', 'learning.view_product')

