#!/usr/bin/env python3
"""Define an abstract animal and concrete dog and cat classes."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Specify the interface shared by animal subclasses."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Represent a dog that barks."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Represent a cat that meows."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
