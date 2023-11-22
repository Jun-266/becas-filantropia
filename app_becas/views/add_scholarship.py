from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.forms.scholarship_forms import ScholarshipForm


@method_decorator(login_required, name='dispatch')
class Add_scholarship(View):

    def get(self, request):
        form = ScholarshipForm()
        return render(request, 'add_scholarship.html', {'form': form})

    def post(self, request):
        form = ScholarshipForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            Scholarship.objects.create(
                name=name,
                description=description,
                amount=amount,
            )

        return redirect('scholarship')

            
        
