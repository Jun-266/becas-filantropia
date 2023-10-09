'''''

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.db import models
from django.http import HttpResponse
from app_becas.forms.add_user import Form_add_user
from app_becas.models import My_user


class Modify_user(View):

    def get(self, request, autoId):

        users = My_user.objects.all()

        return render(request, 'manage_user_2.html', {
            'users': users, 
            'form': Form_add_user()
        })

    def post(self, request):

        My_user.objects.create( userId =request.POST['userId'],
                                name =request.POST['name'],
                                lastname = request.POST['lastname'],
                                email = request.POST['email'],
                                phone = request.POST['phone'],
                                rol = request.POST['rol'])
        return redirect('manage_user')
'''