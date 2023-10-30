from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_student import Form_add_student
from app_becas.models import Student, Major
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class Manage_student(View):

    def get(self, request):
        students = Student.objects.all()
        return render(request, 'manage_student.html', {
            'students': students,
            'form': Form_add_student()
        })

    def post(self, request):

        Student.objects.create( code =request.POST['code'],
                                name =request.POST['name'],
                                lastname =request.POST['lastname'],
                                school =request.POST['school'],
                                email = request.POST['email'],
                                phone = request.POST['phone'],
                                first_semester = request.POST['first_semester'],
                                last_semester = request.POST['last_semester']
                                )

        return HttpResponseRedirect(request.path)
