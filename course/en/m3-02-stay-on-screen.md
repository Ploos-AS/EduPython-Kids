# M3.2 – Stay on screen!

## 🎯 Mission

In the last mission you could move with the arrow keys. But what happens if you keep going?

**Oops — the player disappears!** Now we will teach the game where the edges are.

## 💻 Start with four directions

This is a complete starting program:

```python
import turtle

screen = turtle.Screen()
screen.title("Stay on screen")
screen.setup(600, 400)

player = turtle.Turtle()
player.shape("turtle")
player.penup()

STEP = 20

def right():
    player.setx(player.xcor() + STEP)

def left():
    player.setx(player.xcor() - STEP)

def up():
    player.sety(player.ycor() + STEP)

def down():
    player.sety(player.ycor() - STEP)

screen.listen()
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

turtle.done()
```

Run it and deliberately drive the player out of the window.

## 🗺 Where am I?

Python can ask where the player is:

```python
print(player.xcor())
print(player.ycor())
```

`x` tells you left and right. `y` tells you down and up. The middle is about `x = 0`, `y = 0`.

You do not need to memorise this. Put this line inside one movement function and watch the numbers:

```python
print(player.xcor(), player.ycor())
```

## 🧱 Build the right wall

Replace your `right()` function with:

```python
def right():
    if player.xcor() < 280:
        player.setx(player.xcor() + STEP)
```

Run toward the right edge again. Now the player stops.

## 🔧 Change

Try `250` instead of `280`. Then try `100`. Can you see how the number moves the invisible wall?

## ⭐ Challenge

Add the other three walls. These clues help:

```python
player.xcor() > -280
player.ycor() < 180
player.ycor() > -180
```

Which clue belongs to left, up, and down? Experiment.

## 🌟 Extra

Instead of stopping at an edge, try sending the player back to the middle with:

```python
player.goto(0, 0)
```

## 🐞 Bug hunt

If the player stops too early or still disappears, print `xcor()` or `ycor()`, move slowly toward the edge, and use the number as a clue.

## 🧠 What you learned

- a character has a position
- x describes left and right
- y describes down and up
- `if` can make rules about where the player may go

**Next mission:** Catch the star!
