#!/usr/bin/python3
"""
Rectangle class
"""



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


