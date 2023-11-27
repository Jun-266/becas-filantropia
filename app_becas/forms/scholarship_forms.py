from django import forms
from app_becas.models import TypeScholarship 
from app_becas.models import ConditionEnum, ConditionParams
from app_becas.models import Scholarship, Donor, Calendar
from django.db.utils import OperationalError, ProgrammingError
from django.forms import ModelForm

class ScholarshipFormModel(ModelForm):
    class Meta:
        model = Scholarship
        fields = ('__all__')
        '''
            'name': 'Nombre',
            'summary': 'Resumen',
            'target_audiences': '¿A quién está dirigida?',
            'benefits': 'Beneficios',
            'post_img': 'Imagen',
            'recomendations': 'Recomendaciones',
        '''
        labels = {
            'additional_info': 'Información Adicional',
            'auto_id': forms.HiddenInput(),
        }


class ScholarshipForm(forms.Form):
    #is_active = forms.BooleanField( label="¿Está activa?")

    name = forms.CharField(
        label='Nombre de la beca',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
    )
    post_img = forms.ImageField(
        label='Subir imagen',
        required=False,  
    )
    summary = forms.CharField(
        label='Resumen',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Breve resumen de la beca'}),
    )
    target_audiences = forms.CharField(
        label='A quién está dirigida',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Descripción del público objetivo'}),
    )
    recomendations = forms.CharField(
        label='Recomendaciones',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Consejos o requisitos'}),
    )
    condition_params = forms.CharField(
        label='Condiciones',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Condiciones'}),
    )

    renovation_info = forms.CharField(
        label='Renovación de la Beca',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Sobre la renovación de la Beca'}),
        required=False
    )
    additional_info = forms.CharField(
        label='Información Adicional',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Información adicional opcional'}),
        required=False
    )


    type_scholarship_objects = TypeScholarship.objects.all()
    donor_objects = Donor.objects.all()
    conditions_objects = ConditionEnum.objects.all()
    try:
        type_scholarship_choices = [(obj.name, obj.name) for obj in type_scholarship_objects]
        donor_choices = [(obj.name, obj.name) for obj in type_scholarship_objects]
        conditions_choices = [(obj.name, obj.name) for obj in conditions_objects]
    except OperationalError:
        print("## Es necesario que apliques las migraciones")
        print("## Para que se cree automáticamente las tablas necesarias")
    except ProgrammingError:
        print(ProgrammingError)

    default_choices = [('', 'Selecciona un tipo de beca')] #type_sch
    benfits_choice = forms.MultipleChoiceField( 
        label='Beneficios que incluye',
        choices=default_choices,
        initial='',
        widget=forms.CheckboxSelectMultiple,
    )

    #'class': 'form-control',
    donor_choice = forms.ChoiceField(label= 'Donante', choices=[('', 'Selecciona un donante')], widget=forms.Select(attrs={ 'style': 'width:30%; font-size: medium;'}))
    
    calendar_choice = forms.ChoiceField(label= 'Cronograma', choices=[('', 'Cronogramas')], widget=forms.Select(attrs={ 'style': 'width:30%; font-size: medium; '}))

    benefits = forms.CharField(
        label='Beneficios detallados',
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'style': 'width:70%;', 'placeholder': 'Beneficios sobre cada apartado en el que se brindará apoyo'}),
    )
    


    #Pedir otras condiciones

    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.fields['benfits_choice'].choices = self.get_dynamic_type_sch() #type_sch
        self.fields['donor_choice'].choices = self.get_dynamic_type_donor() 
        self.fields['calendar_choice'].choices = self.get_dynamic_type_calendar() 
        
    def get_dynamic_type_sch(request):
        choices = [(obj.name, obj.name) for obj in TypeScholarship.objects.all()]
        return choices
    def get_dynamic_type_donor(request):
        choices = [(obj.auto_id, obj.enterprise_name) for obj in Donor.objects.all()]
        return choices
    def get_dynamic_type_calendar(request):
        choices = [(obj.auto_id, obj.scholarship_name) for obj in Calendar.objects.all()]
        return choices

# Declare Forms
class conditionsForm1(forms.Form):
    #scholarship = forms.UUIDField()
    scholarship = forms.CharField(
        label='Beca ID',
    )

    conditions_just_select = forms.MultipleChoiceField(
        label='Condiciones Simples',
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )
    
    def __init__(self, *args, **kwargs):
        super(conditionsForm1, self).__init__(*args, **kwargs)
        self.fields['conditions_just_select'].choices = self.get_dynamic_condition_js()

    def get_dynamic_condition_js(request):
        choices = [(obj.name, obj.name) for obj in ConditionEnum.objects.all().filter(condition_type="SI/NO")]
        return choices
    

class conditionsForm2(forms.Form):
    # Socioeconómicos - Financieros 
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

# Third step is attached to the model directly, we will do some tweaks inside the save method of this form
class conditionsForm3(forms.ModelForm):
    class Meta:
        model = ConditionParams
        fields = ('value',)


class conditionsForm(forms.Form):
    #Conditions
    # Los datos que se djen en blanco no serán tomados en cuenta
    conditions_just_select = forms.MultipleChoiceField(
        label='Condiciones Simples',
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    # Socioeconómicos - Financieros 
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

    # Académico
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

    
    # Localidad
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

    # Otros
    edad_maxima = forms.IntegerField(
        label='Edad máxima',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    aprobar_entrevistas_o_pruebas = forms.CharField(
        label='Aprobar entrevistas o pruebas',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    ensayo_escrito = forms.CharField(
        label='Ensayo escrito',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    certificados = forms.CharField(
        label='Certificados',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )
    no_aplica_para_los_programas = forms.CharField(
        label='No aplica para los programas',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'style': 'width:70%;'}),
        required=False
    )

   
    
# To add a condition enum 
class condition_enum_form(forms.Form):
    name = forms.CharField(label='Nombre de la beca')

    default_choices_ct = [('','Elige un tipo'),('SI/NO', 'SI/NO'), ('SI/NO e Ingresar dato', 'Marcar SI/NO e Ingresar dato')]
    condition_type = forms.ChoiceField(
        label='Tipo de condición',
        choices=default_choices_ct,
        initial='',
    )
    
    # Does it need to type?, if yes, what is the data type
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
