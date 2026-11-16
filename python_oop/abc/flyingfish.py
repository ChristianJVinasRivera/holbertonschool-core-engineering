#!/usr/bin/env python3
"""Demonstrate multiple inheritance with a flying fish."""


class Fish:
    """Represent an animal that swims and lives in water."""

    def swim(self):
        """Print how a fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represent an animal that flies and lives in the sky."""

    def fly(self):
        """Print how a bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Combine fish and bird behavior, overriding their shared methods."""

    def swim(self):
        """Print how the flying fish swims."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print how the flying fish flies."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print the flying fish's combined habitat."""
        print("The flying fish lives both in water and the sky!")
