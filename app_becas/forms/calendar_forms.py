from django import forms
from app_becas.models import Calendar

class Calendar_form_model(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ["auto_id",
                  "convocation_type_id",
                  "scholarship_id",
                  "inscription_start_date", 
                  "inscription_deadline",
                  "selection_start_date",
                  "selection_deadline",
                  "interview_start_date",
                  "interview_deadline",
                  "publish_elected_start_date",
                  "publish_elected_deadline",
                  ]