#!/usr/bin/python3
"""
Rectangle class
"""

from models.base import Base

class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        var for the rec
        """
    
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retriebe the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set passet private attribute of width """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieve private instance attribute x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ set private instance attribute x """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieve private instance sttribute y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set private instance attribute y """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

