
from ClaseEmpleadoContratado import EmpleadoContratado
from ClaseEmpleadoExterno import EmpleadoExterno
from ClaseEmpleadoPlanta import EmpleadoPlanta
from ClaseColeccion import Coleccion
from menu import Menu
from datetime import datetime

def test():
    unaColeccion=Coleccion(1)

    fechaInicio = datetime.strptime('2021-04-22', '%Y-%m-%d')
    fechaFinalizacion = datetime.strptime('2021-09-17', '%Y-%m-%d')
    unEmpleadoContratado=EmpleadoContratado('43555444','Matias Gonzalez','Capital','2641213454',fechaInicio,fechaFinalizacion,22)
    unaColeccion.cargarEmpleadoPlanta(unEmpleadoContratado)




if __name__ == '__main__':
    test()
    input()
    tamaño=int(input("Ingresar Tamaño de el Arreglo:"))
    menu=Menu()
    menu.Ejecutar(tamaño)
