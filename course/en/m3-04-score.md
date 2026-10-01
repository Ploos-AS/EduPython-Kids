# M3.4 – Score! 🏆

## 🎯 Mission

Make the game remember how many targets you catch.

Start with:

```python
score = 0
```

## 🏆 Show the score

Create a Turtle that only writes text:

```python
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 160)

def show_score():
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 18, "normal")
    )
```

## ⭐ Earn a point

```python
def check_catch():
    global score

    if player.distance(star) < 25:
        score = score + 1
        show_score()
        move_star()
```

**1! 2! 3!** The game remembers what you did.

You do not need to memorise `global`. Here it lets the function change the score used by the rest of the game.

## 🔧 Change

Make each target worth 5 or 10 points. Which rule do you like?

## ⭐ Challenge

Make something special happen when the score reaches 10.

## 🐞 Bug hunt

Use `print(score)` to see what the game remembers. If numbers are written on top of each other, check `scoreboard.clear()`.

## 🧠 What you learned

- a variable can be a game's memory
- events can change the score
- text can tell the player what is happening

**Next mission:** A monster is coming! 👾
