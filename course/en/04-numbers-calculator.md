# 04 – Numbers and mini calculator

## 🎯 Mission
Use Python as a calculator and make a program that calculates with numbers typed by the user.

## 💻 Code
First try direct arithmetic:

```python
print(3 + 4)
print(10 - 2)
print(6 * 3)
```

Now make it interactive:

```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
```

`input()` gives us text. `int()` converts suitable text such as `"12"` into an integer.

## ▶ Run
Try several pairs of whole numbers, including 0.

## 🔧 Change
Add subtraction and multiplication:

```python
print("Difference:", a - b)
print("Product:", a * b)
```

## 🤔 Think
What do you predict for `"2" + "3"`? What about `2 + 3`? Test both.

## 🐞 Bug hunt
Type a word when the program asks for a number. Read the last part of the error message. What clue does it give you?

You do not need to fix this with advanced error handling yet.

## ⭐ Challenge
Make a tiny score calculator that asks for two fictional game scores and prints their total and difference.

[Extra exercises](../../exercises/en/04-numbers-calculator.md)

## 🧠 What you learned
- Python can calculate with numbers.
- `input()` returns text.
- `int()` converts suitable text to an integer.
- Errors can tell us what kind of value caused a problem.

## Next mission
Next the program will make choices with `if`.
