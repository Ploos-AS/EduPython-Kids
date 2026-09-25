# 11 – Make your own commands with functions

## 🎯 Mission

Make a named task that the program can use several times.

A named task like this is called a **function**.

## 💻 Code

```python
def greet():
    print("Hello!")
    print("Welcome to the game.")

greet()
greet()
```

`def` creates the function. The code inside runs when we **call** the function.

## 🎁 Send information in

```python
def greet(name):
    print("Hello", name + "!")

greet("Ada")
greet("Sam")
```

`name` is a **parameter**. It lets the same function work with different values.

## 🔙 Get a value back

```python
def double(number):
    return number * 2

answer = double(7)
print(answer)
```

`return` sends a value back from the function.

`print()` and `return` do different jobs: `print()` displays something, while a returned value can be stored or used later.

## 🔧 Change

Create a function called `triple(number)`.

## 🤔 Think

What happens here?

```python
result = double(5) + double(2)
print(result)
```

Why can we keep calculating with the values from `double()`?

## ⭐ Challenge

Create a function `roll_die()` that returns a random number from 1 to 6.

## 🐞 Bug hunt

```python
def greet()
    print("Hello!")

greet()
```

What is missing from the first line?

## 🧠 What you learned

- A function groups code under a name.
- A function can be called several times.
- Parameters make functions flexible.
- `return` sends a value back.
- `print()` and `return` have different jobs.
