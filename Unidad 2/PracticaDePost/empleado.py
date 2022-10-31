from logger_base import log

class Empleado:
    def __init__(self,idempleado,nombreempleado,apellidoempleado,emailempleado) -> None:
        self.idempleado=idempleado
        self.nombreempleado=nombreempleado
        self.apellidoempleado=apellidoempleado
        self.emailempleado=emailempleado
        pass

    def __str__(self) -> str:
        return f"idempleado: {self.idempleado}\nNombre: {self.nombreempleado}\nApellido: {self.apellidoempleado}\nEmail: {self.emailempleado}"
# clase persona con idpersona, nombre, apellido, email, edad
# usand omanejador de datos DAO (Data Access Object) persona DAO