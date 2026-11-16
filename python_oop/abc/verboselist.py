#!/usr/bin/env python3
"""A list that announces additions and removals."""


class VerboseList(list):
    """Print a notification when items are added or removed."""

    def append(self, item):
        """Append an item, then announce the addition."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend from an iterable, then announce the number added."""
        previous_length = len(self)
        super().extend(iterable)
        print(f"Extended the list with {len(self) - previous_length} items.")

    def remove(self, item):
        """Announce the item, then remove its first occurrence."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Announce and return the item removed at index."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
