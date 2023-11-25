from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_contact import Form_add_contact
from app_becas.models import Contact, Donor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Manage_contact(View):

    def get(self, request, auto_id):

        search_term = request.GET.get('search', '')
        search_terms = search_term.split()  

        queries = [Q(auto_id__icontains=term) |
                   Q(name__icontains=term) |
                   Q(lastname__icontains=term) |
                   Q(identification__icontains=term) |
                   Q(type__icontains=term) |
                   Q(email__icontains=term) |
                   Q(phone__icontains=term) for term in search_terms]

        contacts = Contact.objects.filter(*queries)

        donor = Donor.objects.get(auto_id=auto_id)

        return render(request, 'manage_contact.html', {
            'form': Form_add_contact(),
            'search_term': search_term,
            "donor": donor,
            "contacts": contacts
        })

    def post(self, request, auto_id):
        donor = Donor.objects.get(auto_id=auto_id)
        form = Form_add_contact(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.donor = donor
            contact.save()
            

        return redirect(request.META.get('HTTP_REFERER', '/'))

