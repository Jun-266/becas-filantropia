from typing import Any
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class Add_scholarship(View):

    def get(self, request):
        return render(request, 'add_scholarship.html')
    