from django import forms
from app_becas.models import Calendar

class Calendar_form_model(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ('__all__')
        labels = {
            'auto_id': 'ID ',
            'scholarship_name': 'Nombre de la Beca',
            'inscription_start_date': 'Fecha de Inicio de Inscripción',
            'inscription_deadline': 'Fecha Límite de Inscripción',
            'selection_start_date': 'Fecha de Inicio de Selección',
            'selection_deadline': 'Fecha Límite de Selección',
            'interview_start_date': 'Fecha de Inicio de Entrevista',
            'interview_deadline': 'Fecha Límite de Entrevista',
            'publish_elected_start_date': 'Fecha de Inicio de Publicación de Elegidos',
            'publish_elected_deadline': 'Fecha Límite de Publicación de Elegidos',
        }

        widgets = {
            'auto_id': forms.HiddenInput(),
        }
