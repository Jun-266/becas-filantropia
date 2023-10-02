from django.db import models

class App_becas_usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.lastname}'
