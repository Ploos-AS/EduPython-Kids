# M3.5 – Watch out! 👾

## 🎯 Mission

Keep your score game from M3.4. Now add a monster that moves by itself and follows you.

## 👾 Add the monster

After you create the target, add:

```python
monster = turtle.Turtle()
monster.shape("square")
monster.penup()
monster.goto(-200, -100)
```

Run once. Make sure the monster appears before making it move.

## 👣 Make it chase you

Add this function:

```python
def move_monster():
    monster.setheading(monster.towards(player))
    monster.forward(8)

    screen.ontimer(move_monster, 100)
```

Start it **once** near the bottom of the program, before `turtle.done()`:

```python
move_monster()
```

Run the game.

**The monster follows you!**

Think of `ontimer()` as: **Monster, take another step in a moment.**

## 💥 Did it catch you?

Inside `move_monster()`, after `monster.forward(8)` and before `ontimer()`, add:

```python
if monster.distance(player) < 25:
    print("The monster caught you!")
```

Try getting caught on purpose.

## 🔧 Change

Try speeds of `3`, `8`, and `15`. Choose a speed that is fun, not just difficult.

## ⭐ Challenge

Choose a fair starting place for the monster with `monster.goto(...)`.

## 🌟 Extra

Make:

```python
monster_speed = 5
```

Then use:

```python
monster.forward(monster_speed)
```

Can you make the monster faster later? Skip this if it becomes frustrating — it is extra.

## 🐞 Bug hunt

If the monster moves only once, check that `screen.ontimer(move_monster, 100)` is inside the function. If it never starts, check the one `move_monster()` call near the bottom.

## 🧠 What you learned

- a character can move without a key press
- `towards()` can point one character at another
- distance can detect when the monster is close
- speed changes difficulty

**Next mission:** The monster caught you — but you have three lives! ❤️❤️❤️
