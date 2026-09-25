"""EduPython Kids: guessing game with repeated attempts."""

import random

secret = random.randint(1, 20)
guess = None
attempts = 0

while guess != secret:
    guess = int(input("Gjett et tall fra 1 til 20: "))
    attempts += 1

    if guess < secret:
        print("For lavt!")
    elif guess > secret:
        print("For høyt!")

print("Riktig! Du brukte", attempts, "forsøk.")
