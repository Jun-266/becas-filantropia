from django.shortcuts import render, redirect
from app_becas.models import TipoBeca  # Importa tu modelo de tipos de beca
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.forms.scholarship_forms import ScholarshipForm

@method_decorator(login_required, name='dispatch')

class add_type_scholarship(View):
    def get(self, request):
        tipos_beca = TipoBeca.objects.all()
        return render(request, 'tipos_beca.html', {'tipos_beca': tipos_beca})

    def post(self, request):
        # Procesa el formulario para agregar un nuevo tipo de beca
        nuevo_tipo_beca = request.POST.get('nuevo_tipo_beca')

        if nuevo_tipo_beca:
            # Crea un nuevo objeto TipoBeca y guárdalo en la base de datos
            tipo_beca = TipoBeca(nombre=nuevo_tipo_beca)
            tipo_beca.save()
            return redirect('tipos_beca')  # Redirecciona a la vista de tipos de beca

        # Si no se proporciona un nuevo tipo de beca, regresa a la vista con un mensaje de error
        tipos_beca = TipoBeca.objects.all()
        error_message = "Debes proporcionar un nuevo tipo de beca."
        return render(request, 'tipos_beca.html', {'tipos_beca': tipos_beca, 'error_message': error_message})

