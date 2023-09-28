from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class Scholarship(View):

    def get(self, request):
        return render(request, 'scholarship.html')

    def searchByName(name):
        for scolarchip in self.becas:
            if scolarchip["nombre"] == name:
                return scolarchip
            return None

scolarchipFound = scolarchipFound.searchByName(scolarchipName)