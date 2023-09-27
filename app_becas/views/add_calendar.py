from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.forms.calendar_forms import Form_add_calendar
from app_becas.models import Calendar


@method_decorator(login_required, name='dispatch')
class Add_calendar(View):


    def get(self, request):
        #Show form
        return render(request, 'add_calendar.html',{
            'form': Form_add_calendar()
        })
    
    def post(self, request):
        #print(request.POST)
        Calendar.objects.create(inscription_start_date =request.POST['inscription_start_date'],
                                inscription_deadline = request.POST['inscription_deadline'],
                                selection_start_date = (request.POST['selection_start_date_year'],request.POST['selection_start_date_month'],request.POST['selection_start_date_day']))
        
        return redirect('')
        