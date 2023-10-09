from app_becas.models import TypeScholarship

#name = models.CharField(max_length=50,unique=True)
def init():   
    if not TypeScholarship.objects.all():
        print("# Table TypeScholarship initialized")
        TypeScholarship.objects.create(id=1, name="Matricula")
        TypeScholarship.objects.create(id=2 ,name="Alimentación")
        TypeScholarship.objects.create(id=3, name="Transporte")
    
    # In case you need to delete them
    '''
    print("deleting")
    TypeScholarship.objects.get(id = 1).delete()
    TypeScholarship.objects.get(id = 2).delete()
    TypeScholarship.objects.get(id = 3).delete()
    '''