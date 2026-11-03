# Python - Functions and Modularity

This project practices defining functions, returning values, and organizing
reusable Python code into modules.

## Task 0: islower

File: `islower.py`

Defines `islower(c)`, which returns `True` when `c` is an ASCII lowercase
letter (`a` through `z`) and `False` otherwise.

The function uses `ord(c)` to check whether the character code is between
97 and 122, inclusive. It returns a boolean without using the built-in
`str.islower()` method.

### Validation

- Passed the local `pycodestyle` check.
- Tested all 128 ASCII characters, checking both classification and boolean
  return values.

### Example

```python
from islower import islower

print(islower('a'))  # True
print(islower('A'))  # False
print(islower('3'))  # False
```

## Task 1: To Uppercase

File: `uppercase.py`

Defines `uppercase(str)`, which prints a string in uppercase followed by
one newline. The function has no explicit return value.

Each ASCII lowercase letter is converted using `ord()` and `chr()` by
subtracting 32 from its character code. Other characters are preserved.
The function does not use `str.upper()`.

### Validation

- Passed the local `pycodestyle` check.
- Tested mixed-case text, digits, punctuation, and an empty string.

### Example

```python
from uppercase import uppercase

uppercase("Holberton")  # HOLBERTON
uppercase("aZ 09!?")    # AZ 09!?
uppercase("")           # Prints one newline
```
