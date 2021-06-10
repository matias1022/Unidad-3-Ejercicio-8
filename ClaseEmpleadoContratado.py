import datetime
from ClaseEmpleado import Empleado


class EmpleadoContratado(Empleado):
    __fechaInicio= None
    __fechaFinalizacion=None
    __cantHorasT=0
    valorHora=500
    def __init__(self,dni,nombre,direccion,telefono,fechaInicio,fechaFinalizacion,cantHorasT):
         super().__init__(dni,nombre,direccion,telefono)
         self.__fechaInicio=fechaInicio
         self.__fechaFinalizacion=fechaFinalizacion
         self.__cantHorasT=cantHorasT
    def getDNI(self):
        return super().getdni()
    def getSueldoFinal(self):
        #Sueldo = cantidad de horas trabajadas * valor de la hora
        sueldoF=self.__cantHorasT*self.valorHora
        
        return sueldoF
    def incrementarH(self,cantidadHoy):
        self.__cantHorasT+=cantidadHoy
        print("La cantidad de horas trabajadas actualemtente es de")
        print(self.__cantHorasT)


    @classmethod
    def getValorporhora(cls):
        return int(cls.valorhora)


    @classmethod
    def modificarValorH(cls,valorHoraNuevo):
        cls.valorHora=valorHoraNuevo       
    def __str__(self):
        s=""
        s=super().__str__()
        s+=f"Fecha de Inicio:{self.__fechaInicio},Fecha de Finalizacion:{ self.__fechaFinalizacion},Cantidad de Horas:{self.__cantHorasT},Valor por Hora:{self.valorHora}"
        return s