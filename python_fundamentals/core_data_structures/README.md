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

## Task 1: Safe access to a list element

File: `element_at.py`

The function `element_at(my_list, idx)` returns the element at index `idx`.
It returns `None` if the index is negative or greater than or equal to
`len(my_list)`. The original list is not modified. No modules are imported.

### Validation

- Checked style with `python3 -m pycodestyle element_at.py`.
- Tested valid indices `0`, `3`, and `4` in a five-element list.
- Tested invalid indices `-1`, `5`, and `15`: returned `None`.
- Tested an empty list at index `0`: returned `None`.
- Confirmed that the original list remains unchanged.
- Added user execution permission to `element_at.py`.

## Task 2: Replace an element in a list

File: `replace_in_list.py`

The function `replace_in_list(my_list, idx, element)` replaces the element
at a valid index and returns the original list object.
If `idx` is negative or greater than or equal to `len(my_list)`, the list
is returned unchanged. No modules are imported.

### Validation

- Checked style with `python3 -m pycodestyle replace_in_list.py`.
- Tested replacement at indices `0`, `3`, and `4` in a five-element list.
- Tested invalid indices `-1`, `5`, and `15`: the list remained unchanged.
- Tested an empty list at index `0`: it remained empty.
- Confirmed that every call returns the original list object using `is`.
- Added user execution permission to `replace_in_list.py`.
