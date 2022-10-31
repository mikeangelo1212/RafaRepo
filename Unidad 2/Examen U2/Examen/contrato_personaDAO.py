from ast import For, Return
from contrato_persona import Contrato_Persona
from conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 
from persona import Persona

class contrato_personaDAO():
    _SELECCIONAR = "SELECT * FROM contrato_persona ORDER BY idpersona"
    _INSERTAR = "INSERT INTO contrato_persona(idpersona,idcontrato) Values(%s,%s)"
    _ACTUALIZAR = "UPDATE contrato_persona SET idpersona=%s, idcontrato=%s WHERE idpersona = %s"
    _ELIMINAR = "DELETE FROM contrato_persona WHERE idpersona=%s"
    _CONTAR = "SELECT SUM(costo) as total FROM contrato_persona INNER Join persona ON contrato_persona.idpersona=persona.id inner join contrato ON contrato_persona.idcontrato = contrato.id WHERE persona.correo= %s"

    @classmethod
    def Insertar(cls,contrato_persona):
        with CursorDelPool() as cursor:
            valores = (contrato_persona.idpersona,contrato_persona.idcontrato)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contrato_personas =[]
                for r in registros:
                    contrato_persona = Contrato_Persona(r[0],r[1])
                    contrato_personas.append(contrato_persona)
                return contrato_personas

    # @classmethod
    # def contar(cls,persona):
    #     with CursorDelPool() as cursor:
    #         valores = (persona.correo)
    #         cursor.execute(cls._CONTAR)
    #         registros = cursor.fetchall()
    #         contrato_personas =[]
    #         for r in registros:
    #             contrato_persona = Contrato_Persona(r[0],r[1])
    #             contrato_personas.append(contrato_persona)
    #         return contrato_personas
    
    

if __name__ == '__main__':
    #Insertar
    contrato_persona1 = Contrato_Persona(idpersona=3,idcontrato=3)
    contrato_personaInsertadas = contrato_personaDAO.Insertar(contrato_persona1)
    log.debug(f"contrato_personas insertadas {contrato_personaInsertadas}")
    #ver
    contrato_personas = contrato_personaDAO.seleccionar()
    for p in contrato_personas:
        log.debug(p)