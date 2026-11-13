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

## Task 2: Rectangle

`1-rectangle.py` defines `Rectangle`, a subclass of `BaseGeometry`.
Its constructor requires `width` and `height`, validates both using the
inherited `integer_validator`, and stores them as private attributes.
Both dimensions must be integers strictly greater than zero; booleans
are rejected. No public getters or setters are defined.

```python
Rectangle = __import__('1-rectangle').Rectangle
rectangle = Rectangle(3, 5)
# rectangle.width raises AttributeError: dimensions are private.
# rectangle.area() raises Exception('area() is not implemented').
```

Invalid types raise `TypeError` with `<name> must be an integer`.
Zero or negative integers raise `ValueError` with
`<name> must be greater than 0`. Validation is inherited, not duplicated.

### Local checks

```bash
python3 -m py_compile 1-rectangle.py
python3 -m pycodestyle 1-rectangle.py
```

## Task 3: Full Rectangle

File: `2-rectangle.py`

`Rectangle` extends `BaseGeometry` and validates positive integer dimensions
with the inherited `integer_validator`. Width and height remain private,
without getters or setters.

- `area()` returns width multiplied by height.
- `__str__()` returns `[Rectangle] <width>/<height>`.
- `print(rectangle)` uses that string representation automatically.

```python
Rectangle = __import__('2-rectangle').Rectangle
rectangle = Rectangle(3, 5)
print(rectangle)         # [Rectangle] 3/5
print(rectangle.area())  # 15
```

Invalid types raise `TypeError` with `<name> must be an integer`.
Zero or negative integers raise `ValueError` with
`<name> must be greater than 0`. Validation is inherited, not duplicated.

### Local checks

```bash
python3 -m py_compile 2-rectangle.py
python3 -m pycodestyle 2-rectangle.py
```

## Task 4: Square #1

`1-square.py` defines `Square`, a subclass of `Rectangle`.

- `Square(size)` validates size with the inherited `integer_validator`.
- Size must be an integer greater than zero; booleans are rejected.
- The side length is stored privately as `__size`, without a getter or setter.
- The parent constructor initializes equal width and height.
- `area()` returns the side length squared.
- The inherited string representation keeps the `[Rectangle]` label.

```python
Square = __import__('1-square').Square
square = Square(13)
print(square)         # [Rectangle] 13/13
print(square.area())  # 169
```

Invalid types raise `TypeError` with `size must be an integer`.
Zero or negative sizes raise `ValueError` with
`size must be greater than 0`.
