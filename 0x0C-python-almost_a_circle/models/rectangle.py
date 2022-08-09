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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

     def area(self):
        """
        Return area of the a rectangle
        """
        return self.__width * self.__height

     def display(self):
         """
         Displays the rectangle with a # sign
         """
         print("\n" * self.__y, end="")
         print((" " * self.__x + "#" * self.__width + "\n") *
               self.__height, end="")
     def __str__(self):
        """
        Str Method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)


     def update(self, *args, **kwargs):
        """
        update public method
        """
        if args and len(args) != 0:
            i = 0
            att_list = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
                   
     def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return (my_dict)              

