from ast import For, Return
from contrato import Contrato
from conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log 

class ContratoDAO():
    _SELECCIONAR = "SELECT * FROM contrato ORDER BY id"
    _INSERTAR = "INSERT INTO contrato(nocontrato,costo,fechadeinicio,fechafin) Values(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE contrato SET nocontrato=%s, costo=%s, fechadeinicio=%s, fechafin=%s WHERE id = %s"
    _ELIMINAR = "DELETE FROM contrato WHERE id=%s"

    @classmethod
    def Insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.nocontrato,contrato.costo,contrato.fechadeinicio,contrato.fechafin)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratos =[]
                for r in registros:
                    contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                    contratos.append(contrato)
                return contratos
    
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
                valores = (contrato.nocontrato,contrato.costo,contrato.fechadeinicio,contrato.fechafin,contrato.id)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar
    # contrato1 = Contrato(id="",nocontrato=2,costo=100,fechadeinicio="10 DE MAYO 2022",fechafin="10 DE MAYO 2025")
    # contratoInsertadas = ContratoDAO.Insertar(contrato1)
    # log.debug(f"contratos insertadas {contratoInsertadas}")
    # # #Actualizar
    # contrato1=Contrato(id="3",nocontrato=10,costo=500,fechadeinicio="20 DE ENERO 2020",fechafin="20 DE MARZO 2020")
    # contratoActualizadas = ContratoDAO.actualizar(contrato1)
    # log.debug(f"contratos actualizadas {contratoActualizadas}")
    # # #Eliminar
    contrato1 = Contrato(id="5",nocontrato="",costo="",fechadeinicio="",fechafin="")
    contratoEliminadas =ContratoDAO.eliminar(contrato1)
    log.debug(f"contratos elimianadas {contratoEliminadas}")
    #ver
    contratos = ContratoDAO.seleccionar()
    for p in contratos:
        log.debug(p)