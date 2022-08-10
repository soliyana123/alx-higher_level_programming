#!/usr/bin/python3
"""
New class base
"""
import json
import csv
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write json in a new  file
        """
        new_file = "{}.json".format(cls.__name__)
        list_wri = []
        if list_objs is not None:
            list_wri = [l.to_dictionary()for l in list_objs]
        with open(new_file, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_wri))

