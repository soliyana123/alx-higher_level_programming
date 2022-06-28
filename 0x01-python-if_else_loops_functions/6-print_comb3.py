#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if b > a and a != 8:
            print("{}{}".format(a, b), end=', ')
        elif a == 8 and b == 9:
            print("{}{}".format(a, b))
