from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Student, Scholarship, Major

class Modify_student(View):
    def get(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        return render(request, "modify_student.html", {"student": student})

    def post(self, request, auto_id):
        action = request.POST.get('action', None)
        if action == 'asociar_beca':
            return self.asociar_beca(request, auto_id)
        elif action == 'asociar_major':
            return self.asociar_major(request, auto_id)
        else:
            #enterprise_name = request.POST['enterprise_name']
            #apellido
            #Demas datos del estudiante
            ##datos de major también para  actualizar
            #major = Major.objects.get(auto_id=major_id)
            #major.auto_id
            #major.name
            student = Student.objects.get(auto_id=auto_id)
            #student.enterprise_name = enterprise_name
            student.save()
            return redirect("manage_student")

    def asociar_major(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        major_id = request.POST['major_id']
        major = Major.objects.get(auto_id=major_id)
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
