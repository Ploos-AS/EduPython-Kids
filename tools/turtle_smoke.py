"""Interactive Turtle/Tk smoke test for M2 hands-on qualification."""

from __future__ import annotations

import sys


def main() -> int:
    try:
        import tkinter as tk
        import turtle
    except Exception as exc:
        print(f"FAIL: Tk/Turtle import failed: {exc}")
        return 1

    print(f"Python: {sys.version.split()[0]}")
    print(f"Tk: {tk.TkVersion}")
    print("Opening Turtle window...")
    print("Visual checklist: square visible; text visible; window responds; close by clicking.")

    try:
        screen = turtle.Screen()
        screen.title("EduPython Kids — Turtle qualification")
        pen = turtle.Turtle()
        pen.speed(0)

        for _ in range(4):
            pen.forward(100)
            pen.right(90)

        pen.penup()
        pen.goto(0, -40)
        pen.write("EduPython Kids Turtle OK", align="center")

        print("PASS candidate: Tk window opened and drawing commands completed.")
        print("Visually confirm: [1] square [2] text [3] responsive window.")
        print("Then click the window to close it normally.")
        screen.exitonclick()
    except Exception as exc:
        print(f"FAIL: graphical Turtle test failed: {exc}")
        return 1

    print("Turtle window closed normally.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
