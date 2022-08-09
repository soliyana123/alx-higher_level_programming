#!/usr/bin/python3
""" Base class of all other classes in this project"""

class Base:
    """ first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
