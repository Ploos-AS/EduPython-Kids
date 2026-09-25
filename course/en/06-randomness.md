# 06 – Randomness and dice

## 🎯 Mission

Make a digital die that gives a random result each time you run the program.

## 💻 Code

```python
import random

roll = random.randint(1, 6)
print("You rolled", roll)
```

`random` is a module with tools for randomness.

`random.randint(1, 6)` chooses a random integer from 1 through 6.

## 🔧 Change

Make a 20-sided die by changing 6 to 20.

## 🤔 Think

Can you know exactly which number the program will choose before you run it?

You cannot know the exact roll, but you know which values are possible.

Why can randomness be useful in games?

## ⭐ Challenge

Roll two dice and print their sum.

```python
import random

a = random.randint(1, 6)
b = random.randint(1, 6)

print("The dice:", a, "and", b)
print("Sum:", a + b)
```

Extra challenge: print "Double!" when both dice show the same number.

## 🐞 Bug hunt

```python
import random
roll = random.randint(1, 6
print(roll)
```

Find the error before you run the program.

## 🧠 What you learned

- `import` can bring more Python tools into a program.
- `random` gives us tools for randomness.
- `randint()` can choose a random integer in a range.
- A random result can be unknown even when all possible results are known.
