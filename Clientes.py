class Clientes:
    # constructor
    def __init__(self, id, nombres, apellidos, dui, telefono):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dui = dui
        self.__telefono = telefono

    # definicion de metodos getter/setter
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombres(self):
        return self.__nombres

    def setNombres(self, nombres):
        self.__nombres = nombres

    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def getDui(self):
        return self.__dui
    
    def setDui(self, dui):
        self.__dui = dui

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono
