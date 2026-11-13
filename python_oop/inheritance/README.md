# Python Inheritance and Polymorphism

## Task 0: Introduction to Inheritance and Polymorphism

File: `0-polymorphism_demo.py`

### Objective

Explore inheritance, method overriding, polymorphism, and class relationships.

### Classes

- `Animal.speak()` returns `Some sound`.
- `Dog` inherits from `Animal` and overrides `speak()` to return `Woof`.
- `Cat` inherits from `Animal` and overrides `speak()` to return `Meow`.

Each subclass responds differently to the same `speak()` method call.
The program demonstrates individual objects and a list of dogs and cats.
It also uses `isinstance()` to check an object's class and `issubclass()`
to check inheritance between classes.

### Run

```bash
python3 0-polymorphism_demo.py
```

### Expected output

```text
Some sound
Woof
Meow
Woof
Meow
Woof
True
True
True
```

The final three values confirm that a dog is both a `Dog` and an `Animal`,
and that `Dog` is a subclass of `Animal`.

### Local validation

```bash
python3 -m py_compile 0-polymorphism_demo.py
python3 -m pycodestyle 0-polymorphism_demo.py
```
