from django.db import models

# Create your models here.
class Calendar(models.Model):
    inscription_start_date = models.CharField(max_length=200)
    inscription_deadline = models.CharField(max_length=255)
    def __str__(self):
        return self.name