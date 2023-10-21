class cono:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

class cono_azul(cono):

    def __str__(self):
        return "Cono azul en la posición: ({}, {})".format(self.__x, self.__y)

class cono_amarillo(cono):

    def __str__(self):
        return "Cono amarillo en la posición: ({}, {})".format(self.__x, self.__y)