from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from app_becas.forms.add_user import Form_add_user
from app_becas.models import MyUser


@method_decorator(login_required, name='dispatch')
class ManageUser(View):

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
        return redirect('manage_user')
