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
        return render(request, 'add_scholarship.html', {'form': form})

    def post(self, request):
        form = ScholarshipForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            type_scholarship = form.cleaned_data['type_scholarship']
            '''
            new_type_scholarship = form.cleaned_data['new_type_scholarship']

            # Si se proporcionó un nuevo tipo de beca, agrégalo a las opciones existentes
            if new_type_scholarship:
                # Obtener las opciones actuales del campo "Tipo de Beca"
                type_scholarship_choices = form.fields['type_scholarship'].choices

                # Verificar si el nuevo tipo de beca ya existe en las opciones
                if (new_type_scholarship, new_type_scholarship) not in type_scholarship_choices:
                    # Si no existe, agrégalo a las opciones
                    type_scholarship_choices.append((new_type_scholarship, new_type_scholarship))
                    form.fields['type_scholarship'].choices = type_scholarship_choices

                # Establecer el nuevo tipo de beca como seleccionado
                type_scholarship = new_type_scholarship
            '''
            # Crear la beca con los datos proporcionados
            Scholarship.objects.create(
                name=name,
                description=description,
                amount=amount,
                type_scholarship=type_scholarship
            )
            return redirect('')
        else:
            return render(request, 'add_scholarship.html', {'form': form})
