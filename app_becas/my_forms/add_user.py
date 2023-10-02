from django.db import models
from django.forms import ModelForm
from app_becas.models import App_becas_usuario

class Add_user(ModelForm):

    class Meta:
        model = App_becas_usuario
        fields = '__all__'

    def is_valid(self):
        super().is_valid()

        return True
