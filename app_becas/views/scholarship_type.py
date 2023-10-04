from django.shortcuts import render
from app_becas.models import ScholarshipType

main_dir = '../templates/scholarship_type_management/'


def home_scholarship(request):
    sch_types = ScholarshipType.objects.all()
    return render(request, main_dir + 'scholarship_type_home.html', {
        'scholarship_types': sch_types
    })
