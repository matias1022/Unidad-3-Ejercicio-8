from ClaseEmpleado import Empleado
from datetime import datetime

class EmpleadoExterno(Empleado):
    __tarea=""
    __fechaInicio=""
    __fechaFinalizacion=""
    __montoV=0.0
    __costoObra=0.0
    __montoSeguro=0.0


    def __init__(self,dni,nombre,direccion,telefono,tarea,fechaInicio,fechaFinalizacion,montoV,costoObra,montoSeguro):
          super().__init__(dni,nombre,direccion,telefono)
          self.__tarea=tarea
          self.__fechaInicio=fechaInicio
          self.__fechaFinalizacion=fechaFinalizacion
          self.__montoV=montoV
          self.__costoObra=costoObra
          self.__montoSeguro=montoSeguro
    def getDNI(self):
        return super().getdni()
    def getTarea(self):
        return self.__tarea
    def getCosto(self):
        return self.__costoObra
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    def getSueldoFinal(self):
        #Sueldo = costo de la obra - viático- monto del seguro de vida
        sueldoF= self.__costoObra - self.__montoV - self.__montoSeguro      
        return sueldoF

    def modificarViatico(self,nuevoViatico):
        self.__montoV=nuevoViatico
        print("El valor ha sido modificado exitosamente")
    def __str__(self):
        s=""
        s=super().__str__()
        s+=f"Tarea que realiza:{self.__tarea},Fecha de Inicio:{ self.__fechaInicio},Fecha de Finalizacion{self.__fechaFinalizacion},Monto Viatico:{ self.__montoV},Costo Obra:{self.__costoObra},Monto Seguro:{ self.__montoSeguro}"
        return s
