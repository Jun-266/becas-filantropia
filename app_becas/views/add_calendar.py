from django import forms
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.forms.add_calendar import CreateNewTaskForm


@method_decorator(login_required, name='dispatch')
class Add_calendar(View):

  def get(self, request):
    return render(request, 'add_calendar.html', {
      'form': CreateNewTaskForm()
    })
