from django.views import View
from django.shortcuts import render
from app_becas.forms.add_contact import Form_add_contact
from app_becas.models import Contact, Donor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Manage_scholarship(View):

    def get(self, request, auto_id):

        search_term = request.GET.get('search', '')
        search_terms = search_term.split()

        queries = [Q(summary__icontains=term) |
                   Q(name__icontains=term) |
                   Q(target_audiences__icontains=term) |
                   Q(benefits__icontains=term) for term in search_terms]


        donor = Donor.objects.get(auto_id=auto_id)
        scholarships = donor.scholarships.filter(*queries)

        return render(request, 'manage_scholarship.html', {
            'form': Form_add_contact(),
            'search_term': search_term,
            'scholarships': scholarships,
            "donor": donor
        })
