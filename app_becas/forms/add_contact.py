from django import forms
from app_becas.models import Contact

class Form_add_contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['identification', 'name', 'lastname', 'type', 'email', 'phone']