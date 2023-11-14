from django.shortcuts import redirect
from django.views import View
from app_becas.models import Student

class Delete_student(View):
    def get(self, request, auto_id):
        student = Student.objects.get(auto_id=auto_id)
        student.delete()
        return redirect('manage_student')