# M3.4 – Score! 🏆

## 🎯 Mission

You can catch the target. Now make the game remember how many you have caught.

Keep your working M3.3 game. We only need to add a score and a scoreboard.

## 🧠 A number the game remembers

Near the top of the program, after `STEP`, add:

```python
score = 0
```

## 🏆 Make a scoreboard

After you create the player and target, add:

```python
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 160)
```

Then add this function with your other functions:

```python
def show_score():
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 18, "normal")
    )
```

Call `show_score()` once before `turtle.done()`. Run the game. You should see **Score: 0**.

## ⭐ Earn a point

Replace your old `check_catch()` with:

```python
def check_catch():
    global score

    if player.distance(star) < 25:
        score = score + 1
        show_score()
        move_star()
```

Run it and catch the target.

**1! 2! 3!** The game remembers what you did.

You do not need to memorise `global`. Here it lets this function change the same score the rest of the game uses.

## 🔧 Change

Make each target worth 5 or 10 points. Which rule do you like?

## ⭐ Challenge

Make something special happen at 10 points:

```python
if score == 10:
    print("SUPER PLAYER!")
```

## 🐞 Bug hunt

If the score does not change, use `print(score)`. If old scores are written on top of new ones, check `scoreboard.clear()`.

## 🧠 What you learned

- a variable can be a game's memory
- an event can change the score
- text can show the player what is happening
- you can improve a working game without rebuilding it

**Next mission:** A monster is coming! 👾
