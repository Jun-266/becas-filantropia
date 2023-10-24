from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Contact

class Modify_contact(View):
    def get(self, request, auto_id):
        contact = Contact.objects.get(auto_id=auto_id)
        return render(request, "modify_contact.html", {"contact": contact})

    def post(self, request, auto_id):
        identification =request.POST['identification']
        type = request.POST['type']
        email = request.POST['email']
        phone = request.POST['phone']
        contact = Contact.objects.get(auto_id = auto_id)
        contact.identification = identification
        contact.type = type
        contact.email = email
        contact.phone = phone
        contact.save()

        return redirect("manage_contact")
