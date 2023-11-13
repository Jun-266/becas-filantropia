from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import MyUser


class Modify_user(View):
    def get(self, request, auto_id):
        user = MyUser.objects.get(auto_id=auto_id)
        return render(request, "modify_user.html", {"user": user})

    def post(self, request, auto_id):
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        rol = request.POST['rol']
        user = MyUser.objects.get(auto_id=auto_id)
        user.name = name
        user.lastname = lastname
        user.email = email
        user.phone = phone
        user.rol = rol
        user.save()

        return redirect("manage_user")
