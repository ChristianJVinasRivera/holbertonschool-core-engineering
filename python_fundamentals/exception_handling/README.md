# Python - Exception Handling

## Task 0: Safe list printing

File: `safe_print_list.py`

Prototype: `def safe_print_list(my_list=[], x=0):`

Prints up to `x` list elements on one line, followed by a newline.
Returns the actual number of elements printed.

### How it works

- Iterates over the requested indexes using `range(x)`.
- Uses `try` to access and print each element without extra spaces.
- Increments a counter after each successful print.
- Catches `IndexError` and stops when the list has no more elements.
- Prints a final newline and returns the counter.
- Uses no imports and does not use `len()`.

### Local validation

- Syntax check: `python3 -m py_compile safe_print_list.py`
- Style check: `python3 -m pycodestyle safe_print_list.py`
- Six external tests passed, checking output and return values:
  partial list, request beyond the list, empty list, zero elements,
  mixed types, and a negative request.

## Task 1: Safe integer printing

File: `safe_print_integer.py`

Prototype: `def safe_print_integer(value):`

Prints an integer using `"{:d}".format(value)`, followed by a newline.
Returns `True` when printing succeeds.
Returns `False` when the value cannot be formatted as an integer.

### How it works

- Uses `try` to format and print the value.
- Catches `ValueError` and `TypeError` for unsupported values.
- Uses no imports and does not use `type()`.
- Style check: `python3 -m pycodestyle safe_print_integer.py`
- Seven external tests passed, checking output and return values:
  positive integer, negative integer, zero, string, float, None, and list.

## Task 2: Safe list printing with type handling

File: `safe_print_list_integers.py`

Prototype: `def safe_print_list_integers(my_list=[], x=0):`

Examines the first `x` positions and prints only integers without spaces.
Prints a final newline and returns the number of integers printed.
If a requested index is outside the list, `IndexError` propagates
before the final newline and return statement are reached.

### How it works

- Iterates over the requested positions using `range(x)`.
- Uses `"{:d}".format()` inside `try` to print each integer.
- Increments the counter only after a successful print.
- Catches `ValueError` and `TypeError` to skip unsupported values.
- Allows `IndexError` to propagate when `x` exceeds the list length.

### Local validation

- Syntax check: `python3 -m py_compile safe_print_list_integers.py`
- Style check: `python3 -m pycodestyle safe_print_list_integers.py`
- Eight external tests passed, checking output, counts, mixed types,
  empty lists, negative requests, zero, negative integers, and IndexError.

## Task 3: Divide two integers safely

File: `safe_print_division.py`

Prototype: `def safe_print_division(a, b):`

Divides two integers and returns the result, or None on failure.
Always prints `Inside result: <result>` followed by a newline.

### How it works

- Initializes `result` to None before attempting the division.
- Performs `a / b` inside a `try` block.
- Catches `ZeroDivisionError` and `TypeError`, keeping the result as None.
- Uses `finally` to print the result whether division succeeds or fails.
- Returns the result after the `finally` block.

### Local validation

- Syntax check: `python3 -m py_compile safe_print_division.py`
- Style check: `python3 -m pycodestyle safe_print_division.py`
- Nine external tests passed, checking return values and exact printed output:
  normal division, division by zero, zero numerator, negative numerator,
  negative denominator, fractional result, zero divided by zero,
  string input, and None input.
