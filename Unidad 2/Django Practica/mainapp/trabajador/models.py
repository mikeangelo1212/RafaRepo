from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"Domicilio {self.id} {self.calle}"
    
class Departamento(models.Model):
    nombreDep = models.CharField(max_length = 255)
    seccion = models.CharField(max_length = 3)
    
    def __str__(self) -> str:
        return f"Departamento {self.id} {self.nombreDep},{self.seccion}"
    
class Jefe(models.Model):
    nombreJefe = models.CharField(max_length = 255)
    departamento = models.ForeignKey(Departamento, on_delete = models.SET_NULL, null = True)
    
    def __str__(self) -> str:
        return f"Jefe {self.id} {self.nombreJefe},{self.departamento}"
        
class Trabajador(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    domiciio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
    departamento = models.ForeignKey(Departamento, on_delete = models.SET_NULL, null = True)
    
    def __str__(self) -> str:
        return f"Persona: {self.id} {self.nombre} {self.apellido}, {self.email}, {self.domiciio}, {self.departamento}"