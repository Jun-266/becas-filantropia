from django import forms

class Form_add_user(forms.Form):
    userId = forms.CharField(max_length=255)
    autoId = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=255)
    rol = forms.CharField(max_length=255)