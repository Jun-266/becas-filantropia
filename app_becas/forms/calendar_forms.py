from django import forms
from app_becas.models import Calendar

class Form_add_calendar(forms.Form):
    '''
    inscription_start_date = forms.DateField(label= "Inicio de la Inscripción", widget=forms.SelectDateWidget)
    inscription_deadline = forms.DateField(label= "Fin de la Inscripción", widget=forms.SelectDateWidget)
    selection_start_date = forms.DateField(label= "Inicio de la Selección de participantes", widget=forms.SelectDateWidget)
    selection_deadline = forms.DateField(label= "Fin de la Selección de participantes", widget=forms.SelectDateWidget)
    interview_start_date = forms.DateField(label= "Inicio de Entrevistas a participantes", widget=forms.SelectDateWidget)
    interview_deadline = forms.DateField(label= "Fin de la Entrevistas a participantes", widget=forms.SelectDateWidget)
    publish_elected_start_date = forms.DateField(label= "Inicio de Publicación de resultados", widget=forms.SelectDateWidget)
    publish_elected_deadline = forms.DateField(label= "Fin de Publicación de resultados", widget=forms.SelectDateWidget)
    '''

class Calendar_form_model(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ["auto_id",
                  "calendar_type_id",
                  "scholarship_id",
                  "inscription_start_date", 
                  "inscription_deadline",
                  "selection_start_date",
                  "selection_deadline",
                  "interview_start_date",
                  "interview_deadline",
                  "publish_elected_start_date",
                  "publish_elected_deadline",
                  ]