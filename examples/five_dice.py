"""EduPython Kids: repeat five dice throws."""

import random

for throw in range(1, 6):
    value = random.randint(1, 6)
    print("Kast", throw, "ble", value)
