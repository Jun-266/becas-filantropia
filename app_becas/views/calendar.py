from django import forms
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class Calendar(View):

    def get(self, request):
        return render(request, 'calendar.html')
    
    def add_calendar(request):
        return render(request, 'add_calendar.html', {
                'form': AuthenticationForm
            })
    
    def post(self, request):
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return HttpResponse('El usuario no existe')
        else:
            login(request, user)
            return redirect('home/')
