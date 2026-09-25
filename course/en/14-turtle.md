# 14 – Draw with Turtle

## 🎯 Mission

Make a little turtle draw a square on the screen.

Turtle comes with many Python installations and needs a graphical environment with Tk support.

## 💻 First drawing

```python
import turtle

pen = turtle.Turtle()

for side in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
```

You are already using a loop. Instead of four nearly identical blocks, the program repeats the same two movements four times.

## 🔧 Change

What happens if you change 100? Try it.

What happens if you change 90? Try again.

## 🔺 Draw a triangle

```python
for side in range(3):
    pen.forward(120)
    pen.right(120)
```

## 🤔 Think

A full turn is 360 degrees. For a shape with equal turns, try:

```text
turn = 360 / number_of_sides
```

Can you use the idea to draw a pentagon?

## ⭐ Challenge

Create a function:

```python
def polygon(sides, length):
    ...
```

It should be able to draw several different polygons.

## 🎨 Make it yours

Experiment with pen size, colours, lengths and angles.

There is no single correct drawing.

## 🐞 Bug hunt

If the Turtle window does not open at all, the problem may be the Python/Tk environment rather than your code. Ask an adult to check the [installation guide](../../docs/INSTALL.md).

If the window opens but the shape looks strange, test one value at a time.

## 🧠 What you learned

- Code can control graphics and movement.
- Loops are useful when a shape has repeated sides.
- Angles change the direction the pen moves.
- Functions can make drawing code reusable.
