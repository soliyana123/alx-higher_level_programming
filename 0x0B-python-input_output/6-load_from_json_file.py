#!/usr/bin/python3
""" function that create an object from json file """
import json

def load_from_json_file(filename):
    """ function that create an object from json file """
   with open(filename, 'r') as f:
       return (json.load(f))
