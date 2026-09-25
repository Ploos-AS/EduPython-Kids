"""EduPython Kids: simple functions."""

import random


def greet(name):
    return "Hei " + name + "!"


def roll_die():
    return random.randint(1, 6)


print(greet("Python-programmerer"))
print("Terningen viser", roll_die())
