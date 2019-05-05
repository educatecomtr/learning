from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class PermissionMixin:
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


class CheckDistributorMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_distributor_role():
            return False

        return True


class CheckDealerMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_dealer_role():
            return False

        return True


class CheckDealerDistributorMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_distributor_role():
            return False

        instance = self.get_object()

        if not instance.distributors.filter(id=self.role_id).exists():
            return False

        return True


class CheckProductDistributorMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        if not self.check_distributor():
            return False

        instance = self.get_object()

        if instance.distributor_id != self.role_id:
            return False

        return True
