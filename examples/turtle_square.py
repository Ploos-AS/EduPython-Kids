"""EduPython Kids: draw a square with Turtle."""

import turtle

pen = turtle.Turtle()

for _ in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
