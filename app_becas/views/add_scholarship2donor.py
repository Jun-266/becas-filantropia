from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_contact import Form_add_contact
from app_becas.models import Scholarship, Donor, ScholarshipApplication
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Add_scholarship2donor(View):

    def get(self, request, auto_id_donor, auto_id_scholarship):

        donor = Donor.objects.get(auto_id=auto_id_donor)
        donor.scholarships.add(auto_id_scholarship)

        return redirect(f"/manage_donor/modify_donor/{donor.auto_id}/manage_scholarship/")
