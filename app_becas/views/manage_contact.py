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

    def get(self, request):
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

        return render(request, 'manage_contact.html', {
            'contacts': contacts,
            'form': Form_add_contact(),
            'search_term': search_term
        })

    def post(self, request):
        form = Form_add_contact(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            
            donor_id = request.POST.get('donor', None)
            if donor_id:
                donor = Donor.objects.get(auto_id=donor_id)
                contact.donor = donor

            contact.save()

        return HttpResponseRedirect(request.path)
