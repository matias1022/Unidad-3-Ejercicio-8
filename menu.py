import os
from ClaseColeccion import Coleccion
from ClaseEmpleadoContratado import EmpleadoContratado
from ClaseEmpleadoExterno import EmpleadoExterno
from ClaseEmpleadoPlanta import EmpleadoPlanta
from ClaseIGerente import IGerente
from ClaseITesorero import ITesorero

class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self,tamaño):
          os.system('cls')
          salir = False
          coleccion=Coleccion(tamaño)
          coleccion.agregarEmpleadoPlanta()
          coleccion.agregarEmpleadoContratado()
          coleccion.agregarEmpleadoExterno()

          while salir == False:
              print('1-\t Ingresar el DNI de un empleado y la cantidad de horas trabajadas hoy e incrementar la cantidad de las horas trabajadas del empleado.')
              print('2-\tDada una tarea mostrar el monto a pagar para ella. Solo se consideran las tareas que no han finalizado.')
              print('3-\tLa empresa dará una ayuda solidaria a los empleados cuyo sueldo sea inferior a $25000; listar nombre, dirección y DNI de los empleados que les corresponde la ayuda.')
              print('4-\tMostrar nombre, teléfono y sueldo a cobrar de todos los empleados.')
              print('5-\tIngreso al sistema como Tesorero o Gerente')

              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1:  
                 dni=input("Ingresar DNI de el empleado a buscar:")#1
                 horas=int(input("Ingresar la cantidad de horas trabajadas hoy dia:"))
                 if coleccion.verificarDNI(dni)==True:
                       coleccion.registrarHora(horas,dni)
                 else: print("No hay empleado con el DNI ingresado")
              elif self.__op == 2: 
                 tarea=input("Ingresar Tarea(Carpinteria, Electricidad, Plomeria):")
                 if tarea=="Carpinteria" or tarea=="Electricidad" or tarea=="Plomeria":
                     coleccion.mostrarMonto(tarea)
                 else: print("La tarea ingresada no esta disponible")
              elif self.__op == 3: 
                  coleccion.ayuda()
              elif self.__op == 4: 
                  coleccion.mostrarSueldo()
              elif self.__op == 5: 
                  usuario=input("\nIngrese el nombre de usuario: ")
                  passw=input("\nIngrese la contraseña: ")

                  if usuario == "uTesorero" and passw == "ag@74ck":
                         self.Tesorero(ITesorero(coleccion))

                  elif usuario== "uGerente" and passw =="ufC77#!1":
                      self.Gerente(IGerente(coleccion))
                  else: print("Credenciales incorrectas")
                 
                 
              elif self.__op == 0: 
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')

        
          print('Cerrando Menú..')   



      def Tesorero(self,lista):
        DNI=input("Ingrese el numero de documento de el empleado: ")
        lista.gastosSueldoPorEmpleado(DNI)
      def Gerente(self,lista):
        op = int(input("1. Modificar Sueldo Basico \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Opcion: " ))
        while op > 0:
            self.opciones(op,lista)
            op = int(input("1. Modificar Báscio \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Otra Opcion: " ))
      def opciones(self,op,lista):
        dni=input("Ingrese el numero de documento de el empleado: ")
        valor=input("\nIngresar valor a modificar: ")
        if op==1:
            lista.modificarSueldoB(dni,valor)

        if op == 2:
            lista.modificarViatico(dni,valor)

        elif op ==3:
            lista.modificarValorH(dni,valor)
