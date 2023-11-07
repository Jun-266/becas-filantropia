from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Student, Scholarship, Major, ScholarshipApplication, ApplicationStatus


class Modify_student(View):
    def get(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        majors = Major.objects.all()
        context = {
            "student": student,
            "majors": majors,
        }
        return render(request, "modify_student.html", context)

    def post(self, request, auto_id):
        action = request.POST.get("action", None)

        if action == "asociar_beca":
            return self.asociar_beca(request, auto_id)
        elif action == "update_status":
            return self.update_status(request, auto_id)
        else:
            student = Student.objects.get(auto_id=auto_id)
            student.code = request.POST.get("code")
            student.name = request.POST.get("name")
            student.lastname = request.POST.get("lastname")
            student.school = request.POST.get("school")
            student.email = request.POST.get("email")
            student.phone = request.POST.get("phone")
            student.first_semester = request.POST.get("first_semester")
            student.last_semester = request.POST.get("last_semester")
            student.major = Major.objects.get(auto_id=request.POST.get("major_select"))
            student.save()
            return redirect("manage_student")

    def asociar_beca(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        scholarship_id = request.POST.get("student_scholarship")
        scholarship = Scholarship.objects.get(auto_id=scholarship_id)

        application_status = ApplicationStatus.objects.get(type="En proceso")

        ScholarshipApplication.objects.create(
            student=student,
            scholarship=scholarship,
            application_status=application_status,
        )

        return HttpResponseRedirect(request.path)
    
    def update_status(self, request, auto_id_student):
        student = Student.objects.get(auto_id=auto_id_student)

        for application in student.scholarshipapplication_set.all():
            application_id = application.auto_id
            status = request.POST.get(f"status_{application_id}")
            application_status = ApplicationStatus.objects.get(type=status)
            application.application_status = application_status
            application.application_status.save()
            application.save()

        return HttpResponseRedirect(request.path)





