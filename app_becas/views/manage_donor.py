from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_donor import Form_add_donor
from app_becas.models import Donor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import datetime

@method_decorator(login_required, name='dispatch')
class Manage_donor(View):
    def get(self, request):
        search_term = request.GET.get('search', '')
        search_terms = search_term.split()

        queries = [Q(auto_id__icontains=term) |
                   Q(enterprise_name__icontains=term) |
                   Q(email__icontains=term) |
                   Q(phone__icontains=term) |
                   Q(city__icontains=term) |
                   Q(pais__icontains=term) |
                   Q(joined_date__icontains=term) for term in search_terms]

        donors = Donor.objects.filter(*queries)
        return render(request, 'manage_donor.html', {
            'donors': donors,
            'form': Form_add_donor(),
            'search_term': search_term
        })

    def post(self, request):
        form = Form_add_donor(request.POST)
        if form.is_valid():
            Donor.objects.create(
                enterprise_name=form.cleaned_data['enterprise_name'],
                city=form.cleaned_data['city'],
                pais=form.cleaned_data['pais'],
                joined_date=datetime.now(),
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            return HttpResponseRedirect(request.path)
        else:
            donors = Donor.objects.all()
            return render(request, 'manage_donor.html', {'donors': donors, 'form': form, 'search_term': ''})
