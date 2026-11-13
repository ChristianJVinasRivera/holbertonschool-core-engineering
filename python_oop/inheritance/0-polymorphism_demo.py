#!/usr/bin/python3
"""Demonstrate inheritance, method overriding, and polymorphism."""


class Animal:
    """Represent an animal with a generic sound."""

    def speak(self):
        """Return the generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog that inherits from Animal."""

    def speak(self):
        """Return the dog's sound."""
        return "Woof"


class Cat(Animal):
    """Represent a cat that inherits from Animal."""

    def speak(self):
        """Return the cat's sound."""
        return "Meow"


if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()
    print(animal.speak())
    print(dog.speak())
    print(cat.speak())

    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    dog = Dog()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
