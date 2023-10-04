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
