"""Configuration of the doubling experiment tool."""

from enum import Enum


class ListData(str, Enum):
    """Define the data that will be stored in the list nodes of the lists."""

    ints = "ints"

    def __str__(self):
        """Define a default string representation."""
        return self.value
