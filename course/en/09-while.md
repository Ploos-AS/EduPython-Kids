# 09 – Keep going with while

## 🎯 Mission

Make a program continue until something specific happens.

## 💻 Code

```python
answer = ""

while answer != "yes":
    answer = input("Are you ready? ")

print("Let's begin!")
```

A `while` loop means roughly "as long as". It continues while its condition is true.

Here it continues while `answer` is **not** equal to `"yes"`.

## 🔧 Change

Make a program that asks for a fictional code word until the correct word is entered.

Never use a real password that you use somewhere else.

## 🔢 Count with while

```python
number = 1

while number <= 5:
    print(number)
    number = number + 1
```

The value changes each round. Eventually the condition becomes false and the loop stops.

## 🤔 Think

What happens if we forget `number = number + 1`?

The value that should make the condition false never changes, so the loop can continue forever.

In a terminal you can usually stop such a program with Ctrl+C.

## ⭐ Challenge

Make a countdown from 10 to 1 and print "START!" at the end.

## 🐞 Bug hunt

```python
number = 1

while number <= 5:
    print(number)
```

Why does the program not stop? Which value must change?

## 🧠 What you learned

- `while` repeats code while a condition is true.
- Something usually needs to change so the loop can stop.
- A loop that never stops is often called an infinite loop.
- `for` often fits known repetitions; `while` fits waiting for something to happen.
