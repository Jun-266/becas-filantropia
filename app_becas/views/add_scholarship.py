from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.forms.scholarship_forms import ScholarshipForm



@method_decorator(login_required, name='dispatch')
class Add_scholarship(View):

    def get(self, request):
        form = ScholarshipForm()
        return render(request, '')
    
    def post (self,request):

        form = ScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista_o_url')
        else:
            return render(request, 'add_scholarship.html', {'form': form})
    