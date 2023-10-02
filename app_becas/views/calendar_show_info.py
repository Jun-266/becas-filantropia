from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from app_becas.models import Calendar

@method_decorator(login_required, name='dispatch')
class Calendar_show_info(View):

    def get(self, request):
        return render(request, 'calendar.html')