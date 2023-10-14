from django.views import View
from django.shortcuts import render, redirect
from app_becas.forms.add_user import Form_add_user
from app_becas.models import My_user


class ManageUser2(View):

    def get(self, request):
        users = My_user.objects.all()

        return render(request, 'manage_user.html', {
            'users': users,
            'form': Form_add_user()
        })

    def post(self, request):
        My_user.objects.create(userId=request.POST['userId'],
                               name=request.POST['name'],
                               lastname=request.POST['lastname'],
                               email=request.POST['email'],
                               phone=request.POST['phone'],
                               rol=request.POST['rol'])
        return redirect('home')
