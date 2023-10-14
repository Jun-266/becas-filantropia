from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app_becas.models import Scholarship
from app_becas.forms.scholarship_forms import SearchScholarshipForm

@method_decorator(login_required, name='dispatch')

class SearchScholarship(View):

    def get(self, request):
        form = SearchScholarshipForm()
        return render(request, 'search_scholarship.html', {'form': form, 'search_scholarship': True})

    def post(self, request):
        form = SearchScholarshipForm(request.POST)

        if form.is_valid():
            scholarship_name = form.cleaned_data['scholarship_name']

            scholarships = Scholarship.objects.filter(name=scholarship_name)

            return render(request, 'search_scholarship.html', {'scholarships': scholarships})

        return render(request, 'search_scholarship.html', {'form': form, 'search_scholarship_form': True})