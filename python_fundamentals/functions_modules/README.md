# Python - Functions and Modules

## Task 4: Script Execution and Import Behavior

### Files

- `simple_add.py`: defines `add(a, b)`, which returns the sum of its arguments.
- `test_import.py`: imports `simple_add` to observe import-time behavior.

### Before the execution guard

The call `print(add(3, 5))` was at the top level of `simple_add.py`.
Running either file printed `8`, because importing a module executes its
unprotected top-level statements on the first import in that process.

### After the execution guard

The print call is protected by:

```python
if __name__ == "__main__":
    print(add(3, 5))
```

- `python3 simple_add.py` prints `8` followed by a newline.
- `python3 test_import.py` produces no output.

When run directly, `simple_add.py` has `__name__ == "__main__"`.
When imported, its `__name__` is `"simple_add"`, so the guarded call is skipped.
The function remains available as `simple_add.add`.

### Validation

Both files passed the following style check:

```bash
python3 -m pycodestyle simple_add.py test_import.py
```

Direct execution and import were tested before and after adding the guard.
