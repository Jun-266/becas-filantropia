import uuid
from django.db import models

class My_user(models.Model):
    userId = models.CharField(max_length=255)
    autoId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    

    def __str__(self):
        return f'{self.name} {self.lastname}'
    

class   Scholarship(models.Model):
    auto_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    amount = models.IntegerField()
    type_scholarship = models.CharField(max_length=50, choices=[('Excelencia', 'Excelencia'), ('Logros y Representantes', 'Logros y Representantes'), ('Colaboradores', 'Colaboradores'), ('Especial', 'Especial'), ('Familiar y Minorías', 'Familiar y Minorías')])

    def __str__(self):
        return self.name
    
    
class Calendar(models.Model):
        
    auto_id =  models.AutoField(primary_key = True)
    calendar_type_id = models.CharField(max_length=2)
    scholarship_id = models.CharField(max_length=20)
    inscription_start_date = models.DateField()
    inscription_deadline = models.DateField()
    selection_start_date = models.DateField()
    selection_deadline = models.DateField()
    interview_start_date = models.DateField()
    interview_deadline = models.DateField()
    publish_elected_start_date = models.DateField()
    publish_elected_deadline = models.DateField( )

    def __str__(self):
        return str(self.auto_id) 
