# Classes and Object Model

## Task 1: My First Square

### File
`0-square.py`

### Objective
Define an empty class named `Square` that represents a square.

### Implementation
- Document the module and the class with docstrings.
- Use `pass` to indicate that the class has no operations yet.
- Do not define attributes or methods in this version.

### Usage
```python
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
```

### Expected output
```text
<class '0-square.Square'>
{}
```

Each call to `Square()` creates an instance. Its instance dictionary is
empty because no instance attributes have been assigned.

## Task 2: Square with Size

### File
`1-square.py`

### Objective
Define a `Square` class with a private instance attribute named `__size`.
The size must be provided when creating an instance.

### Implementation
- Use `__init__(self, size)` to initialize each square.
- Store the given value in `self.__size`.
- Do not validate the type or value of `size` in this version.
- Double leading underscores trigger name mangling: `__size` becomes
  `_Square__size`, avoiding accidental access through `size` or `__size`.
  This is not a security boundary.

### Usage
```python
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

for name in ('size', '__size'):
    try:
        print(getattr(my_square, name))
    except AttributeError as error:
        print(error)
```

### Expected output
```text
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
```

## Task 3: Size Validation

### File
`2-square.py`

### Objective
Validate the size before storing it in the private `__size` attribute.

### Implementation
- Use `__init__(self, size=0)` so the default size is zero.
- Check the type with `isinstance(size, int)`.
- Raise `TypeError("size must be an integer")` for non-integer values.
- Raise `ValueError("size must be >= 0")` for negative integers.
- Store the size only after both checks pass.

### Usage
```python
Square = __import__('2-square').Square

print(Square().__dict__)
print(Square(3).__dict__)

for size in ("3", -89):
    try:
        Square(size)
    except (TypeError, ValueError) as error:
        print(error)
```

### Expected output
```text
{'_Square__size': 0}
{'_Square__size': 3}
size must be an integer
size must be >= 0
```
