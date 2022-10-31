from ast import For, Return
from empleado import Empleado
from conexion import Conexion
from EmpleadocursorDelPool import CursorDelPool
from logger_base import log 

class EmpleadoDAO():
    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY idempleado'
    _INSERTAR = 'INSERT INTO empleado(nombreempleado,apellidoempleado,emailempleado) Values(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombreempleado=%s, apellidoempleado=%s, emailempleado=%s WHERE idempleado = %s'
    _ELIMINAR = 'DELETE FROM empleado WHERE idempleado=%s'

    @classmethod
    def Insertar(cls,empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombreempleado,empleado.apellidoempleado,empleado.emailempleado)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                empleados =[]
                for r in registros:
                    empleado = Empleado(r[0],r[1],r[2],r[3])
                    empleados.append(empleado)
                return empleados
    
    @classmethod
    def actualizar(cls,empleado):
        with CursorDelPool() as cursor:
                valores = (empleado.nombreempleado,empleado.apellidoempleado,empleado.emailempleado,empleado.idempleado)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.idempleado,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar
    # empleado1 = Empleado(idempleado="",nombreempleado="Martin",apellidoempleado="Sanabia",emailempleado="sanabia@gmail.com")
    # empleadoInsertadas = EmpleadoDAO.Insertar(empleado1)
    # log.debug(f"empleados insertadas {empleadoInsertadas}")
    # #Actualizar
    empleado1=Empleado(idempleado=8,nombreempleado="Luis",apellidoempleado="Soto",emailempleado="tontolandia@gmail.com")
    empleadoActualizadas = EmpleadoDAO.actualizar(empleado1)
    log.debug(f"empleados actualizadas {empleadoActualizadas}")
    # # #Eliminar
    # empleado1 = Empleado(idempleado=6,nombreempleado="Pancrasio",apellidoempleado="Mendez",emailempleado="Pancrasio@gmail.com")
    # empleadoEliminadas =EmpleadoDAO.eliminar(empleado1)
    # log.debug(f"empleados elimianadas {empleadoEliminadas}")
    #ver
    empleados = EmpleadoDAO.seleccionar()
    for p in empleados:
        log.debug(p)
