from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.forms.scholarship_forms import ScholarshipForm



@method_decorator(login_required, name='dispatch')
class Add_scholarship(View):

    def get(self, request):
        
        lista = [('Excelencia', 'Excelencia'), ('Logros y Representantes', 'Logros y Representantes'),
                ('Colaboradores', 'Colaboradores'), ('Especial', 'Especial'),
               ('Familiar y Minorías', 'Familiar y Minorías')]
    
        return render(request, 'add_scholarship.html',{
            'lista': lista
        })
    
    def post (self,request):

        Scholarship.objects.create(
                                   name = request.POST['name'],
                                   description = request.POST['description'],
                                   amount = request.POST['amount'],
                                   type_scholarship = request.POST['type_scholarship'])
        
        return redirect('scholarship')