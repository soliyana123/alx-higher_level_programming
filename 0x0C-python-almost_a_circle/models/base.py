#!/usr/bin/python3
"""
New class base
"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        new var
        """
        if id is not none:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

