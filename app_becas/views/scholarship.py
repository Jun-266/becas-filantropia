<<<<<<< HEAD
from typing import Any
from django.shortcuts import redirect, render
=======
from django.shortcuts import render
>>>>>>> feat-40
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship as Scholarship_obj


@method_decorator(login_required, name='dispatch')

class Scholarship(View):

    def get(self, request):
        scholarships = Scholarship_obj.objects.all()
        return render(request, 'scholarship.html', {
<<<<<<< HEAD
            'scholarships' : scholarships
=======
            'scholarships': scholarships,
>>>>>>> feat-40
        })

    def search_by_name(request):
        request.session['ss_scholarship_name'] = scholarship.name
        name = request.session['ss_scholarship_name']
        for scholarship in self.becas:
            if scholarship["nombre"] == name:
                return scholarship
            return None
        
    def print_values(request):
        response = redirect("scholarship")
        response['Location'] += request.GET.get('name')
        return response.url
        