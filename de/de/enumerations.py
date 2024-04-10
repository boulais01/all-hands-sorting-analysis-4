"""Configuration of the doubling experiment tool."""

from enum import Enum


class ListData(str, Enum):
    """Define the data that will be stored in the list nodes of the lists."""

    ints = "ints"
    strings = "strings"
    floats = "floats"

    def __str__(self):
        """Define a default string representation."""
        return self.value

class FunctionParamTypes(str, Enum):
    """Define the data that will be stored in the list nodes of the lists."""

    # some sorting algorithms need to know the length
    # of the input array; let's account for that
    just_array = "just_array"
    array_and_length = "array_and_length"

    def __str__(self):
        """Define a default string representation."""
        return self.value

class TimeComplexity(str, Enum):
    """Define valid time complexities for sorting operations."""
    constant = "1"
    linear = "n"
    quadratic = "n²"
    logarithmic = "log(n)"
    linearithmic = "n log(n)"
    notsure = "not sure"

    def __str__(self):
        """Define a default string representation."""
        return self.value
