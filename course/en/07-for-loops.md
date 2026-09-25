# 07 – Repeat with for

## 🎯 Mission

Make Python do a job several times without writing the same code again.

## 💻 Code

```python
for number in range(5):
    print("Round", number)
```

A **loop** repeats code. A `for` loop is useful when we know how many repetitions we want.

The code belonging to the loop is indented.

## 🔧 Change

What happens if you change `5` to `10`?

Also try:

```python
for number in range(1, 11):
    print(number)
```

## 🎲 Five dice rolls

```python
import random

for round_number in range(5):
    roll = random.randint(1, 6)
    print("Roll", round_number + 1, "was", roll)
```

## 🤔 Think

What do you think the first value of `round_number` is?

`range(5)` gives 0, 1, 2, 3 and 4. That is why we use `round_number + 1` when we want to display "Roll 1" through "Roll 5".

## ⭐ Challenge

Make a program that rolls a die 10 times and counts how many sixes you get.

## 🐞 Bug hunt

```python
for i in range(5):
print(i)
```

Python cares about indentation. Can you repair the program?

## 🧠 What you learned

- A loop repeats code.
- `for` is useful for a known number of repetitions or values.
- `range()` creates a sequence of numbers for a loop.
- Python often starts counting at 0.
- Code inside the loop needs correct indentation.
