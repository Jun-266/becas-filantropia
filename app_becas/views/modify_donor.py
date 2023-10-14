from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Donor

class Modify_donor(View):
    def get(self, request, auto_id):
        donor = Donor.objects.get(auto_id=auto_id)
        return render(request, "modify_donor.html", {"donor": donor})

    def post(self, request, auto_id):
        enterprise_name =request.POST['enterprise_name']
        donor = Donor.objects.get(auto_id = auto_id)
        donor.enterprise_name = enterprise_name
        donor.save()

        return redirect("manage_donor")
