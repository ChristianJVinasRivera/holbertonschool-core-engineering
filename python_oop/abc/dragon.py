#!/usr/bin/env python3
"""Combine swimming and flying behaviors with mixins."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
