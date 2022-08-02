#!/usr/bin/python3
"""writes a string to text file (UTF8)"""

def write_file(filename="", text=""):
    """writes a string to text file (UTF8)"""
       with open(filename, 'w', encoding='utf-8') as f:
           return (f.write(text))
