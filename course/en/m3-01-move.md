# M3.1 – Move!

## 🎯 Mission

Make a little game window and control your character with the arrow keys.

You have already used Turtle for drawing. Now the turtle becomes a **game character**.

## 💻 Start here

```python
import turtle

screen = turtle.Screen()
screen.title("My first game")

player = turtle.Turtle()
player.shape("turtle")
player.penup()

def right():
    player.forward(20)

def left():
    player.backward(20)

screen.listen()
screen.onkey(right, "Right")
screen.onkey(left, "Left")

turtle.done()
```

Run it. Click the game window once if needed, then try the right and left arrow keys.

**You made controls!**

## 🔧 Change

Find the number `20`. Try `50`, then `5`. Which movement feels best?

## 🚀 Four directions

Can you add up and down?

```python
def up():
    player.sety(player.ycor() + 20)

def down():
    player.sety(player.ycor() - 20)
```

Connect them to `"Up"` and `"Down"`.

## 🤔 Think

Which function runs when you press Right? What would you change to make each step bigger?

## ⭐ Challenge

Make the game yours: change the shape, movement speed, window title, or invent one small rule.

## 🐞 Bug hunt

If the keys do nothing, click the Turtle window, check the capital letters in the key names, and check your function names. Change one thing at a time.

## 🧠 What you learned

- a key press can run a function
- Python can move a game character
- small number changes can change how a game feels

**Next mission:** Can we stop the player from disappearing off the screen?
