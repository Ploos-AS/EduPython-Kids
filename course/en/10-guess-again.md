# 10 – Guess the number with more attempts

## 🎯 Mission

Upgrade the guessing game so the player can keep trying until the answer is correct.

## 💻 Code

```python
import random

secret = random.randint(1, 20)
guess = None
attempts = 0

while guess != secret:
    guess = int(input("Guess a number from 1 to 20: "))
    attempts = attempts + 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct! You used", attempts, "attempts.")
```

Now `while` and `if` work together: the loop decides whether the game continues, while the conditions give hints.

The variables `secret`, `guess` and `attempts` describe what is happening in the game right now. We can call this **game state**.

## 🔧 Change

Change the range to 1–50 or 1–100.

## 🤔 Think

Why do we set `guess = None` before the loop?

We need a starting value before Python can test `guess != secret`. Here, `None` means that we do not have a guess yet.

## ⭐ Challenge

Give the player at most five attempts. Can you make the game tell the player when the attempts are used up?

## 🌟 Extra

Let the player choose a difficulty before the game starts.

## 🐞 Bug hunt

If the game stops too early or never stops, temporarily print `guess`, `secret` and `attempts`.

What do the values tell you?

## 🧠 What you learned

- `while` can drive a game round until a condition changes.
- A counter can track the number of attempts.
- Several variables can describe game state together.
- Temporary `print()` lines can help you find a bug.
