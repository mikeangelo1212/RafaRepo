from logger_base import log

class Contrato:
    def __init__(self,id,nocontrato,costo,fechadeinicio,fechafin) -> None:
        self.id=id
        self.nocontrato=nocontrato
        self.costo=costo
        self.fechadeinicio=fechadeinicio
        self.fechafin=fechafin
        pass
    
    def __str__(self) -> str:
        return f"id: {self.id}\nNo. Contrato: {self.nocontrato}\nCosto: {self.costo}\nFecha de Inicio: {self.fechadeinicio}\nFecha Fin: {self.fechafin}"