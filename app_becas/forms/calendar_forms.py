from django import forms
from datetime import date

class Form_add_calendar(forms.Form):
    inscription_start_date = forms.CharField(label= "Fecha de inicio de la Inscripción", max_length=200)
    inscription_deadline = forms.CharField(label= "Fecha de terminación de la Inscripción", max_length=200)
    selection_start_date = forms.DateField(label= "Inicio de la Selección de participantes", widget=forms.SelectDateWidget)