from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Student, Scholarship, Major, ScholarshipApplication, ApplicationStatus

class Modify_student(View):
    def get(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        majors = Major.objects.all()
        return render(request, "modify_student.html", {"student": student, "majors": majors})

    def post(self, request, auto_id):
        action = request.POST.get('action', None)
        if action == 'asociar_beca':
            return self.asociar_beca(request, auto_id)
        else:
            student = Student.objects.get(auto_id=auto_id)
            student.code = request.POST['code']
            student.name = request.POST['name']
            student.lastname = request.POST['lastname']
            student.school = request.POST['school']
            student.email = request.POST['email']
            student.phone = request.POST['phone']
            student.first_semester = request.POST['first_semester']
            student.last_semester = request.POST['last_semester']
            student.major = Major.objects.get(auto_id=request.POST['major_select'])
            student.save()
            return redirect("manage_student")
    
    def asociar_beca(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        scholarship_id = request.POST['student_scholarship']
        scholarship = Scholarship.objects.get(auto_id=scholarship_id)
        
        # Obten la instancia de ApplicationStatus con nombre "En proceso"
        application_status = ApplicationStatus.objects.get(type="En proceso")
        
        # Crea una ScholarshipApplication para el estudiante y la beca, y asigna la instancia de ApplicationStatus
        ScholarshipApplication.objects.create(student=student, scholarship=scholarship, application_status=application_status)
        
        return redirect('manage_student')
