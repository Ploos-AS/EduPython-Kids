# M3.3 – Catch the star! ⭐

## 🎯 Mission

Put a target on the screen. When the player catches it, make it jump somewhere new.

## 💻 Add a target

```python
import random

star = turtle.Turtle()
star.shape("circle")
star.penup()
star.goto(150, 80)
```

## ⭐ Did I catch it?

```python
def check_catch():
    if player.distance(star) < 25:
        move_star()
```

Call `check_catch()` after each player move.

## 🎲 Make it jump

```python
def move_star():
    x = random.randint(-250, 250)
    y = random.randint(-150, 150)
    star.goto(x, y)
```

Now you never know exactly where the target will appear.

## 🔧 Change

Try changing `25`. Does `10` make catching harder? What about `60`?

## ⭐ Challenge

Change the target's shape or size and decide what the player is collecting in your game.

## 🐞 Bug hunt

If a catch does nothing, print `player.distance(star)` and use the number as a clue.

## 🧠 What you learned

- the game can measure the distance between two things
- `if` can decide when something is caught
- random numbers can make each game different

**Next mission:** How many can you catch? Let's add points!
