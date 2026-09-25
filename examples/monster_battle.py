"""EduPython Kids: a tiny text battle game."""

import random


def roll():
    return random.randint(1, 6)


player_health = 10
monster_health = 10

print("Et monster dukker opp!")

while player_health > 0 and monster_health > 0:
    input("Trykk Enter for å angripe...")

    damage = roll()
    monster_health -= damage
    print("Du gjør", damage, "skade.")

    if monster_health <= 0:
        break

    damage = roll()
    player_health -= damage
    print("Monsteret gjør", damage, "skade.")
    print("Dine liv:", player_health, "| Monsterets liv:", monster_health)

if player_health > 0:
    print("Du vant! 🎉")
else:
    print("Monsteret vant denne gangen.")
