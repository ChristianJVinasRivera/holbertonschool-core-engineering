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
