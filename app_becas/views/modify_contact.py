from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from app_becas.models import Contact, Donor

class Modify_contact(View):
    def get(self, request, auto_id, contact_auto_id):
        contact = get_object_or_404(Contact, auto_id=contact_auto_id)
        return render(request, "modify_contact.html", {"contact": contact})

    def post(self, request, auto_id, contact_auto_id):

        contact = Contact.objects.get(auto_id = contact_auto_id)

        identification =request.POST['identification']
        name =request.POST['name']
        lastname =request.POST['lastname']
        type = request.POST['type']
        email = request.POST['email']
        phone = request.POST['phone']
        
        contact.name = name
        contact.lastname = lastname
        contact.identification = identification
        contact.type = type
        contact.email = email
        contact.phone = phone
        contact.save()

        return HttpResponseRedirect('/manage_donor/modify_donor/{}/manage_contact/'.format(auto_id))
