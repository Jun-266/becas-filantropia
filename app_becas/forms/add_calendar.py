from django import forms

class CreateNewTaskForm(forms.Form):
    title = forms.CharField(label= "Titulo de la tarea", max_length=200)
    description = forms.CharField(label= "Descripción de la view", widget=forms.Textarea)