from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_contact import Form_add_contact
from app_becas.models import Scholarship, Student
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Link_student2scholarship(View):

    def get(self, request, auto_id_student):

        search_term = request.GET.get('search', '')
        search_terms = search_term.split()  

        queries = [Q(summary__icontains=term) |
                   Q(name__icontains=term) |
                   Q(target_audiences__icontains=term) |
                   Q(benefits__icontains=term) for term in search_terms]


        student = Student.objects.get(auto_id=auto_id_student)
        scholarships = Scholarship.objects.all().filter(*queries)
        

        return render(request, 'link_student2scholarship.html', {
            'form': Form_add_contact(),
            'search_term': search_term,
            "student": student,
            "scholarships": scholarships
        })