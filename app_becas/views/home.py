from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout


@method_decorator(login_required, name='dispatch')
class Home(View):

    def get(self, request):
        return render(request, 'home.html')

    def signout(request):
        logout(request)
        return redirect('')