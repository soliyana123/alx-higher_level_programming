#!/usr/bin/python3
""" Base class of all other classes in this project"""
import json
import os
import csv



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
           

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)       


    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        my_list = []
        fname = cls.__name__ + '.json'
        if (list_objs is not None):
            for ins in list_objs:
                my_list.append(ins.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(fname, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """
        return a string of json
        """
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """
        new instance
        """
        new_ins = None
        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 1)
        elif cls.__name__ == "Square":
            new_ins = cls(1)
        new_ins.update(**dictionary)
        return new_ins
