# Python - Core Data Structures

## Task 0: Print a list of integers

File: `print_list_integer.py`

The function `print_list_integer(my_list=[])` prints each integer in a list
on its own line. It uses a `for` loop and explicit `{:d}` integer formatting.
No modules are imported. An empty list or a call without arguments prints
nothing.

### Validation

- Checked style with `python3 -m pycodestyle print_list_integer.py`.
- Tested `[1, 2, 3, 4, 5]`: one integer per line.
- Tested `[]` and the default argument: no output.
- Tested `[-3, 0, 98]`: negative, zero, and positive integers.
- Added user execution permission to `print_list_integer.py`.
