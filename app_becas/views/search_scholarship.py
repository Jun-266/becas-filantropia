from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.forms.scholarship_forms import SearchScholarshipForm


@method_decorator(login_required, name='dispatch')

class SearchScholarship(View):

    def get(self, request):
        form = SearchScholarshipForm()
        return render(request, 'scholarship.html', {'form': form, 'scholarship': True})

    def post(self, request):
        form = SearchScholarshipForm(request.POST)
        msg = ''
        scholarship = None
        if form.is_valid():
            try:
                scholarship = Scholarship.objects.get(name=request.POST['nombre_beca'])
            except Scholarship.DoesNotExist:
                msg = "La beca no esta registrada" 
            
            return render(request, 'scholarship.html', {'scholarship': scholarship, 'msg': msg})
        return render(request, 'scholarship.html', {'form': form, 'search_scholarship_form': True})
        