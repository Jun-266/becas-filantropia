from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Donor, Scholarship, Contact

class Modify_donor(View):
    def get(self, request, auto_id):
        donor = Donor.objects.get(auto_id=auto_id)
        return render(request, "modify_donor.html", {"donor": donor})

    def post(self, request, auto_id):
        action = request.POST.get('action', None)
        if action == 'asociar_beca':
            return self.asociar_beca(request, auto_id)
        elif action == 'asociar_contacto':
            return self.asociar_contacto(request, auto_id)
        else:
            enterprise_name = request.POST['enterprise_name']
            donor = Donor.objects.get(auto_id=auto_id)
            donor.enterprise_name = enterprise_name
            donor.save()
            return redirect("manage_donor")

    def asociar_beca(self, request, auto_id):
        donor = Donor.objects.get(auto_id=auto_id)
        scholarship_id = request.POST['donor_scholarship']
        scholarship = Scholarship.objects.get(auto_id=scholarship_id)
        donor.scholarships.add(scholarship)
        donor.save()
        return redirect('manage_donor')

    def asociar_contacto(self, request, auto_id):
        donor = Donor.objects.get(auto_id=auto_id)
        contact_id = request.POST['donor_contact']
        contact = Contact.objects.get(auto_id=contact_id)
        donor.contacts.add(contact)
        donor.save()
        return redirect('manage_donor')
