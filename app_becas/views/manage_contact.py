from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_contact import Form_add_contact
from app_becas.models import Contact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class Manage_contact(View):

    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'manage_contact.html', {
            'contacts': contacts,
            'form': Form_add_contact()
        })

    def post(self, request):

        Contact.objects.create( identification =request.POST['identification'],
                                type =request.POST['type'],
                                email = request.POST['email'],
                                phone = request.POST['phone'])
        return HttpResponseRedirect(request.path)
