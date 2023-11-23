from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_donor import Form_add_donor
from app_becas.models import Donor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Manage_donor(View):

    def get(self, request):
        search_term = request.GET.get('search', '')
        donors = Donor.objects.filter(
            Q(enterprise_name__icontains=search_term)
        )
        return render(request, 'manage_donor.html', {
            'donors': donors,
            'form': Form_add_donor(),
            'search_term': search_term
        })

    def post(self, request):
        Donor.objects.create(enterprise_name=request.POST['enterprise_name'])
        return HttpResponseRedirect(request.path)