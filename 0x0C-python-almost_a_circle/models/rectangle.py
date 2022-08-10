
#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""
class Base:
    """
    New class base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        new var
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects



class Rectangle(Base):
    """A representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

