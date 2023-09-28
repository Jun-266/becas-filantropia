from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.forms.calendar_forms import Form_add_calendar
from app_becas.models import Calendar
from datetime import datetime


@method_decorator(login_required, name='dispatch')
class Add_calendar(View):


    def get(self, request):
        #Show form
        return render(request, 'add_calendar.html',{
            'form': Form_add_calendar()
        })
    
    def post(self, request):
        print(request.POST)
        Calendar.objects.create(inscription_start_date = request.POST['inscription_s'],
                                inscription_deadline = request.POST['inscription_d'],
                                selection_start_date = request.POST['selection_s'],
                                selection_deadline = request.POST['selection_d'],
                                interview_start_date = request.POST['interview_s'],
                                interview_deadline = request.POST['interview_d'],
                                publish_elected_start_date = request.POST['publish_elected_s'],
                                publish_elected_deadline = request.POST['publish_elected_d'])
        
        return redirect('')
        
