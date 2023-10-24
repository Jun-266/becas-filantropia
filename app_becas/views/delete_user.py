from django.shortcuts import redirect
from django.views import View
from app_becas.models import My_user

class Delete_user(View):
    def get(self, request, auto_id):
        user = My_user.objects.get(auto_id=auto_id)
        user.delete()
        return redirect('manage_user')
