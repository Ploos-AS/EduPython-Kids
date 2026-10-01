# M3.5 – Watch out! 👾

## 🎯 Mission

Keep collecting targets, but do not let the monster catch you.

## 👾 Add the monster

```python
monster = turtle.Turtle()
monster.shape("square")
monster.penup()
monster.goto(-200, -100)
```

## 👣 Make it chase you

```python
def move_monster():
    monster.setheading(monster.towards(player))
    monster.forward(8)
    screen.ontimer(move_monster, 100)
```

Call `move_monster()` once before `turtle.done()`.

## 💥 Did it catch you?

Inside the monster function:

```python
if monster.distance(player) < 25:
    print("The monster caught you!")
```

Try getting caught on purpose.

## 🔧 Change

Try monster speeds of `3`, `8`, and `15`. Choose a speed that is fun, not just difficult.

Think of `ontimer()` as: **Monster, take another step in a moment.**

## ⭐ Challenge

Choose a fair starting position for the monster.

## 🌟 Extra

Store the monster speed in a variable and try making it faster when the player earns points.

## 🐞 Bug hunt

If the monster moves only once, check that `ontimer()` is inside the function. If it never starts, check that you call `move_monster()` once.

## 🧠 What you learned

- a character can move without a key press
- `towards()` can point one character at another
- speed changes difficulty

**Next mission:** The monster caught you — but you have three lives! ❤️❤️❤️
