from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import TypeScholarship
from app_becas.forms.scholarship_forms import delete_type

@method_decorator(login_required, name='dispatch')

class DeleteTypeScholarship(View):

    def get(self, request):
        tipos_beca = TypeScholarship.objects.all()
        return render(request, 'delete_type_scholarship.html', {'tipos_beca': tipos_beca, 'form': delete_type})

    def post(self, request):
        
        tipo_de_beca_borrar = request.POST['delete_type_scholarship']

        print('okokoko')
        
        if tipo_de_beca_borrar:

            

            tipo_beca = TypeScholarship(name = tipo_de_beca_borrar)
            tipo_beca.delete()
            return redirect('delete_type_scholarship')
        
