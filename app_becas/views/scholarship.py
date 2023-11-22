from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship as Scholarship_obj


@method_decorator(login_required, name='dispatch')

class Scholarship(View):

    def get(self, request):
        scholarships = Scholarship_obj.objects.all()
        return render(request, 'scholarship.html', {
            'scholarships': scholarships,
        })
    
    def post(self, request):
        msg = ''
        scholarship = None
    
        try:
            scholarship = Scholarship_obj.objects.get(name=request.POST['nombre_beca'])
        except Scholarship_obj.DoesNotExist:
            msg = "La beca no esta registrada" 
            return render(request, 'scholarship.html', {'msg': msg})
        
        return render(request, 'scholarship.html', {'searched': scholarship, 'msg': msg})
        

        