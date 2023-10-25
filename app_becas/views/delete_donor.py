from django.shortcuts import redirect
from django.views import View
from app_becas.models import Donor

class Delete_donor(View):
    def get(self, request, auto_id):
        donor = Donor.objects.get(auto_id=auto_id)
        donor.delete()
        return redirect('manage_donor')