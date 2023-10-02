from django.db import models

# Create your models here.
class Calendar(models.Model):
    auto_id =  models.AutoField(primary_key = True)
    calendar_type_id = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
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
        return str(self.name)