from logger_base import log

class Contrato_Persona:
    def __init__(self,idpersona,idcontrato) -> None:
        self.idpersona=idpersona
        self.idcontrato=idcontrato
        pass
    
    def __str__(self) -> str:
        return f"idPersona: {self.idpersona}\nidContrato: {self.idcontrato}"