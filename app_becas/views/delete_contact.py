from django.shortcuts import redirect
from django.views import View
from app_becas.models import Contact

class Delete_contact(View):
    def get(self, request, auto_id):
        contact = Contact.objects.get(auto_id=auto_id)
        contact.delete()
        return redirect('manage_contact')