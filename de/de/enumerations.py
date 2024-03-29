"""Configuration of the benchmarking tool and its approaches."""

from enum import Enum


class ListType(str, Enum):
    """Define the type of the lists subject to benchmarking."""

    singlylinked = "singlylinked"
    doublylinked = "doublylinked"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class ListData(str, Enum):
    """Define the data that will be stored in the list nodes of the lists."""

    ints = "ints"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class BenchmarkStrategy(str, Enum):
    """Define the benchmarking strategy."""

    double = "double"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class BenchmarkOperation(str, Enum):
    """Define the benchmarking operation."""

    removefirst = "removefirst"
    removelast = "removelast"
    add = "add"
    iadd = "iadd"

    def __str__(self):
        """Define a default string representation."""
        return self.value
