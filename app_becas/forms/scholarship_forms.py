from django import forms
from app_becas.models import TypeScholarship 
from app_becas.models import Scholarship
from app_becas.models import Calendar
from django.db.utils import OperationalError

class ScholarshipForm(forms.Form):
    name = forms.CharField(label='Nombre de la beca')
    description = forms.CharField(label='Descripción')
    amount = forms.DecimalField(label='Monto')

    default_choices = [('', 'Selecciona un cronograma existente')] 
    calendar_id = forms.ChoiceField(
        label='Cronograma (ID)',
        initial = '',
    )

    default_choices = [('', '_')]
    type_scholarship = forms.ChoiceField(
        label='Tipo de Beca',
        choices= default_choices,
        initial = '',
    )

    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        try:
            self.fields['type_scholarship'].choices = self.get_dynamic_choice_ts()
            self.fields['calendar_id'].choices = self.get_dynamic_choice_ci()
        except OperationalError:
            print("## Es necesario que apliques las migraciones")
            print("## Para que se cree automáticamente las tablas necesarias")

        
    def get_dynamic_choice_ts(request):
        choices = [(obj.name, obj.name) for obj in TypeScholarship.objects.all()]
        return choices
    
    def get_dynamic_choice_ci(request):
        choices = [(obj.auto_id, "-"+Scholarship.objects.get(obj.scholarship_id).name) for obj in Calendar.objects.all()]
        return  choices
    
   


class type_scholarship_form(forms.Form):

    new_type_scholarship = forms.CharField(
        label='Nuevo Tipo de Beca',
    )

class delete_type(forms.Form):

    delete_type_scholarship = forms.CharField(
        label= 'Nombre de tipo de beca:', 
    )
