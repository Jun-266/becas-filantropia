from django.shortcuts import get_object_or_404, redirect
from django.views import View
from app_becas.models import Contact

class Delete_contact(View):

    def get(self, request, auto_id, contact_auto_id):
        contact = get_object_or_404(Contact, auto_id=contact_auto_id)
        contact.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))