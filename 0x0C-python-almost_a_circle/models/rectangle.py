#!/usr/bin/python3
"""
class rectangle
"""

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        var for rec
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


