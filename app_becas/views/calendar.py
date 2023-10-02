from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Calendar as Calendar_obj


@method_decorator(login_required, name='dispatch')
class Calendar(View):
    
    def get(self, request):
         # calendar = list(Project.objects.values())
        calendars = Calendar_obj.objects.all()
        return render(request, 'calendar.html', {
            'calendars': calendars
        })
        
