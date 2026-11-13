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

## Task 1: Base Geometry

File: `base_geometry.py`

### Objective

Define shared behavior for geometric shapes and validate positive integers.

### Methods

- `area()` raises `Exception("area() is not implemented")` because each
  concrete shape must provide its own calculation.
- `integer_validator(name, value)` accepts only integers greater than zero.
  Boolean values are rejected.
- Invalid types raise `TypeError("<name> must be an integer")`.
- Zero and negative integers raise
  `ValueError("<name> must be greater than 0")`.

### Example

```python
BaseGeometry = __import__('base_geometry').BaseGeometry
geometry = BaseGeometry()
geometry.integer_validator('width', 3)
try:
    geometry.area()
except Exception as error:
    print(error)  # area() is not implemented
```

### Local validation

```bash
python3 -m py_compile base_geometry.py
python3 -m pycodestyle base_geometry.py
```
