# Python - Everything is object 🐍

In Python, **everything** you interact with is an **object** — whether it’s a **number**, a **list**, a **string**, or even a **function**. Writing reliable code and avoiding surprises requires a solid understanding of how Python handles these objects, how variables refer to them, the key differences between mutable and immutable objects, and how arguments are passed to functions.

## Understanding Types and Object Identity in Python

In Python, every object you create has two fundamental properties: its **type** and its **unique identity**.

- The **type** tells you what kind of data the object represents (for example, integer, list, or string).

- The **identity** is a unique value assigned to the object during its lifetime, distinguishing it from all other objects.

You can easily check these properties using Python’s built-in functions `type()` and `id()`.

```
number = 42
print(type(number))  # Shows the object's data type: <class 'int'>
print(id(number))    # Displays a unique identifier for the object (usually its memory address)
```

The value returned by `id()` remains constant for that object until it is destroyed. This identity helps Python keep track of each individual object in memory.
