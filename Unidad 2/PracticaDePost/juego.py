from logger_base import log

class Juego:
    def __init__(self,idjuego,nombre,consola,costo) -> None:
        self.idjuego=idjuego
        self.nombre=nombre
        self.consola=consola
        self.costo=costo

    def __str__(self) -> str:
        return f"idjuego: {self.idjuego}\nNombre: {self.nombre}\nConsola: {self.consola}\nCosto: {self.costo}"