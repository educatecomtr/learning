from django.views import View
from django.shortcuts import render
from project.models import Dealer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class DealerRoleView(LoginRequiredMixin, View):

    def get(self, request, pk=None):

        role_page = request.session.get('role_page', False)

        if role_page == 'dealer':
            dealer = Dealer.objects.get(pk=pk)
        else:
            dealer = Dealer.objects.filter((Q(author=request.user) | Q(staff=request.user)) & Q(id=pk))

            if dealer:
                request.session['role_page'] = 'dealer'
                request.session['role_id'] = pk

        context = {
            'dealer': dealer
        }

        return render(request=request, template_name='project/accounts/dealer.html', context=context)
