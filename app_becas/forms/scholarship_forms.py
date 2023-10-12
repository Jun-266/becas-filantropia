from django import forms
from app_becas.models import TypeScholarship 


class ScholarshipForm(forms.Form):
    name = forms.CharField(label='Nombre de la beca')
    description = forms.CharField(label='Descripción')
    amount = forms.DecimalField(label='Monto')

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
