from logger_base import log

class Persona:
    def __init__(self,id,nombre,edad,correo) -> None:
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.correo=correo
        pass
    
    def __str__(self) -> str:
        return f"id: {self.id}\nNombre: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo}"