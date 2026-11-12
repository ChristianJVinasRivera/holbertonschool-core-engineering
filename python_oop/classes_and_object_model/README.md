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
