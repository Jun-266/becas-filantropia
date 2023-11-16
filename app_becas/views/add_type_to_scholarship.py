from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.models import TypeScholarship
from app_becas.forms.scholarship_forms import add_type_to_scholarship
from django.shortcuts import get_object_or_404


@method_decorator(login_required, name='dispatch')

class AddTypeToScholarship(View):
    
    def get(self, request):
        scholarship = get_object_or_404(Scholarship, auto_id=request.GET['auto_id'])
        request.session['auto_id'] = scholarship.auto_id
        types_scholarship = TypeScholarship.objects.all()

        return render(request, 'add_type_to_scholarship.html', 
                      {'scholarship': scholarship,
                       'types_scholarship': types_scholarship,
                       'form' : add_type_to_scholarship, })

    def post(self, request):
        scholarship = Scholarship.objects.get(auto_id = request.session.get('auto_id'))
        types_selected = request.POST.getlist('types')
        for type_x in types_selected:
            try:
                type_scholarship = TypeScholarship.objects.get(name=type_x.name)
                scholarship.types.add(type_scholarship)
            except TypeScholarship.DoesNotExist:
                # Manejar la situación en la que el tipo de beca no existe
                pass  # O puedes agregar un manejo de error según sea necesario
        return render(request, 'show_scholarship_info.html', {'auto_id': scholarship.auto_id})
