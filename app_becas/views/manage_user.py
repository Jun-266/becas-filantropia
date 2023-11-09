from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from app_becas.forms.add_user import Form_add_user
from app_becas.models import MyUser


class Manage_user(View):

    def get(self, request):
        users = MyUser.objects.all()

        return render(request, 'manage_user.html', {
            'users': users,
            'form': Form_add_user()
        })

    def post(self, request):
        MyUser.objects.create(user_id=request.POST['user_id'],
                              name=request.POST['name'],
                              lastname=request.POST['lastname'],
                              email=request.POST['email'],
                              phone=request.POST['phone'],
                              rol=request.POST['rol'])
        return HttpResponseRedirect(request.path)
