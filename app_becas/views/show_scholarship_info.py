from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship


@method_decorator(login_required, name='dispatch')

class Show_scholarship_info(View):

    def get(self, request):
        scholarship = Scholarship.objects.get(auto_id = request.GET['auto_id'])
        # for delete method, if wants to be implemented in here
        # request.session['ss_scholarship_id'] = scholarship.auto_id.hex
        
        return render(request, 'show_scholarship_info.html', {
            'scholarship' : scholarship
        })

        