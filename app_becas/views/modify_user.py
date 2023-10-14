from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import My_user

class Modify_user(View):
    def get(self, request, autoId):
        user = My_user.objects.get(autoId=autoId)
        return render(request, "modify_user.html", {"user": user})

    def post(self, request, autoId):
        name =request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        rol = request.POST['rol']
        user = My_user.objects.get(autoId = autoId)
        user.name = name
        user.lastname = lastname
        user.email = email
        user.phone = phone
        user.rol = rol
        user.save()

        return redirect("manage_user")
