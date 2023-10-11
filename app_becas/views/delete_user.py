from django.shortcuts import redirect
from django.views import View
from app_becas.models import My_user

class Delete_user(View):
    def get(self, request, autoId):
        user = My_user.objects.get(autoId=autoId)
        user.delete()
        return redirect('manage_user')
