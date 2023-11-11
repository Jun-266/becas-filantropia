from django.shortcuts import get_object_or_404, redirect
from django.views import View
from app_becas.models import Donor, Scholarship

class Delete_donor_scholarship(View):
    def get(self, request, auto_id, scholarship_auto_id):
        donor = get_object_or_404(Donor, auto_id=auto_id)
        scholarship = get_object_or_404(Scholarship, auto_id=scholarship_auto_id)
        donor.scholarships.remove(scholarship)
        return redirect(request.META.get('HTTP_REFERER', '/'))