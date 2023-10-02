from django.db import models

class Scholarship(models.Model):
    name = models.CharField
    description = models.CharField(max_length=250)
    amount = models.IntegerField()

