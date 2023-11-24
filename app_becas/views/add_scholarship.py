from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.models import ConditionEnum
from app_becas.forms.scholarship_forms import ScholarshipForm


@method_decorator(login_required, name='dispatch')
class Add_scholarship(View):

    def get(self, request):
        form = ScholarshipForm()
        conditions_objects = ConditionEnum.objects.all()
        choices = [obj.name for obj in conditions_objects]

        return render(request, 'add_scholarship.html', {'form': form, 'choices': choices})

    def post(self, request):
        form = ScholarshipForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            summary = form.cleaned_data['summary']
            target_audiences = form.cleaned_data['target_audiences']
            benefits = form.cleaned_data['benefits']
            recomendations = form.cleaned_data['recomendations']
            additional_info = form.cleaned_data['additional_info']

            scholarship = Scholarship.objects.create(
                name = name,
                summary = summary,
                target_audiences = target_audiences,
                benefits = benefits,
                recomendations = recomendations,
                additional_info = additional_info,
            )

            truncated_target_audiences = scholarship.target_audiences
            truncated_benefits = scholarship.benefits[:20]
            truncated_recomendations = scholarship.recomendations[:3]
            truncated_additional_info = scholarship.additional_info[:20]

            # Pass the truncated fields to the template
            context = {
                'truncated_target_audiences': truncated_target_audiences,
                'truncated_benefits': truncated_benefits,
                'truncated_recomendations': truncated_recomendations,
                'truncated_additional_info': truncated_additional_info,
            }
        return render(request, 'scholarship.html')

            
        
