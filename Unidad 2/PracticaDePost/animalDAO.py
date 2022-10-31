from ast import For, Return
from animal import Animal
from conexion import Conexion
from AnimalcursorDelPool import CursorDelPool
from logger_base import log 

class AnimalDAO():
    _SELECCIONAR = "SELECT * FROM animal ORDER BY idanimal"
    _INSERTAR = "INSERT INTO animal(nombre,especie,sexo) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE animal SET nombre=%s, especie=%s, sexo=%s WHERE idanimal = %s"
    _ELIMINAR = "DELETE FROM animal WHERE idanimal=%s"

    @classmethod
    def Insertar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.nombre,animal.especie,animal.sexo)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                animales =[]
                for r in registros:
                    animal = Animal(r[0],r[1],r[2],r[3])
                    animales.append(animal)
                return animales
    
    @classmethod
    def actualizar(cls,animal):
        with CursorDelPool() as cursor:
                valores = (animal.nombre,animal.especie,animal.sexo,animal.idanimal)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.idanimal,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar
    # animal1 = Animal(idanimal="",nombre="Jordan",especie="Pinguino",sexo="hembra")
    # animalInsertadas = AnimalDAO.Insertar(animal1)
    # log.debug(f"animales insertadas {animalInsertadas}")
    # #Actualizar
    animal1=Animal(idanimal=7,nombre="tonto",especie="tiburon",sexo="niña")
    animalActualizadas = AnimalDAO.actualizar(animal1)
    log.debug(f"animales actualizadas {animalActualizadas}")
    # #Eliminar
    # animal1 = Animal(idanimal="8",nombre="Pancrasio",especie="Mendez",sexo="hembra")
    # animalEliminadas =AnimalDAO.eliminar(animal1)
    # log.debug(f"animales elimianadas {animalEliminadas}")
    #ver
    animales = AnimalDAO.seleccionar()
    for p in animales:
        log.debug(p)
