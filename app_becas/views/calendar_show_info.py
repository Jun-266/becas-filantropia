from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.forms.calendar_forms import Calendar_form_model
from app_becas.models import Calendar as Calendar_obj
#from django.http import HttpResponseRedirect

@method_decorator(login_required, name='dispatch')
class Calendar_show_info(View):

    def get(self, request):
        calendar = Calendar_obj.objects.get(auto_id = request.GET['auto_id'])
        request.session['ss_calendar_id'] = calendar.auto_id.hex
        print ( "##" + request.session.get('ss_calendar_id'))
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
    
    def update_calendar(request):
        x_record = get_object_or_404(Calendar_obj, auto_id = request.session.get('ss_calendar_id'))
        form = Calendar_form_model(request.POST or None, instance=x_record)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'calendar_update.html', {'form': form})
    
        