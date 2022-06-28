#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % (-10 if number < 0 else 10)
print("Last digit of", number, "is", ldigit, "and is ", end="")
if ldigit == 0:
    print("0")
elif ldigit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
