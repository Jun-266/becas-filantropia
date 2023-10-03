import uuid
from django.db import models

class Scholarship(models.Model):
    Type_Scholaship = [
        ('Excelencia', 'Beca de Excelencia'),
        ('Logros', 'Beca de Logros'),
        ('Representantes', 'Beca de Representantes'),
        ('Colaboradores', 'Beca de Colaboradores'),
        ('Especial', 'Beca Especial'),
        ('Familiar', 'Beca Familiar'),
        ('Minorias', 'Beca de Minorías'),
    ]
    auto_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    amount = models.IntegerField()
    type = models.CharField(max_length=20, choices=Type_Scholaship)

    def __str__(self):
        return self.name