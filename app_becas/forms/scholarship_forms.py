from django import forms
from app_becas.models import TypeScholarship 


class ScholarshipForm(forms.Form):
    name = forms.CharField(label='Nombre de la beca')
    description = forms.CharField(label='Descripción')
    amount = forms.DecimalField(label='Monto')
    type_scholarship_objects = TypeScholarship.objects.all()
    type_scholarship_choices = [(obj.name,obj.name) for obj in type_scholarship_objects]
    type_scholarship = forms.ChoiceField(
        label='Tipo de Beca',
        choices=[('', 'Selecciona un tipo de beca')] + type_scholarship_choices,
        initial = '',
    )
    

class type_scholarship_form(forms.Form):

    new_type_scholarship = forms.CharField(
        label='Nuevo Tipo de Beca',
    )

class delete_type(forms.Form):

    delete_type_scholarship = forms.CharField(
        label= 'Nombre de tipo de beca:', 
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