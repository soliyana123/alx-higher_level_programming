#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        strng = ""
        for b in a:
            print("{:s}{:d}".format(strng, b), end='')
            strng = " "
        print()
