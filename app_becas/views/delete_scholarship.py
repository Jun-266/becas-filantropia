from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import View
from app_becas.models import Donor

class DeleteScholarship(View):
    def get(self, request, auto_id_donor, auto_id_scholarship):
        try:
            donor = Donor.objects.get(auto_id=auto_id_donor)
            donor.scholarships.remove(auto_id_scholarship)
        except Donor.DoesNotExist:
            pass
        
        return redirect(request.META.get('HTTP_REFERER', '/'))

