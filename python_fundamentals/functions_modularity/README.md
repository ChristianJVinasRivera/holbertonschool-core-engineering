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

## Task 2: Print Last Digit

File: `print_last_digit.py`

Defines `print_last_digit(number)`, which prints the last digit of an
integer and returns that digit as an integer from 0 to 9.

The function uses `abs(number) % 10` so negative inputs also produce a
nonnegative digit. It prints the digit using string formatting, without
extra text or a trailing newline.

### Validation

- Passed the Python syntax check and `pycodestyle` 2.7.0.
- Tested positive, negative, and zero inputs: 98, -1024, and 0.
- Verified that the returned values are 8, 4, and 0, respectively.

### Example

```python
from print_last_digit import print_last_digit

last = print_last_digit(-1024)  # Prints 4 and returns 4
```

## Task 3: Power

File: `pow.py`

Defines `pow(a, b)`, which returns `a` raised to the integer power `b`.

The function starts with 1 and repeatedly multiplies by `a` using a loop.
For a zero exponent, it returns 1. For a negative exponent, it returns
the reciprocal of the product. It does not use the `**` operator or imports.
A zero base with a negative exponent raises `ZeroDivisionError`.

### Validation

- Passed Python syntax and `pycodestyle` 2.7.0 checks.
- Passed five tests covering positive, zero, and negative exponents,
  a negative base, and a zero base with a positive exponent.

### Example

```python
from pow import pow

pow(2, 4)    # Returns 16
pow(5, 0)    # Returns 1
pow(2, -3)   # Returns 0.125
pow(-2, 3)   # Returns -8
pow(0, 3)    # Returns 0
```
