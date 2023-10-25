from django import forms

class Form_add_donor(forms.Form):
    autoId = forms.CharField(max_length=255)
    enterprise_name = forms.CharField(max_length=20)