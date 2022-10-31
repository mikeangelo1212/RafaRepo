from ast import For, Return
from juego import Juego
from conexion import Conexion
from JuegocursorDelPool import CursorDelPool
from logger_base import log 

class JuegoDAO():
    _SELECCIONAR = 'SELECT * FROM juego ORDER BY idjuego'
    _INSERTAR = 'INSERT INTO juego(nombre,consola,costo) Values(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE juego SET nombre=%s, consola=%s, costo=%s WHERE idjuego = %s'
    _ELIMINAR = 'DELETE FROM juego WHERE idjuego=%s'

    @classmethod
    def Insertar(cls,juego):
        with CursorDelPool() as cursor:
            valores = (juego.nombre,juego.consola,juego.costo)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                juegos =[]
                for r in registros:
                    juego = Juego(r[0],r[1],r[2],r[3])
                    juegos.append(juego)
                return juegos
    
    @classmethod
    def actualizar(cls,juego):
        with CursorDelPool() as cursor:
                valores = (juego.nombre,juego.consola,juego.costo,juego.idjuego)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,juego):
        with CursorDelPool() as cursor:
            valores = (juego.idjuego,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar
    # juego1 = Juego(idjuego="",nombre="RafaGame",consola="ouya",costo=10)
    # juegoInsertadas = JuegoDAO.Insertar(juego1)
    # log.debug(f"juegos insertadas {juegoInsertadas}")
    # # #Actualizar
    juego1=Juego(idjuego=5,nombre="RAFAAAAAAAA",consola="xbox",costo=70)
    juegoActualizadas = JuegoDAO.actualizar(juego1)
    log.debug(f"juegos actualizadas {juegoActualizadas}")
    # #Eliminar
    # juego1 = Juego(idjuego="4",nombre="Genshin",consola="switch",costo=50)
    # juegoEliminadas =JuegoDAO.eliminar(juego1)
    # log.debug(f"juegos elimianadas {juegoEliminadas}")
    #ver
    juegos = JuegoDAO.seleccionar()
    for p in juegos:
        log.debug(p)