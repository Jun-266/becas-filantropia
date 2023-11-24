from app_becas.models import TypeScholarship
from app_becas.models import ConditionEnum

#name = models.CharField(max_length=50,unique=True)
def init():   
    # To start wiht TypeScholarship default choices / enum
    if not TypeScholarship.objects.exists():
        print("# Table TypeScholarship initialized")
        TypeScholarship.objects.create(name="Matricula")
        TypeScholarship.objects.create(name="Alimentación")
        TypeScholarship.objects.create(name="Transporte")
        TypeScholarship.objects.create(name="Libros")
        TypeScholarship.objects.create(name="Programa de acompañamiento")
    
    # In case you need to delete them
    '''
    print("deleting")
    TypeScholarship.objects.get(name="Matricula").delete()
    TypeScholarship.objects.get(name="Alimentación").delete()
    TypeScholarship.objects.get(name="Transporte").delete()
    TypeScholarship.objects.get(name="Libros").delete()
    TypeScholarship.objects.get(name="Programa de acompañamiento").delete()
    '''
    

    # To start wiht ConditionEnum default choices / enum
    if not ConditionEnum.objects.exists():
        print("# Table ConditionEnum initialized")
        ConditionEnum.objects.create(name="Lograr admisión a algun pregrado", condition_type= "SI/NO", data_type="Does not apply") 
        ConditionEnum.objects.create(name="Vivir fuera de Cali", condition_type= "SI/NO", data_type="Does not apply") 

        ConditionEnum.objects.create(name="Ciudad de residencia", condition_type= "SI/NO e Ingresar dato", data_type="Text") # e,g Cali, e.g Palmira
        ConditionEnum.objects.create(name="Lugar de proveniencia", condition_type= "SI/NO e Ingresar dato", data_type="Text") # e.g Cali, e.g Cundinamarca
        ConditionEnum.objects.create(name="Ensayo escrito", condition_type= "SI/NO e Ingresar dato", data_type="Number")  # extension/pages
        ConditionEnum.objects.create(name="Aprobar entrevistas o pruebas", condition_type= "SI/NO e Ingresar dato", data_type="Text")  # e.g psicológicas, e.g para Lumni Colmbia
        ConditionEnum.objects.create(name="Edad mínima", condition_type= "SI/NO e Ingresar dato", data_type="Number")
        ConditionEnum.objects.create(name="Edad máxima", condition_type= "SI/NO e Ingresar dato", data_type="Number")
        ConditionEnum.objects.create(name="No aplica para los programas", condition_type= "SI/NO e Ingresar dato", data_type="Text") # e.g Ingenierías
        ConditionEnum.objects.create(name="Cerfificados", condition_type= "SI/NO e Ingresar dato", data_type="Text")
        ConditionEnum.objects.create(name="Ingresos del padre y madre menores a", condition_type= "SI/NO e Ingresar dato", data_type="Number") # 2.5 SMMLV
        ConditionEnum.objects.create(name="Porcentaje aprobado por el ICETEX", condition_type= "SI/NO e Ingresar dato", data_type="Number") # 30 %
        ConditionEnum.objects.create(name="Promedio en grados superior a", condition_type= "SI/NO e Ingresar dato", data_type="Number") # 4
        ConditionEnum.objects.create(name="Grados del bachiller a los que aplica", condition_type= "SI/NO e Ingresar dato", data_type="Text") # 9°,10°,11°
        ConditionEnum.objects.create(name="SISBEN", condition_type= "SI/NO e Ingresar dato", data_type="Text") # e.g 70, e.g A
        ConditionEnum.objects.create(name="Estratos socioeconómicos", condition_type= "SI/NO e Ingresar dato", data_type="Text") # e.g (1,2,3)

        ConditionEnum.objects.create(name="Puntaje ICFES", condition_type= "SI/NO e Ingresar dato", data_type="Number") # e.g 250
        ConditionEnum.objects.create(name="Mes-año ICFES", condition_type= "SI/NO e Ingresar dato", data_type="Date") # e.g Agosto 2014
        ConditionEnum.objects.create(name="Promedio acumulado en la carrera", condition_type= "SI/NO e Ingresar dato", data_type="Number") # e.g 3.8

    