# 08 – Mini-game: Guess the number

## 🎯 Mission

Combine what you have learned to make a small game.

The program chooses a secret number from 1 to 10. You try to guess it.

## 💻 First version

```python
import random

secret = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

if guess == secret:
    print("Correct! 🎉")
else:
    print("Not this time.")
    print("The number was", secret)
```

You are already combining variables, `input()`, `int()`, randomness and `if`.

## 🔧 Make the game smarter

```python
if guess == secret:
    print("Correct! 🎉")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
```

`elif` means roughly "otherwise, if ...". Only one of these three paths is chosen.

## 🤔 Think

What do you think we need to let the player guess again and again until the answer is correct?

We have not learned that tool yet. In the next lesson you will meet `while`.

## ⭐ Challenge

Change the range to 1–20. Make your own winning message.

Extra: give the player points when the answer is correct.

## 🐞 Bug hunt

What is the difference between these?

```python
guess = secret
guess == secret
```

The first gives `guess` a value. The second is a condition asking whether the values are equal.

## 🧠 What you learned

- Earlier Python tools can be combined into a game.
- `elif` adds another condition between `if` and `else`.
- `<` and `>` compare numbers.
- Some problems show us why we need a new programming tool.
