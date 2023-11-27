from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_contact import Form_add_contact
from app_becas.models import Scholarship, Student, ScholarshipApplication
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Linking_student2scholarship(View):

    def get(self, request, auto_id_student, auto_id_scholarship):

        student = Student.objects.get(auto_id=auto_id_student)
        scholarship = Scholarship.objects.get(auto_id=auto_id_scholarship)
        ScholarshipApplication.objects.create(scholarship=scholarship, student=student, application_status_id='En proceso')

        return redirect(f"/manage_student/modify_student/{student.auto_id}/")