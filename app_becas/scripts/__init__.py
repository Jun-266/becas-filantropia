from app_becas.models import TypeScholarship

#name = models.CharField(max_length=50,unique=True)
def init():   
    if not TypeScholarship.objects.all():
        print("# Table TypeScholarship initialized")
        TypeScholarship.objects.create(name="Matricula")
        TypeScholarship.objects.create(name="Alimentación")
        TypeScholarship.objects.create(name="Transporte")
    
    # In case you need to delete them
    '''
    print("deleting")
    TypeScholarship.objects.get(name="Matricula").delete()
    TypeScholarship.objects.get(name="Alimentación").delete()
    TypeScholarship.objects.get(name="Transporte").delete()
    '''