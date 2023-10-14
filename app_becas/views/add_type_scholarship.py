from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import TypeScholarship
from app_becas.forms.scholarship_forms import type_scholarship_form

@method_decorator(login_required, name='dispatch')

class AddTypeScholarship(View):

    def get(self, request):
        tipos_beca = TypeScholarship.objects.all()
        return render(request, 'add_type_scholarship.html', {'tipos_beca': tipos_beca ,'form' : type_scholarship_form})

    def post(self, request):

        nuevo_tipo_beca = request.POST['new_type_scholarship']

        if nuevo_tipo_beca:
           
            tipo_beca = TypeScholarship(name=nuevo_tipo_beca)
            tipo_beca.save()
            return redirect('add_type_scholarship') 

       
        tipos_beca = TypeScholarship.objects.all()
        error_message = "Debes proporcionar un nuevo tipo de beca."
        return render(request, 'add_type_scholarship.html', {'tipos_beca': tipos_beca, 'error_message': error_message})
    
    def delete_type_scholarship(request):
        type_scholarship = TypeScholarship.objects.get(name = request.GET('name_scholarship'))
        type_scholarship.delete()
        try:
            del request.session['name_scholarship']
        except KeyError:
            pass
        return redirect('add_type_scholarship')