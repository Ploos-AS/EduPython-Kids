# M3.6 – Three lives! ❤️❤️❤️

## 🎯 Mission

Each time the monster catches you, lose one life. The game ends when you reach zero.

```python
lives = 3
```

## ❤️ Show lives

Create a text Turtle and a `show_lives()` function, just like the scoreboard.

## 💥 Lose a life

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

## 🛑 GAME OVER

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

Add a `game_running` variable so the monster can stop after GAME OVER. At the top of its movement function, return if the game is no longer running.

## 🔧 Change

Try five lives or only one. Which is more fun?

## ⭐ Challenge

Make a `restart()` function and connect it to the R key. Restart is extra — closing and running the game again is fine too.

## 🐞 Bug hunt

If you lose several lives at once, move the player and monster farther apart after a hit.

## 🧠 What you learned

- variables can remember lives as well as points
- games can have rules for losing
- a game can be running or finished

**Next mission:** Make the game yours! 🎨
