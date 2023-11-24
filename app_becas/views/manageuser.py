from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from app_becas.forms.add_user import Form_add_user
from app_becas.models import MyUser
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class ManageUser(View):

    def get(self, request):
        
        search_term = request.GET.get('search', '')
        search_terms = search_term.split()  

        queries = [Q(auto_id__icontains=search_term) |
                   Q(user_id__icontains=term) |
                   Q(name__icontains=term) |
                   Q(lastname__icontains=term) |
                   Q(email__icontains=term) |
                   Q(phone__icontains=term) |
                   Q(rol__icontains=term) for term in search_terms]

        users = MyUser.objects.filter(*queries)

        return render(request, 'manage_user.html', {
            'users': users,
            'form': Form_add_user(),
            'search_term': search_term
        })

    def post(self, request):
        MyUser.objects.create(user_id=request.POST['user_id'],
                              name=request.POST['name'],
                              lastname=request.POST['lastname'],
                              email=request.POST['email'],
                              phone=request.POST['phone'],
                              rol=request.POST['rol'])
        return redirect('manage_user')
