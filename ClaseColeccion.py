from ClaseEmpleado import Empleado
import numpy as np
import csv
from ClaseEmpleadoContratado import EmpleadoContratado
from ClaseEmpleadoExterno import EmpleadoExterno
from ClaseEmpleadoPlanta import EmpleadoPlanta
from datetime import datetime
from ClaseITesorero import ITesorero
from ClaseIGerente import IGerente
from zope.interface import implementer

@implementer (ITesorero)
@implementer (IGerente)

class Coleccion:
    __empleados=None
    __i=0
    __actual=0
    __dimension=0
    def __init__(self,dimension):
        self.__dimension=dimension
        self.__tamaño=0
        self.__empleados= np.empty(self.__dimension, dtype=Empleado)
    
    def agregarEmpleadoPlanta(self):
        archivo = open('planta.csv')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            dni=fila[0]
            nombre=fila[1]
            direccion=fila[2]           
            telefono=fila[3]
            sueldoB=float(fila[4]) 
            antiguedad=float(fila[5]) 
            unEPlanta = EmpleadoPlanta(dni,nombre, direccion,telefono, sueldoB,antiguedad)
            '''self.__empleados[self.__i]=unEPlanta
            self.__i+=1
            self.__tamaño+=1'''
            self.cargarEmpleadoPlanta(unEPlanta)
        archivo.close()
    def cargarEmpleadoPlanta(self,unEmpleado):
            if self.__dimension==self.__actual:
               self.__dimension+=1
               self.__empleados.resize(self.__dimension,refcheck=False)
            self.__empleados[self.__actual]=unEmpleado
            self.__actual+=1
            print(unEmpleado)
        
    def agregarEmpleadoContratado(self):
        archivo = open('contratados.csv')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            dni=fila[0]
            nombre=fila[1]
            direccion=fila[2]           
            telefono=fila[3]
            fechaInicio=fila[4]
            fechaFinalizacion=fila[5]
            cantHorasT=int(fila[6])
            unEContratado = EmpleadoContratado(dni,nombre, direccion,telefono, fechaInicio,fechaFinalizacion,cantHorasT)
            '''self.__empleados[self.__i]=unEContratado
            self.__i+=1
            self.__tamaño+=1'''
            self.cargarEmpleadoPlanta(unEContratado)

        print(unEContratado)
        archivo.close()
    def agregarEmpleadoExterno(self):
        archivo = open('externos.csv')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            dni=fila[0]
            nombre=fila[1]
            direccion=fila[2]           
            telefono=fila[3]
            tarea=fila[4]
            fecha_str_inicio = fila[5]
            fecha_str_fin = fila[6]
            datetime1 = datetime.strptime(fecha_str_inicio, '%Y-%m-%d %H:%M:%S.%f')
            datetime2 = datetime.strptime(fecha_str_fin, '%Y-%m-%d %H:%M:%S.%f')
            montoV=float(fila[7])
            costoObra=float(fila[8])  
            montoSeguro=float(fila[9])
            unEExterno = EmpleadoExterno(dni,nombre, direccion,telefono,tarea, datetime1,datetime2,montoV,costoObra,montoSeguro)
            '''self.__empleados[self.__i]=unEExterno
            self.__i+=1
            print(unEExterno)
            self.__tamaño+=1'''
            self.cargarEmpleadoPlanta(unEExterno)
        archivo.close()

    def verificarDNI(self,dni):
        i=0
        print(dni)
        encontrado=False
        while not encontrado and i<int(self.__dimension):  

              if self.__empleados[i].getDNI()==dni:
                       encontrado=True                                  
              i=i+1
        return encontrado  
    def registrarHora(self,cant,dni):
        i=0
        print(dni)
        encontrado=False
        while not encontrado and i<int(self.__dimension):       
              if self.__empleados[i].getDNI()==dni:
                  if isinstance(self.__empleados[i],EmpleadoContratado):
                       self.__empleados[i].incrementarH(cant)
                       encontrado=True              
              i=i+1
        if encontrado==True:
            print("Las horas de el empleado contratado se actualizaron")
        else: print("El DNI que puso es de un empleado Externo o de Planta")

    def mostrarMonto(self,tarea):
        encontro=False
        i=0
       # fechaHoy=datetime.today()
        while i<int(self.__dimension) and not encontro:
            if isinstance(self.__empleados[i],EmpleadoExterno):  
                if str(self.__empleados[i].getTarea()) == tarea:
                    
                    if self.__empleados[i].getFechaFinalizacion()>datetime.today():
                          print(f"\n El costo de la tarea es:{self.__empleados[i].getCosto()}")
                          encontro=True
            i=i+1
        if encontro==False:
            print("\nTarea ya Finalizada")

    def ayuda(self):
        i=0
        while i < int(self.__dimension):
            if self.__empleados[i].getSueldoFinal()<25000:
                print("Se le dara ayuda solidaria al empleado:")
                print("----------------------------------")
                print(self.__empleados[i].getSueldoFinal())
                print(self.__empleados[i].getNombre())
                print(self.__empleados[i].getDireccion())
                print(self.__empleados[i].getdni())
            i+=1
    def mostrarSueldo(self):
        i=0
        print("-------Listado-------")
        while i < len(self.__empleados):
                print("----------------------------------")
                print(self.__empleados[i].getNombre())
                print(self.__empleados[i].getTelefono())
                print(self.__empleados[i].getSueldoFinal())
                i+=1
    def gastosSueldoPorEmpleado(self,DNI):
        i=0

        while i<int(self.__dimension) and str(self.__empleados[i].getdni()) != DNI:
            i+=1

        if i<int(self.__dimension):
            print("\nNombre: {}\nTelefono: {}\nSueldo: {}".format(self.__empleados[i].getNombre(),self.__empleados[i].getTelefono(),self.__empleados[i].getSueldoFinal()))

        else:
            print("\nEl dni no se encuentra .")


    def modificarSueldoB(self,dni,nuevo):
        i=0
        while i<int(self.__dimension) and str(self.__empleados[i].getdni()) !=dni:
            i+=1
        if i<int(self.__dimension):
            if isinstance(self.__empleados[i],EmpleadoPlanta):
                self.__empleados[i].modificarSueldoB(nuevo)
            else:
                print("\nEl dni no es de un Empleado De Planta")
        else:
            print("\nNo se encontro al empleado.")

    def modificarViatico(self,dni,nuevo):
        i=0
        while i<int(self.__dimension) and str(self.__empleados[i].getdni()) !=dni:
            i+=1
        if i<int(self.__dimension):
            if isinstance(self.__empleados[i],EmpleadoExterno):
                self.__empleados[i].modificarViatico(nuevo)
            else:
                print("\El dni no es de un Empleado Externo")
        else:
            print("\nNo se encontro al empleado.")

    def modificarValorH(self,dni,nuevo):
        i=0
        while i<int(self.__dimension) and str(self.__empleados[i].getdni()) !=dni:
            i+=1
        if i<int(self.__dimension):
            if isinstance(self.__empleados[i],EmpleadoContratado):
                self.__empleados[i].modificarValorH(nuevo)
                print("El valor ha sido modificado exitosamente")
            else:
                print("\El dni no es de un Empleado Contratado")
        else:
           print("\nNo se encontro al empleado.")
