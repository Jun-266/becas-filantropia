from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_becas.forms.add_user import Form_add_user
from app_becas.models import My_user
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class Manage_user(View):

    def get(self, request):
        users = My_user.objects.all()
        return render(request, 'manage_user.html', {
            'users': users,
            'form': Form_add_user()
        })

    def post(self, request):

        My_user.objects.create( user_id =request.POST['user_id'],
                                name =request.POST['name'],
                                lastname = request.POST['lastname'],
                                email = request.POST['email'],
                                phone = request.POST['phone'],
                                rol = request.POST['rol'])
        return HttpResponseRedirect(request.path)
