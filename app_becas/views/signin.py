from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


class Signin(View):

    def get(self, request):
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })

    def post(self, request):
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error_message': 'El usuario no existe'
            })
        else:
            login(request, user)
            return redirect('home/')