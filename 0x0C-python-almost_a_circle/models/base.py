#!/usr/bin/python3
"""
New class base
"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        change to stri
        """
        if list_dictionaries and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"
