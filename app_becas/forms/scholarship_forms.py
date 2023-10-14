from django import forms
from app_becas.models import TypeScholarship 
from django.db.utils import OperationalError

class ScholarshipForm(forms.Form):
    name = forms.CharField(label='Nombre de la beca')
    description = forms.CharField(label='Descripción')
    amount = forms.DecimalField(label='Monto')
    type_scholarship_objects = TypeScholarship.objects.all()
    try:
        type_scholarship_choices = [(obj.name,obj.name) for obj in type_scholarship_objects]
    except OperationalError:
        print("## Es necesario que apliques las migraciones")
        print("## Para que se cree automáticamente las tablas necesarias")

    default_choices = [('', 'Selecciona un tipo de beca')]
    type_scholarship = forms.ChoiceField(
        label='Tipo de Beca',
        choices= default_choices,
        initial = '',
    )

    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.fields['type_scholarship'].choices = self.get_dynamic_choice()
        

    def get_dynamic_choice(request):
        choices = [(obj.name, obj.name) for obj in TypeScholarship.objects.all()]
        return choices

class type_scholarship_form(forms.Form):

    new_type_scholarship = forms.CharField(
        label='Nuevo Tipo de Beca',
    )

class delete_type(forms.Form):

    delete_type_scholarship = forms.CharField(
        label= 'Nombre de tipo de beca:', 
    )
