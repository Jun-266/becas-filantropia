from typing import Any
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship as Scholarchip_obj


@method_decorator(login_required, name='dispatch')

class Scholarship(View):

    def get(self, request):
        return render(request, 'scholarship.html')

    def searchByName(name):
        for scholarship in self.becas:
            if scholarship["nombre"] == name:
                return scholarship
            return None

        