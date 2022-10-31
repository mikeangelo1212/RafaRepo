from ast import For, Return
from persona import Persona
from conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class PersonaDAO():
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id"
    _INSERTAR = "INSERT INTO persona(nombre,edad,correo) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, edad=%s, correo=%s WHERE id = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id=%s"
    _CONTAR = "SELECT SUM(costo) FROM contrato,idpersona WHERE idpersona.correo= %s"

    _CONTAR = "SELECT SUM(costo) as total FROM persona INNER Join contrato_persona ON contrato_persona.idpersona=persona.id inner join contrato ON contrato_persona.idcontrato = contrato.id WHERE correo= %s"


    @classmethod
    def Insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.edad,persona.correo)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas =[]
                for r in registros:
                    persona = Persona(r[0],r[1],r[2],r[3])
                    personas.append(persona)
                return personas
    
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
                valores = (persona.nombre,persona.edad,persona.correo,persona.id)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
    
    @classmethod
    def contar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.correo)
            cursor.execute(cls._CONTAR)
            registros = cursor.fetchall()
            personas =[]
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas

if __name__ == '__main__':
    #Insertar
    persona1 = Persona(id="",nombre="Jordan",edad=20,correo="j@gmail.com")
    personaInsertadas = PersonaDAO.Insertar(persona1)
    log.debug(f"personas insertadas {personaInsertadas}")
    # #Actualizar
    # persona1=Persona(id="2",nombre="tonto",edad="50",correo="tonto@gmail.com")
    # personaActualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f"personas actualizadas {personaActualizadas}")
    # # #Eliminar
    # persona1 = Persona(id="1",nombre="",edad="",correo="")
    # personaEliminadas =PersonaDAO.eliminar(persona1)
    # log.debug(f"personas elimianadas {personaEliminadas}")
    #ver
    personas = PersonaDAO.seleccionar()
    for p in personas:
        log.debug(p)