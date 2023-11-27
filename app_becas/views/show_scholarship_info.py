from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.forms.scholarship_forms import ScholarshipFormModel
from app_becas.models import Scholarship
from app_becas.models import ScholarshipParams

@method_decorator(login_required, name='dispatch')

class Show_scholarship_info(View):

    def get(self, request):
        scholarship = Scholarship.objects.get(auto_id = request.GET['auto_id'])
        #params = ScholarshipParams.objects.filter(scholarship_id = scholarship.auto_id)
        # for delete method
        request.session['ss_scholarship_id'] = scholarship.auto_id

        return render(request, 'show_scholarship_info.html', {
            'scholarship' : scholarship,
            #'scholarship_params': params ,
        })
    
    def delete_scholarship(request):
        scholarship = Scholarship.objects.get(auto_id = request.session.get('ss_scholarship_id'))
        scholarship.delete()
        try:
            del request.session["ss_calendar_id"]
        except KeyError:
            pass
        # Here should be a notification
        return redirect('scholarship')
    
    def update_scholarship(request):
        x_record = get_object_or_404(Scholarship, auto_id = request.session.get('ss_scholarship_id'))
        form = ScholarshipFormModel(request.POST or None, instance=x_record)
        if form.is_valid():
            form.save()
            return redirect('scholarship')
        return render(request, 'scholarship_update.html', {'form': form})

        