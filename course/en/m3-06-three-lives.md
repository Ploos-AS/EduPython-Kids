# M3.6 – Three lives! ❤️❤️❤️

## 🎯 Mission

The monster caught you, but the game is not over yet.

Keep your M3.5 game. Give the player **three lives** and make the game end at zero.

## ❤️ Remember the lives

Near `score = 0`, add:

```python
lives = 3
```

Create another text Turtle:

```python
life_board = turtle.Turtle()
life_board.hideturtle()
life_board.penup()
life_board.goto(-250, 160)
```

Add:

```python
def show_lives():
    life_board.clear()
    life_board.write(
        f"Lives: {lives}",
        font=("Arial", 18, "normal")
    )
```

Call `show_lives()` once when the game starts.

## 💥 Lose one life

Add:

```python
def caught_by_monster():
    global lives

    lives = lives - 1
    show_lives()

    player.goto(0, 0)
    monster.goto(-200, -100)
```

Now replace the monster's print message with:

```python
if monster.distance(player) < 25:
    caught_by_monster()
```

Get caught on purpose.

**3 → 2 → 1 ...**

## 🛑 GAME OVER

Change `caught_by_monster()` so zero lives calls a new function:

```python
def caught_by_monster():
    global lives

    lives = lives - 1
    show_lives()

    if lives == 0:
        game_over()
    else:
        player.goto(0, 0)
        monster.goto(-200, -100)
```

Add:

```python
def game_over():
    monster.hideturtle()
    player.hideturtle()
    star.hideturtle()

    scoreboard.goto(0, 0)
    scoreboard.clear()
    scoreboard.write(
        "GAME OVER",
        align="center",
        font=("Arial", 28, "bold")
    )
```

## ⚠️ Stop the monster too

Near your other game variables, add:

```python
game_running = True
```

At the start of `move_monster()` add:

```python
if not game_running:
    return
```

And inside `game_over()` add:

```python
global game_running
game_running = False
```

That means: **if the game is over, stop here.**

## 🔧 Change

Try five lives or only one. Which is more fun?

## ⭐ Challenge — play again

Restart is extra. First make sure the normal game works all the way to GAME OVER.

If you want a bigger challenge, make a `restart()` function that resets lives, score, positions, and `game_running`, then connect it to the R key.

Closing the game and running it again is completely fine.

## 🐞 Bug hunt

If you lose several lives almost at once, make sure the player and monster move apart after a hit. If the monster continues after GAME OVER, check `game_running` and the test at the top of `move_monster()`.

## 🧠 What you learned

- variables can remember lives as well as score
- games can have rules for hits and losing
- a game can be running or finished
- functions can collect everything that should happen after an event

**Next mission:** Make the game yours! 🎨
