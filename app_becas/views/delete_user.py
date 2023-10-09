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

class Delete_user():

    def delete_user(request, autoId):
        user = My_user.objects.get(autoId=autoId)
        user.delete()
        redirect('/')