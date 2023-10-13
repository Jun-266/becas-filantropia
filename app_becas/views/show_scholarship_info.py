from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.models import TypeScholarship
from app_becas.models import Calendar


@method_decorator(login_required, name='dispatch')

class Show_scholarship_info(View):

    def get(self, request):
        scholarship = Scholarship.objects.get(auto_id = request.GET['auto_id'])
        auto_id_hex = scholarship.auto_id.hex[:8]
        type_scholarship = TypeScholarship.objects.get(name = scholarship.type_scholarship)
        msg = ""
        calendar = None
        try:
            calendar = Calendar.objects.get(auto_id = scholarship.calendar_id)
        except:
            msg = "El cronograma asociado fue borrado, por favor actualiza el registro"
        # for delete method, if wants to be implemented in here
        # request.session['ss_scholarship_id'] = scholarship.auto_id.hex

        return render(request, 'show_scholarship_info.html', {
            'scholarship' : scholarship,
            'auto_id_hex' : auto_id_hex,
            'calendar' : calendar,
            'type_scholarship' : type_scholarship,
            'msg' : msg,
        })

        