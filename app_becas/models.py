import uuid
from django.db import models


class MyUser(models.Model):
    user_id = models.CharField(max_length=50)
    auto_id = models.CharField(max_length=30, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    rol = models.CharField(max_length=30, choices=[
        ('Director filantropía', 'Director filantropía'),
        ('Filantropía', 'Filantropía'),
        ('Apoyo financiero', 'Apoyo financiero'),
    ])
    
    def __str__(self):
        return f'{self.name} {self.lastname}'


class TypeScholarship(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name 


class ScholarshipParams(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    type_name = models.CharField(max_length=30, default=uuid.uuid4)
    scholarship_id = models.CharField(max_length=30, default=uuid.uuid4)
    units = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    units_type = models.CharField(max_length=20, default=1)

    def __str__(self):
        return self.auto_id 


class Scholarship(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    calendar_id = models.CharField(max_length=50, default=uuid.uuid4, editable=True)
    donor_id = models.CharField(max_length=50, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=40)
    summary = models.CharField(max_length=250)
    target_audiences = models.CharField(max_length=400,
                                        default="La Beca está dirigida a _, de estratos _, del departamento/municipio de _, con alto desempeño, potencial académico y limitaciones económicas manifiestas, interesados en cursar los programas de pregrado de _. Esta beca no aplica para _ ")
    benefits = models.CharField(max_length=450)

    #conditions = Another table
    recomendations = models.CharField(max_length=2200)
    additional_info = models.CharField(max_length=2500)
    #post_img = models.ImageField(upload_to='images/')
    #is_active = models.BooleanField()
    
    def __str__(self):
        return self.name

class ConditionEnum(models.Model):
    name = models.CharField(max_length=35, editable=False, primary_key=True)
    condition_type = models.CharField(max_length=40)
    ## SI/NO. SI/NO e Ingresar dato
    data_type = models.CharField(max_length=10)
    # Numero, Texto, Fecha 
     
    def __str__(self):
        return self.name
    
class ConditionParams(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    scholarship_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False)
    condition_name = models.CharField(max_length=50, editable=False)
    value = models.CharField(max_length=30, editable=False)

    def __str__(self):
        return self.name
    
class Calendar(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, primary_key=True)
    convocation_type_id = models.CharField(max_length=2)
    scholarship_id = models.CharField(max_length=20)
    inscription_start_date = models.DateField()
    inscription_deadline = models.DateField()
    selection_start_date = models.DateField()
    selection_deadline = models.DateField()
    interview_start_date = models.DateField()
    interview_deadline = models.DateField()
    publish_elected_start_date = models.DateField()
    publish_elected_deadline = models.DateField()

    def _str_(self):
        return str("sch id:"+self.scholarship_id)


class Donor(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    scholarships = models.ManyToManyField(Scholarship, related_name='donors')
    enterprise_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=30, null=True, blank=True)
    pais = models.CharField(max_length=30, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.auto_id)
    
class Contact(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, blank=True, related_name='contacts')
    identification = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=[
        ('Dueño', 'Dueño'),
        ('Empleado', 'Empleado'),
    ])
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.auto_id)


class File(models.Model):
    my_file = models.FileField(upload_to='archivos/')


class Candidate(models.Model):
    full_name = models.CharField(max_length=250)
    student_code = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    grade_point_average = models.DecimalField(max_digits=5, decimal_places=2)
    application_date = models.DateField()
    requested_scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)


class Major(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.auto_id)


class Student(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    first_semester = models.CharField(max_length=8)
    last_semester = models.CharField(max_length=8)

    def __str__(self):
        return str(self.auto_id)


class ApplicationStatus(models.Model):
    type = models.CharField(max_length=20, primary_key=True, choices=[
        ('Aprobada', 'Aprobada'),
        ('En proceso', 'En proceso'),
        ('Denegada', 'Denegada'),
        ('Concluida', 'Concluida'),
    ])

    def __str__(self):
        return self.type


class ScholarshipApplication(models.Model):
    auto_id = models.CharField(max_length=50, default=uuid.uuid4, editable=False, primary_key=True)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    application_status = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Scholarship Application"
        verbose_name_plural = "Scholarship Applications"
