from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Student, Scholarship, Major

class Modify_student(View):
    def get(self, request, auto_id):

        student = Student.objects.get(auto_id=auto_id)
        
        try:
            major = Major.objects.get(auto_id=student.major_id)
        except Major.DoesNotExist:
            major = Major.objects.create(
                        name = "",
                        description = ""
                        )
            major.save()

        student.major = major
        student.save()

        return render(request, "modify_student.html", {"student": student, "major": major})

    def post(self, request, auto_id):
        action = request.POST.get('action', None)
        if action == 'asociar_beca':
            return self.asociar_beca(request, auto_id)
        elif action == 'asociar_major':
            return self.asociar_major(request, auto_id)
        else:
            #enterprise_name = request.POST['enterprise_name']
            #major = Major.objects.get(auto_id=major_id)
            student = Student.objects.get(auto_id=auto_id)
            student.code = request.POST['code']
            student.name = request.POST['name']
            student.lastname = request.POST['lastname']
            student.school = request.POST['school']
            student.email = request.POST['email']
            student.phone = request.POST['phone']
            student.first_semester = request.POST['first_semester']
            student.last_semester = request.POST['last_semester']
            student.save()
            return redirect("manage_student")

    def asociar_major(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)

        #Actualizar major
        major = student.major
        major.name = request.POST['major_name']
        major.description = request.POST['major_description']
        major.save()
        #Link student-major
        student.major = major
        student.save()
        return redirect('manage_student')

#    def asociar_beca(self, request, auto_id):
 #       donor = Student.objects.get(auto_id=auto_id)
  #      scholarship_id = request.POST['student_scholarship']
   #     scholarship = Scholarship.objects.get(auto_id=scholarship_id)
    #    donor.scholarships.add(scholarship)
     #   donor.save()
      #  return redirect('manage_donor')
