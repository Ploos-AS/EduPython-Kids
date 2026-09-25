# 12 – Project: Monster Battle

## 🎯 Mission

Build a small text game where you meet a monster.

Several Python tools you already know will now work together in one program.

## 💻 The game

```python
import random

def roll():
    return random.randint(1, 6)

player_health = 10
monster_health = 10

print("A monster appears!")

while player_health > 0 and monster_health > 0:
    input("Press Enter to attack...")

    damage = roll()
    monster_health = monster_health - damage
    print("You deal", damage, "damage.")

    if monster_health <= 0:
        break

    damage = roll()
    player_health = player_health - damage
    print("The monster deals", damage, "damage.")
    print("Your health:", player_health, "| Monster health:", monster_health)

if player_health > 0:
    print("You won! 🎉")
else:
    print("The monster won this time.")
```

## 🧰 What are we using?

- `random`
- variables and game state
- `input()`
- `while`
- `if`
- functions and `return`
- arithmetic

`player_health` and `monster_health` are game state: values that change while the game runs.

`break` stops the loop immediately. Here we use it when the monster has no health left.

## 🔧 Change

Start with one small change, such as giving the monster more or less health.

Run the game several times before changing something else.

## 🤔 Think

How does the difficulty change if the monster starts with 20 health?

What happens if `roll()` uses `random.randint(1, 10)`?

## ⭐ Make the game yours

Choose at least two improvements:

- Give the monster a name.
- Let the player choose a nickname.
- Create different monsters.
- Add a health potion.
- Let the player choose attack or defend.
- Make critical hits when the die shows 6.
- Create a new function for the monster's attack.

## 🧪 Playtests

Play at least three times.

Write down one bug or surprise you found, one rule you changed, and what the change did to the game.

You are not only a player now. You are testing and developing your own game.

## 🧠 What you learned

- A larger program can be built from small concepts you already know.
- Game state changes while a game runs.
- Functions can make parts of a program reusable.
- Testing helps find both bugs and rules you want to improve.
- Improving one small part at a time is often easier.
