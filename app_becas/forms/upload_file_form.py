from django.forms import ModelForm
from app_becas.models import File


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = ['my_file']
