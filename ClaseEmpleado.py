class Empleado:
    __dni=""
    __nombre=""
    __direccion=""
    __telefono=""
    
    def __init__(self,dni="",nombre="",direccion="",telefono=""):
        self.__dni=dni
        self.__direccion=direccion
        self.__telefono=telefono
        self.__nombre=nombre
    def getdni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def __str__(self):
        return f'''DNI:{self.__dni},
        Nombre:{self.__nombre},Direccion:{self.__direccion},Telefono:{self.__telefono}'''