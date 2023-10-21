class cone:
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

class blue_cone(cone):

    def __str__(self):
        return "Blue cone at position: ({}, {})".format(self.__x, self.__y)

class yellow_cone(cone):

    def __str__(self):
        return "Yellow cone at position: ({}, {})".format(self.__x, self.__y)
