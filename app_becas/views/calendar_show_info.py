from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Calendar as Calendar_obj
#from django.http import HttpResponseRedirect

@method_decorator(login_required, name='dispatch')
class Calendar_show_info(View):

    def get(self, request):
        # calendar = list(Calendar.objects.values())
        calendar = Calendar_obj.objects.get(auto_id = request.GET['auto_id'])
        request.session['ss_calendar_id'] = calendar.auto_id
        return render(request, 'calendar_show_info.html', {
            'calendar' : calendar
        })
    
    def delete_calendar(request):
        calendar = Calendar_obj.objects.get(auto_id = request.session.get('ss_calendar_id'))
        calendar.delete()
        try:
            del request.session["ss_calendar_id"]
        except KeyError:
            pass
        # Here should be a notification
        return redirect('calendar')
    
  
        