from django import forms
from app_becas.models import Calendar

class Form_add_donor(forms.Form):
    enterprise_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'margin-bottom: 10px; border-radius: 10px;',
            'placeholder': 'Nombre de la empresa',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'style': 'margin-bottom: 10px; border-radius: 10px;',
            'placeholder': 'Correo electrónico',
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'margin-bottom: 10px; border-radius: 10px;',
            'placeholder': 'Teléfono',
        })
    )
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'margin-bottom: 10px; border-radius: 10px;',
            'placeholder': 'Ciudad',
        })
    )
    pais = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'margin-bottom: 10px; border-radius: 10px;',
            'placeholder': 'País',
        })
    )
    
    joined_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'style': 'margin-bottom: 10px; border-radius: 10px;',
            'placeholder': 'Fecha de unión',
            'type': 'date',
        })
    )

    def __init__(self, *args, **kwargs):
        super(Form_add_donor, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = ''