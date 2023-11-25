from django import forms
from app_becas.models import TypeScholarship 
from app_becas.models import ConditionEnum 
from app_becas.models import Scholarship 
from django.db.utils import OperationalError, ProgrammingError
from django.forms import ModelForm

class ScholarshipFormModel(ModelForm):
    class Meta:
        model = Scholarship
        fields = "__all__"
        labels = {
            'name': 'Nombre',
            'summary': 'Resumen',
            'target_audiences': '¿A quién está dirigida?',
            'benefits': 'Beneficios',
            'recomendations': 'Recomendaciones',
            'additional_info': 'Información Adicional',
        }

        widgets = {
            'summary': forms.Textarea(attrs={'class': 'form-control mb-2 ', 'style': 'width:70%;',  'rows': 4}),
            'target_audiences': forms.Textarea(attrs={'class': 'form-control mb-2 ', 'style': 'width:70%;',  'rows': 4}),
            'benefits': forms.Textarea(attrs={'class': 'form-control mb-2 ', 'style': 'width:70%;'}),
            'recomendations': forms.Textarea(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
            
            # Add other widgets for different fields if needed
        }
  


# In pause
class ScholarshipForm(forms.Form):
    #widget=forms.Textarea
    #name = forms.CharField(label='Nombre de la beca')
    #summary = forms.CharField(label='Resumen', widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Breve resumen de la beca"}))
    #target_audiences = forms.CharField(label='A quién está dirigida', widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Descripción del público objetivo"}))
    #benefits = forms.CharField(label='Beneficios', widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Lista de beneficios"}))
    #recommendations = forms.CharField(label='Recomendaciones', widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Consejos o requisitos"}))
    #additional_info = forms.CharField(label='Información Adicional', widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Información adicional opcional"}), required=False)

    name = forms.CharField(
        label='Nombre de la beca',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
    )
    summary = forms.CharField(
        label='Resumen',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Breve resumen de la beca'}),
    )
    target_audiences = forms.CharField(
        label='A quién está dirigida',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Descripción del público objetivo'}),
    )
    benefits = forms.CharField(
        label='Beneficios',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Lista de beneficios'}),
    )
    recomendations = forms.CharField(
        label='Recomendaciones',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Consejos o requisitos'}),
    )
    additional_info = forms.CharField(
        label='Información Adicional',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Información adicional opcional'}),
        required=False
    )


    type_scholarship_objects = TypeScholarship.objects.all()
    conditions_objects = ConditionEnum.objects.all()
    try:
        type_scholarship_choices = [(obj.name, obj.name) for obj in type_scholarship_objects]
        conditions_choices = [(obj.name, obj.name) for obj in conditions_objects]
    except OperationalError:
        print("## Es necesario que apliques las migraciones")
        print("## Para que se cree automáticamente las tablas necesarias")
    except ProgrammingError:
        print(ProgrammingError)

    default_choices = [('', 'Selecciona un tipo de beca')]
    type_scholarship = forms.MultipleChoiceField(
        label='Beneficios que incluye',
        choices=default_choices,
        initial='',
        widget=forms.CheckboxSelectMultiple,
    )
    
    #Conditions
    conditions_just_select = forms.MultipleChoiceField(
        label='Condiciones Simples',
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

##
    ciudad_de_residencia = forms.CharField(
        label='Ciudad de residencia',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    lugar_de_proveniencia = forms.CharField(
        label='Lugar de proveniencia',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    ensayo_escrito = forms.CharField(
        label='Ensayo escrito',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    aprobar_entrevistas_o_pruebas = forms.CharField(
        label='Aprobar entrevistas o pruebas',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    edad_minima = forms.IntegerField(
        label='Edad mínima',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    edad_maxima = forms.IntegerField(
        label='Edad máxima',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    no_aplica_para_los_programas = forms.CharField(
        label='No aplica para los programas',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    certificados = forms.CharField(
        label='Certificados',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    ingresos_del_padre_y_madre_menores_a = forms.IntegerField(
        label='Ingresos del padre y madre menores a',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    porcentaje_aprobado_por_el_icetex = forms.IntegerField(
        label='Porcentaje aprobado por el ICETEX',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    promedio_en_grados_superior_a = forms.IntegerField(
        label='Promedio en grados superior a',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    grados_del_bachiller_a_los_que_aplica = forms.CharField(
        label='Grados del bachiller a los que aplica',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    sisben = forms.CharField(
        label='SISBEN',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    estratos_socioeconomicos = forms.CharField(
        label='Estratos socioeconómicos',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    puntaje_icfes = forms.IntegerField(
        label='Puntaje ICFES',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    mes_anio_icfes = forms.DateField(
        label='Mes-año ICFES',
        widget=forms.DateInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    promedio_acumulado_en_la_carrera = forms.FloatField(
        label='Promedio acumulado en la carrera',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )


    


    

    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.fields['type_scholarship'].choices = self.get_dynamic_type_sch()
        self.fields['conditions_just_select'].choices = self.get_dynamic_condition_js()
        
    def get_dynamic_type_sch(request):
        choices = [(obj.name, obj.name) for obj in TypeScholarship.objects.all()]
        return choices

    def get_dynamic_condition_js(request):
        choices = [(obj.name, obj.name) for obj in ConditionEnum.objects.all().filter(condition_type="SI/NO")]
        return choices
    
    
# To add a condition enum 
class condition_enum_form(forms.Form):
    name = forms.CharField(label='Nombre de la beca')

    default_choices_ct = [('','Elige un tipo'),('SI/NO', 'SI/NO'), ('SI/NO e Ingresar dato', 'Marcar SI/NO e Ingresar dato')]
    condition_type = forms.ChoiceField(
        label='Tipo de condición',
        choices=default_choices_ct,
        initial='',
    )
    
    # Does it need to tpye?, if yes, what is the data type
    default_choices_dt = [('','Elige un tipo'), ('Number','Número'), ('Text','Texto'), ('Date','Fecha'), ('Does not apply', 'No aplica')]
    data_type = forms.ChoiceField(
        label='Dato esperado',
        choices=default_choices_dt,
        initial='',
    )

class type_scholarship_form(forms.Form):
    new_type_scholarship = forms.CharField(
        label='Nuevo Tipo de Beca',
    )


class delete_type(forms.Form):

    delete_type_scholarship = forms.CharField(
        label='Nombre de tipo de beca:',
    )


class SearchScholarshipForm(forms.Form):
    scholarship_name = forms.CharField(label='Nombre de la Beca', required=False)
    
class add_type_to_scholarship(forms.Form):
    types_obj = TypeScholarship.objects.all()
    try:
        types = [(obj.name,obj.name) for obj in types_obj]
    except OperationalError:
        print("## Es necesario que apliques las migraciones")
        print("## Para que se cree automáticamente las tablas necesarias")
    units = forms.DecimalField(label='Unidades disponibles')
    units_type = forms.ChoiceField(
        label='Tipo de Unidades',
        choices=(('Porcentaje', 'Porcentaje'), ('Dinero', 'Dinero'), ('Articulos', 'Articulos'))
    )
