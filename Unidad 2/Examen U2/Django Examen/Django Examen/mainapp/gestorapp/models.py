from django.db import models

# Create your models here.

class Escuela(models.Model):
    nombreEscuela = models.CharField(max_length=255)
    CapacidadAlumnos = models.IntegerField()
    calleEsc = models.CharField(max_length=255)
    no_calleEsc = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Escuela {self.id} {self.nombreEscuela} {self.CapacidadAlumnos} {self.calleEsc} {self.no_calleEsc}"

class Domicilio(models.Model):
    calleDom = models.CharField(max_length = 255)
    no_calleDom = models.CharField(max_length = 255)
    colonia = models.CharField(max_length = 255)
    
    def __str__(self) -> str:
        return f"Domicilio: {self.id} {self.calleDom} {self.no_calleDom}, {self.colonia}"
    
class Alumnos(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
    escuela = models.ForeignKey(Escuela, on_delete = models.SET_NULL, null = True)
        
    def __str__(self) -> str:
        return f"Alumnos {self.id} {self.nombre},{self.apellido} {self.email} {self.domicilio} {self.escuela}"
    
class Maestro(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    materia = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
    escuela = models.ForeignKey(Escuela, on_delete = models.SET_NULL, null = True)
    
    def __str__(self) -> str:
        return f"Maestro {self.id} {self.nombre} {self.apellido} {self.materia} {self.email} {self.domicilio} {self.escuela}"
    
class Directivos(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    puesto = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
    escuela = models.ForeignKey(Escuela, on_delete = models.SET_NULL, null = True)
    
    def __str__(self) -> str:
        return f"Jefe {self.id} {self.nombre} {self.apellido} {self.puesto} {self.email} {self.domicilio} {self.escuela}"
