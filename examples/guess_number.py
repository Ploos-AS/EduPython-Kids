"""EduPython Kids: first guessing game."""

import random

secret = random.randint(1, 10)
guess = int(input("Gjett et tall fra 1 til 10: "))

if guess == secret:
    print("Riktig! 🎉")
elif guess < secret:
    print("For lavt! Tallet var", secret)
else:
    print("For høyt! Tallet var", secret)
