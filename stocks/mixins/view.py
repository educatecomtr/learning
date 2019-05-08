from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


# Kullanıcı rol seçtiğinde sessiona role_id ve role_page eklemiştik.
# PermissionMixin diğer Mixinlerde sessiondan gelen verileri ve
# Bu veriler ile distributor ve bayi yetkisi olup olmadığını kontrol ediyoruz.
class PermissionMixin(LoginRequiredMixin):
    role_id = False
    role_page = False

    def get_role_session(self):
        self.role_id = self.request.session.get('role_id', False)
        self.role_page = self.request.session.get('role_page', False)

    def check_distributor_role(self):
        self.get_role_session()

        if not self.role_id or self.role_page != 'distributor':
            return False

        return True

    def check_dealer_role(self):
        self.get_role_session()
        if not self.role_id or self.role_page != 'dealer':
            return False

        return True

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect('role-list')


# Kullanıcının distributor rolü olup olmadığı kontrol edilir.
class CheckDistributorMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_distributor_role():
            return False

        return True


# Kullanıcının bayi rolü olup olmadığı kontrol edilir.
class CheckDealerMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_dealer_role():
            return False

        return True


# Kullanıcının distribütör rolu olup olmadığı kontrol edilir.
# Eğer distribütör rolü varsa ilgili bayi için yetkisi olup olmadığı kontrol edilir.
class CheckDealerDistributorMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_distributor_role():
            return False

        instance = self.get_object()

        if not instance.distributors.filter(id=self.role_id).exists():
            return False

        return True


# Kullanıcının distribütör rolu olup olmadığı kontrol edilir.
# Eğer distribütör rolü varsa ürün için yetkisi olup olmadığı kontrol edilir.
class CheckProductDistributorMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_distributor_role():
            return False

        instance = self.get_object()

        if instance.distributor_id != self.role_id:
            return False

        return True
