from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from app_becas.models import Major

class Add_major(View):
    def get(self, request):
        majors = Major.objects.all()
        return render(request, "add_major.html", {"majors": majors})

    def post(self, request):

        Major.objects.create( 
                            name = request.POST['major_name'],
                            description = request.POST['major_description']
                        )
        return redirect('manage_student')