from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class PermissionDeniedRedirectMixin:
    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect('role-list')


class CheckDistributorMixin(PermissionDeniedRedirectMixin, UserPassesTestMixin):

    def test_func(self):
        role_id = self.request.session.get('role_id', False)
        role_page = self.request.session.get('role_page', False)

        if not role_id or role_page != 'distributor':
            return False

        return True


class CheckDealerMixin(PermissionDeniedRedirectMixin, UserPassesTestMixin):

    def test_func(self):
        role_id = self.request.session.get('role_id', False)
        role_page = self.request.session.get('role_page', False)

        if not role_id or role_page != 'dealer':
            return False

        return True


class CheckDealerDistributorMixin(PermissionDeniedRedirectMixin, UserPassesTestMixin):

    def test_func(self):
        role_id = self.request.session.get('role_id', False)
        role_page = self.request.session.get('role_page', False)

        if not role_id or role_page != 'distributor':
            return False

        instance = self.get_object()

        if not instance.distributors.filter(id=role_id).exists():
            return False

        return True


class CheckProductDistributorMixin(PermissionDeniedRedirectMixin, UserPassesTestMixin):

    def test_func(self):
        role_id = self.request.session.get('role_id', False)
        role_page = self.request.session.get('role_page', False)

        if not role_id or role_page != 'distributor':
            return False

        instance = self.get_object()

        if instance.distributor_id != role_id:
            return False

        return True
