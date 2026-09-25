# 13 – Collect things in lists

## 🎯 Mission

Make a backpack that can contain several things.

## 💻 Code

```python
backpack = ["map", "flashlight", "apple"]

print(backpack)
print("First item:", backpack[0])
```

A **list** collects several values in one place.

Each position has a number called an **index**. Python starts list indexes at 0.

In this list:

- `backpack[0]` → `"map"`
- `backpack[1]` → `"flashlight"`
- `backpack[2]` → `"apple"`

## ➕ Add something

```python
backpack.append("key")
print(backpack)
```

`.append()` adds a new value at the end of the list.

## 🔁 Look at everything

```python
for item in backpack:
    print("You have:", item)
```

The `for` loop visits one item at a time. We do not need to know how long the list is.

## 🔧 Change

Make your own list with five items for a fictional adventurer.

## 🤔 Think

What do you think `backpack[1]` gives you?

What happens if you try `backpack[99]`?

## ⭐ Challenge

Make a small game inventory. Let the player find a treasure and add it with `.append()`.

## 🐞 Bug hunt

```python
animals = ["dog", "cat"]
print(animals[2])
```

The list has two items. Which indexes exist?

Read the error message. Can it help you?

## 🧠 What you learned

- A list can collect several values.
- Each position has an index.
- Python starts list indexes at 0.
- `.append()` adds a value.
- A `for` loop can visit the values in a list.
