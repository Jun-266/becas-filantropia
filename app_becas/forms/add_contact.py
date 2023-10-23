from django import forms

class Form_add_contact(forms.Form):
    auto_id = forms.CharField(max_length=255)
    identification = forms.CharField(max_length=255)
    type = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)