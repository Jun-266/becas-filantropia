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
