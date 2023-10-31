from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Student, Scholarship, Major

class Modify_student(View):
    def get(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        majors = Major.objects.all()
        return render(request, "modify_student.html", {"student": student, "majors": majors})

    def post(self, request, auto_id):
            student = Student.objects.get(auto_id=auto_id)
            student.code = request.POST['code']
            student.name = request.POST['name']
            student.lastname = request.POST['lastname']
            student.school = request.POST['school']
            student.email = request.POST['email']
            student.phone = request.POST['phone']
            student.first_semester = request.POST['first_semester']
            student.last_semester = request.POST['last_semester']
            student.major = Major.objects.get(auto_id = request.POST['major_select'])
            student.save()
            return redirect("manage_student")
