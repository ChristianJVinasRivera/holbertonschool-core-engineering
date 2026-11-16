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

## Task 1: Shapes, Interfaces, and Duck Typing

`shapes.py` defines a common interface and two concrete shapes:

- `Shape` inherits from `ABC` and declares abstract `area()` and
  `perimeter()` methods. It cannot be instantiated directly.
- `Circle(radius)` calculates area as `math.pi * radius ** 2` and
  perimeter as `2 * math.pi * radius`.
- `Rectangle(width, height)` calculates area as `width * height` and
  perimeter as `2 * (width + height)`.
- `shape_info(shape)` prints area and perimeter by calling the object's
  methods directly. It uses duck typing, not `isinstance` checks, so an
  unrelated class with both methods also works.

### Example

```python
from shapes import Circle, Rectangle, shape_info

shape_info(Circle(radius=5))
shape_info(Rectangle(width=4, height=7))
```

Expected output:

```text
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

### Local validation

```bash
python3 -m py_compile shapes.py
python3 -m pycodestyle shapes.py
```

## Task 2: The Enigmatic FlyingFish - Exploring Multiple Inheritance

`flyingfish.py` demonstrates multiple inheritance and method overriding:

- `Fish` defines `swim()` and `habitat()`.
- `Bird` defines `fly()` and `habitat()`.
- `FlyingFish(Fish, Bird)` inherits from both classes and overrides all three
  methods with behavior specific to a flying fish.
- `FlyingFish.__mro__` (or `FlyingFish.mro()`) shows the method resolution
  order: `FlyingFish`, `Fish`, `Bird`, then `object`. Python searches in that
  order and uses the first matching method. Here the overrides in `FlyingFish`
  take precedence over the parent implementations.

### Example

```python
from flyingfish import Fish, Bird, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
```

Expected output:

```text
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

### Local validation

```bash
python3 -m py_compile flyingfish.py
python3 -m pycodestyle flyingfish.py
```
