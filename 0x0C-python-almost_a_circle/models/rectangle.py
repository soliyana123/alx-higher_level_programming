#!/usr/bin/python3
""" First Rectangle that inherits from Base """

class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

