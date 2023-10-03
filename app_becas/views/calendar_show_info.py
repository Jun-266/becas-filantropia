from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Calendar as Calendar_obj

@method_decorator(login_required, name='dispatch')
class Calendar_show_info(View):

    def get(self, request):
        # calendar = list(Calendar.objects.values())
        calendar = Calendar_obj.objects.get(auto_id = request.GET['auto_id'])
        #calendar = self
        return render(request, 'calendar_show_info.html', {
            'calendar': calendar
        })