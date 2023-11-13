from django import forms

class Form_add_student(forms.Form):
    autoId = forms.CharField(max_length=255)
    code = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    school = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)
    first_semester = forms.CharField(max_length=255)
    last_semester = forms.CharField(max_length=255)