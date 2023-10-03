import urllib
from django.shortcuts import redirect

from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Calendar as Calendar_obj


@method_decorator(login_required, name='dispatch')
class Calendar(View):
    
    def get(self, request):
         # calendar = list(Calendar.objects.values())
        calendars = Calendar_obj.objects.all()
        return render(request, 'calendar.html', {
            'calendars': calendars
        })
    
    def send_id(value):
        params = {
            'id': value,
        }
        url = 'calendar_show_info'

        response = redirect(url)
        if params:
            query_string = urllib.urlencode(params)
            response['Location'] += '?' + query_string
        return redirect(response)
        
        