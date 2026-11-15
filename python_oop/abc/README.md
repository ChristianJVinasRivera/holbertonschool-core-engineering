# Abstract Classes and Interfaces

## Task 0: Abstract Animal Class and its Subclasses

File: `animals.py`

### Objective

Define an abstract `Animal` base class with an abstract `sound()` method,
then implement the contract in `Dog` and `Cat`.

### Classes

- `Animal` inherits from `abc.ABC` and declares `sound()` with
  `@abstractmethod`.
- `Dog.sound()` returns `"Bark"`.
- `Cat.sound()` returns `"Meow"`.
- `Animal` cannot be instantiated until its abstract method is implemented;
  attempting to instantiate it raises `TypeError`.

### Example

```python
from animals import Animal, Dog, Cat

print(Dog().sound())
print(Cat().sound())
try:
    Animal()
except TypeError as error:
    print(error)
```

Expected output begins:

```text
Bark
Meow
Can't instantiate abstract class Animal with abstract method sound
```

### Local validation

```bash
python3 -m py_compile animals.py
python3 -m pycodestyle animals.py
```
