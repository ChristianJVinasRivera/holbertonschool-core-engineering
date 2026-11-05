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

## Task 3: Print a matrix of integers

File: `print_matrix_integer.py`

The function `print_matrix_integer(matrix=[[]])` prints each row on its
own line using nested loops and `{:d}` integer formatting.
Values in a row are separated by one space, with no trailing spaces.
The matrix is not modified. No modules are imported by the function file.

### Validation

- Checked style with `python3 -m pycodestyle print_matrix_integer.py`.
- Tested a 3-by-3 matrix and verified the exact output.
- Tested negative integers, zero, and single-column rows.
- Tested `[]`: no output.
- Tested `[[]]` and the default argument: one newline.
- Confirmed that the matrix remains unchanged and the function returns `None`.
- Added user execution permission to `print_matrix_integer.py`.

## Task 4: Tuple addition

File: `add_tuple.py`

The function `add_tuple(tuple_a=(), tuple_b=())` returns a tuple of two
integers by adding the corresponding first and second values of each input.
Missing values are treated as zero, and values beyond the first two are ignored.
Tuple concatenation adds padding zeros, and slicing keeps the first two values.
The original tuples remain unchanged. No modules are imported.

### Validation

- Checked style with `python3 -m pycodestyle add_tuple.py`.
- Tested two complete tuples and verified position-by-position addition.
- Tested empty tuples, single-element tuples, and default arguments.
- Tested extra elements: only the first two values were used.
- Tested negative integers and zero.
- Confirmed that each result is a tuple containing exactly two values.
- Confirmed that the input tuples remain unchanged.
- Added user execution permission to `add_tuple.py`.

## Task 5: Common elements in two sets

File: `common_elements.py`

The function `common_elements(set_1, set_2)` returns a new set containing
only elements present in both input sets. It uses the `&` intersection operator.
The original sets remain unchanged. No modules are imported.

### Validation

- Checked style with `python3 -m pycodestyle common_elements.py`.
- Tested the task example: the only common element is `"C"`.
- Tested disjoint sets: the result is an empty set.
- Tested one empty input and two empty inputs.
- Tested identical sets and sets containing negative integers and zero.
- Confirmed that each result is a new set, distinct from both inputs.
- Confirmed that both input sets remain unchanged.
- Added user execution permission to `common_elements.py`.
