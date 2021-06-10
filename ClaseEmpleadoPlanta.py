from ClaseEmpleado import Empleado


class EmpleadoPlanta(Empleado):
    __sueldoB=0
    __antiguedad=0

    def __init__(self,dni,nombre,direccion,telefono,sueldoB,antiguedad):
         super().__init__(dni,nombre,direccion,telefono)
         self.__sueldoB=sueldoB
         self.__antiguedad=antiguedad
    def getDNI(self):
        return super().getdni()
    def getSueldoFinal(self):
        #Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad
        sueldoF= self.__sueldoB+self.__sueldoB/100*self.__antiguedad
        return sueldoF
    def modificarSueldoB(self,nuevo):
        self.__sueldoB=nuevo        
        print("El valor ha sido modificado exitosamente")  
    def __str__(self):
        s=""
        s=super().__str__()
        s+=f" Sueldo Basico: {self.__sueldoB},Años de antiguedad: {self.__antiguedad}"
        return s
       # {self.__dni}{self.__nombre}{self.__direccion}{self.__telefono}