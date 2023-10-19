from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Calendar as Calendar_obj
import uuid


@method_decorator(login_required, name='dispatch')
class Calendar(View):
    
    def get(self, request):
        calendars = Calendar_obj.objects.all()
        return render(request, 'calendar.html', {
            'calendars': calendars,
            'msg': "",
            'default_value_msg': "not-searched",
        }, )
    
    def post(self, request):
        #calendars = Calendar_obj.objects.filter(auto_id =  uuid.UUID(request.POST['to_search'])) 
        calendars = Calendar_obj.objects.filter(auto_id =  1) 
        
        if calendars: #Calendar not empty
            return render(request, 'calendar.html', {
                'calendars': calendars,
                'msg': "",
                'default_value_msg': calendars.__getitem__(0).scholarship_id,
            })
        else :
            msg_error = "No se encontró ninguna coincidencia"
            return render(request, 'calendar.html', {
                'calendars': calendars, 
                "msg": msg_error,
                'default_value_msg': request.POST['to_search'],
            })
        
    
        
        