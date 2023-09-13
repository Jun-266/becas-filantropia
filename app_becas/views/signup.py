from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })


    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                return redirect('/signin')
            except IntegrityError:
                return HttpResponse('El usuario ya existe')
        else:
            return HttpResponse('Las contraseñas no son iguales')

