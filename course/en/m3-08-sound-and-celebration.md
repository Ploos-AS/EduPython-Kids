# M3.8 – Sound and celebration! 🔔

## 🎯 Mission

Make the game celebrate when you catch the target.

We start with feedback that works without sound: a flash.

## ✨ Flash the target

```python
def celebrate():
    old_color = star.color()[0]
    star.color("yellow")

    def finished():
        star.color(old_color)

    screen.ontimer(finished, 150)
```

Call `celebrate()` when the target is caught.

## 🔔 Optional sound

Some computers can also make a simple bell:

```python
def beep():
    try:
        screen.getcanvas().bell()
    except Exception:
        pass
```

If you hear nothing, that is fine. The game must still work without sound.

## 🧠 Why optional?

Computers and classrooms are different. Sound may be muted or unavailable, and some players prefer silence. Important game information should also be visible.

## 🔧 Change

Try a longer flash or another colour.

## ⭐ Challenge

Make two different signals: one for catching the target and one for being caught by the monster. Can a player understand both with sound turned off?

## 🐞 Bug hunt

If the flash never ends, check the `ontimer()` call. If sound does not work, continue without it — sound is a bonus.

## 🧠 What you learned

- games can give immediate feedback
- visual signals also work without sound
- sound can be an optional bonus

**Next mission:** Put everything together into a complete mini-game! 🎮
