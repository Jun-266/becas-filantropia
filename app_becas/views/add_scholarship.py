from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.models import ConditionEnum
from app_becas.forms.scholarship_forms import ScholarshipForm, ScholarshipFormModel, conditionsForm1, conditionsForm3

@method_decorator(login_required, name='dispatch')
class Add_scholarship(View):

    def get(self, request):
        form = ScholarshipForm()
        conditions_objects = ConditionEnum.objects.all()
        choices = [obj.name for obj in conditions_objects]

        return render(request, 'add_scholarship.html', {'form': form, 'choices': choices})

    def post(self, request):
        #form = ScholarshipForm(request.POST)

        Scholarship.objects.create(
            name = request.POST['name'],
            calendar_id = request.POST['calendar_choice'],
            donor_id = request.POST['donor_choice'],
            summary = request.POST['summary'],
            target_audiences = request.POST['target_audiences'],
            benefits = request.POST['benefits'],
            recomendations = request.POST['recomendations'],
            renovation_info = request.POST['renovation_info'],
            additional_info = request.POST['additional_info'],
            post_img = request.POST['post_img'],
        )
        
        return redirect('scholarship')


         
        
