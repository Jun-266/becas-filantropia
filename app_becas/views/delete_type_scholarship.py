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
        return render(request, 'delete_type_scholarship.html', {'tipos_beca': tipos_beca})

    def post(self, request):
        tipos_beca_seleccionados = request.POST.getlist('tipos_beca')
        for tipo_beca_name in tipos_beca_seleccionados:
            TypeScholarship.objects.filter(name=tipo_beca_name).delete()
        return redirect('delete_type_scholarship')