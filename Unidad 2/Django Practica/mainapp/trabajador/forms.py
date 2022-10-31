from django.forms import ModelForm,EmailInput
from trabajador.models import *

class TrabajadorForm(ModelForm):
    class Meta:
        model= Trabajador
        fields='__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }
        
class JefeForm(ModelForm):
    class Meta:
        model= Jefe
        fields='__all__'
        
class DomForm(ModelForm):
    class Meta:
        model= Domicilio
        fields='__all__'
        
class DepaForm(ModelForm):
    class Meta:
        model= Departamento
        fields='__all__'