# M3.3 – Catch the star! ⭐

## 🎯 Mission

Put a target on the screen. When the player catches it, make it jump somewhere new.

Keep your working movement program from M3.2. We will add one new piece at a time.

## 💻 Add a target

At the top, add `random` beside your Turtle import:

```python
import random
import turtle
```

After you create `player`, add:

```python
star = turtle.Turtle()
star.shape("circle")
star.penup()
star.goto(150, 80)
```

Run the program. You should see both the player and the target before continuing.

## 🎲 Make the target jump

Put this function above the keyboard setup:

```python
def move_star():
    x = random.randint(-250, 250)
    y = random.randint(-150, 150)
    star.goto(x, y)
```

For a quick test, temporarily add `move_star()` before `turtle.done()`. Run the program a few times. The target should start in different places.

Then remove that temporary test call.

## ⭐ Did I catch it?

Add:

```python
def check_catch():
    if player.distance(star) < 25:
        move_star()
```

Now add this line at the end of **each** movement function:

```python
check_catch()
```

Run the game and catch the target several times.

## 🔧 Change

Try changing `25` to `10`, then `60`. Which feels fair?

Try a smaller random area too. Does that make the game easier?

## ⭐ Challenge

Change the target's shape or size. What is the player collecting in your game — treasure, food, or an energy ball?

## 🐞 Bug hunt

If nothing happens when you touch the target, check that `check_catch()` is called after movement. You can also print:

```python
print(player.distance(star))
```

## 🧠 What you learned

- the game can measure the distance between two things
- `if` can decide when something is caught
- random numbers can make each game different
- a working program can grow one small piece at a time

**Next mission:** How many can you catch? Let's add points!
