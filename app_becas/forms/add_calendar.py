from django import forms

class Form_add_calendar(forms.Form):
    inscription_start_date = forms.CharField(label= "Fecha de inicio de la Inscripción", max_length=200)
    inscription_deadline = forms.CharField(label= "Fecha de terminación de la Inscripción", widget=forms.Textarea)