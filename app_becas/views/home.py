from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from app_becas.models import Scholarship as Scholarship_obj
from app_becas.models import File 

@method_decorator(login_required, name='dispatch')
class Home(View):

    def get(self, request):
        scholarships = Scholarship_obj.objects.all()
        files = File.objects.all()
        return render(request, 'home.html', {
            'scholarships': scholarships,
            'files': files,
        })

    def signout(request):
        logout(request)
        return redirect('')