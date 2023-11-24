from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_student import Form_add_student
from app_becas.models import Student, Major, ApplicationStatus
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Manage_student(View):

    def get(self, request):

        search_term = request.GET.get('search', '')
        search_terms = search_term.split()

        queries = [Q(auto_id__icontains=term) |
                   Q(code__icontains=term) |
                   Q(name__icontains=term) |
                   Q(lastname__icontains=term) |
                   Q(school__icontains=term) |
                   Q(email__icontains=term) |
                   Q(phone__icontains=term) |
                   Q(first_semester__icontains=term) |
                   Q(last_semester__icontains=term) |
                   Q(major__name__icontains=term) for term in search_terms]

        students = Student.objects.filter(*queries)
        majors = Major.objects.all()

        try:
            Major.objects.get(auto_id=0)
        except Major.DoesNotExist:
            Major.objects.create(
                auto_id=0,
                name='NA',
                description='NA'
            )

        try:
            ApplicationStatus.objects.get(type="En proceso")
        except ApplicationStatus.DoesNotExist:

            ApplicationStatus.objects.create(
                type="Aprobada"
            )

            ApplicationStatus.objects.create(
                type="En proceso"
            )

            ApplicationStatus.objects.create(
                type="Denegada"
            )

            ApplicationStatus.objects.create(
                type="Concluida"
            )

        return render(request, 'manage_student.html', {
            'students': students,
            'majors': majors,
            'form': Form_add_student(),
            'search_term': search_term
        })

    def post(self, request):
        Student.objects.create(
            code=request.POST['code'],
            name=request.POST['name'],
            lastname=request.POST['lastname'],
            school=request.POST['school'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            first_semester=request.POST['first_semester'],
            last_semester=request.POST['last_semester'],
            major_id=request.POST['major_select'],
        )

        return HttpResponseRedirect(request.path)
