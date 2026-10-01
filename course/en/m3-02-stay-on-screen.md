# M3.2 – Stay on screen!

## 🎯 Mission

Keep moving in one direction. **Oops — the player disappears!**

Now we will teach the game where the edges are.

## 💻 Four directions

Use a 600 by 400 Turtle window and move with `setx()` and `sety()`:

```python
STEP = 20

def right():
    player.setx(player.xcor() + STEP)

def left():
    player.setx(player.xcor() - STEP)

def up():
    player.sety(player.ycor() + STEP)

def down():
    player.sety(player.ycor() - STEP)
```

## 🗺 Where am I?

Try:

```python
print(player.xcor(), player.ycor())
```

`x` tells you left and right. `y` tells you down and up. You do not need to memorise it — move and watch the numbers.

## 🧱 Build a wall

```python
def right():
    if player.xcor() < 280:
        player.setx(player.xcor() + STEP)
```

Try the right edge again.

## ⭐ Challenge

Add the other three walls using `-280`, `180`, and `-180`. Experiment to discover which number belongs to which edge.

## 🌟 Extra

Instead of stopping at an edge, try sending the player back to the middle with `player.goto(0, 0)`.

## 🐞 Bug hunt

Print `xcor()` or `ycor()` and move slowly toward the troublesome edge. Numbers can be clues.

## 🧠 What you learned

- a character has a position
- x describes left and right
- y describes down and up
- `if` can make rules about where the player may go

**Next mission:** Catch the star!
