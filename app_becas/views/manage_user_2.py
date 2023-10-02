from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.db import models
from django.http import HttpResponse
from app_becas.my_forms.add_user import *
from app_becas.models import *


class Manage_user_2(View):

    def get(self, request):
        form = Add_user()
        return render(request, 'manage_user_2.html', {
            'form': form,
        })

    def post(self, request):
        form = Add_user(request.POST)
        if form.is_valid():
            try:
                App_becas_usuario(**form.cleaned_data).save()
                return redirect('')
            except IntegrityError:
                return render(request, 'manage_user_2.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya está agregado'
                })
        else:
            return render(request, 'manage_user_2.html', {
                'form': UserCreationForm,
                'error': 'Formulario invalido'
            })
