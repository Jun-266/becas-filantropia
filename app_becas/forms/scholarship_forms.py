from django import forms
from app_becas.models import Scholarship 

class ScholarshipForm(forms.Form):
    #form = Scholarship()
    type_scholarship = forms.ChoiceField(
    choices=[('Excelencia', 'Excelencia'), ('Logros y Representantes', 'Logros y Representantes'),
                ('Colaboradores', 'Colaboradores'), ('Especial', 'Especial'),
                ('Familiar y Minorías', 'Familiar y Minorías')],
    label="Tipo de Beca"

    )

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