from django import forms
from app_becas.models import TypeScholarship 
from app_becas.models import Calendar

class ScholarshipForm(forms.Form):
    name = forms.CharField(label='Nombre de la beca')
    description = forms.CharField(label='Descripción')
    amount = forms.DecimalField(label='Monto')

    default_choices = [('', 'Selecciona un cronograma')]
    calendar_id = forms.ChoiceField(
        label='Cronograma (ID)',
        choices= default_choices,
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
        self.fields['type_scholarship'].choices = self.get_dynamic_choice_ts()
        self.fields['calendar_id'].choices = self.get_dynamic_choice_ci()

    def get_dynamic_choice_ts(request):
        choices = [(obj.id, obj.name) for obj in TypeScholarship.objects.all()]
        return choices
    
    def get_dynamic_choice_ci(request):
        choices = [(obj.auto_id, obj.scholarship_id) for obj in Calendar.objects.all()]
        return [('', 'Selecciona un cronograma existente')] + choices

class type_scholarship_form(forms.Form):

    new_type_scholarship = forms.CharField(
        label='Nuevo Tipo de Beca',
    )
