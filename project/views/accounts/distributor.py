from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from project.models import Distributor
from django.db.models import Q
from django.shortcuts import render, redirect


class DistributorRoleView(LoginRequiredMixin, View):

    def get(self, request, pk=None):

        role_page = request.session.get('role_page', False)

        if role_page == 'distributor':
            distributor = Distributor.objects.get(pk=pk)
        else:
            distributor = Distributor.objects.filter((Q(author=request.user) | Q(staff=request.user)) & Q(id=pk)).first()

            if distributor:
                request.session['role_page'] = 'distributor'
                request.session['role_id'] = pk
                request.session['role_name'] = distributor.name

            else:
                return redirect('role-list')

        context = {
            'distributor': distributor
        }

        return render(request=request, template_name='project/accounts/distributor.html', context=context)
