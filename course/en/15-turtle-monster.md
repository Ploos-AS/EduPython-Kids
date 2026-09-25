# 15 – Turtle challenge: Robot Monster

## 🎯 Mission
Draw your own robot monster from simple shapes. The goal is to use code as a drawing tool and split a bigger idea into smaller parts.

## 💻 Start with one building block
```python
import turtle
pen = turtle.Turtle()
pen.speed(0)

def square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

square(100)
turtle.done()
```

## 🧱 Build with functions
Create functions for at least three parts, such as body, eye, antenna, foot or mouth. Move the pen with `penup()`, `goto(x, y)` and `pendown()`. Test one function at a time.

## 🔧 Change
Make one function flexible with a parameter, such as `def eye(size):`, and try two values.

## 🤔 Think
Why are functions useful for two identical eyes or several legs? What can you reuse for a second monster?

## ⭐ Challenge
Create your own complete monster. Give it a name and write the name with `pen.write()`.

## 🌟 Extra
Create two monsters on the same screen and vary their size or other values.

## 🐞 Bug hunt
If the whole drawing is hard to debug, temporarily comment out function calls and test one body part alone. Check its shape, starting position, and whether the pen is up or down while moving.

## 🧠 What you learned
- A larger problem can be split into smaller functions.
- The same function can be reused.
- Parameters create variations.
- Testing small parts separately makes bugs easier to find.
