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
    

class Scholarship(models.Model):
    auto_id = models.UUIDField(default=uuid.uuid4, editable=False)
    calendar_id = models.UUIDField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    amount = models.IntegerField()
    type_scholarship = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
class Calendar(models.Model):
    #auto_id = models.AutoField(primary_key=True)
    auto_id = models.UUIDField(default=uuid.uuid4, primary_key= True)
    convocation_type_id = models.CharField(max_length=2)
    scholarship_id = models.CharField(max_length=20)
    inscription_start_date = models.DateField()
    inscription_deadline = models.DateField()
    selection_start_date = models.DateField()
    selection_deadline = models.DateField()
    interview_start_date = models.DateField()
    interview_deadline = models.DateField()
    publish_elected_start_date = models.DateField()
    publish_elected_deadline = models.DateField( )

    def _str_(self):
        return str("sch id:"+self.scholarship_id)
    
class TypeScholarship(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name 

class Contact(models.Model):
    auto_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key= True)
    identification = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.auto_id)


class Donor(models.Model):
    scholarships = models.ManyToManyField(Scholarship, related_name='donors')
    contacts = models.ManyToManyField(Contact, related_name='donors')
    auto_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key= True)   
    enterprise_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.auto_id)


class File(models.Model):
    my_file = models.FileField(upload_to='archivos/')

