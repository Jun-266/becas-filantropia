from typing import Any
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class Scholarship(View):

    becas =[]

    def __init__(self, name, description, type, amount):
        self.name = name
        self.description = description
        self.type = type
        self.amount = amount

    def get(self, request):
        return render(request, 'scholarship.html')

    def searchByName(name):
        for scolarchip in self.becas:
            if scolarchip["nombre"] == name:
                return scolarchip
            return None

    def addScolarchip(name,description,type,amount):
        new_scolarchip = {"nombre": name, "descripción": description, "monto": amount}
        becas.append(new_scolarchip)

    print(f"Se ha agregado una nueva beca: {name}")


scolarchipFound = scolarchipFound.searchByName(scolarchipName)