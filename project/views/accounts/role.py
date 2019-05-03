from django.views import View
from django.shortcuts import render
from project.models import Dealer, Distributor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.models import User


class RoleView(LoginRequiredMixin, View):

    def get(self, request):
        request.session['role_page'] = False
        request.session['role_id'] = False

        dealers = Dealer.objects.filter(Q(author=request.user) | Q(staff=request.user)).distinct()
        distributors = Distributor.objects.filter(Q(author=request.user) | Q(staff=request.user)).distinct()

        context = {
            'dealers': dealers,
            'distributors': distributors,
        }

        return render(request=request, template_name='project/accounts/role.html', context=context)


