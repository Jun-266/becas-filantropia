from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import TypeScholarship
from app_becas.forms.scholarship_forms import delete_type

@method_decorator(login_required, name='dispatch')


class DeleteTypeScholarship(View):
    template_name = 'delete_type_scholarship.html'

    def get(self, request):
        tipos_beca = TypeScholarship.objects.all()
        return render(request, self.template_name, {'tipos_beca': tipos_beca})

    def post(self, request):
        confirmed_deletion = request.POST.getlist('tipos_beca')
        
        if confirmed_deletion:
            TypeScholarship.objects.filter(name__in=confirmed_deletion).delete()

        return redirect('delete_type_scholarship')