from django.forms import ModelForm,EmailInput
from gestorapp.models import *

class AlumnoForm(ModelForm):
    class Meta:
        model= Alumnos
        fields='__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }
        
class MaestroForm(ModelForm):
    class Meta:
        model= Maestro
        fields='__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }

class DirectivoForm(ModelForm):
    class Meta:
        model= Directivos
        fields='__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }