from logger_base import log

class Animal:
    def __init__(self,idanimal,nombre,especie,sexo) -> None:
        self.idanimal=idanimal
        self.nombre=nombre
        self.especie=especie
        self.sexo=sexo
        pass
    
    def __str__(self) -> str:
        return f"idanimal: {self.idanimal}\nNombre: {self.nombre}\nEspecie: {self.especie}\nSexo: {self.sexo}"