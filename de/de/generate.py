"""Populate lists of a given data type with a specified size."""

import random
import string

from typing import Union, List
from de import enumerations
from de.constants import constants


def generate_lists(listdata: enumerations.ListData, startsize: int, n_lists: int) -> List[Union[str, float, int]]:
    """Generate lists according to a doubling strategy starting at `startsize`."""
    if startsize <= 0:
        raise ValueError("Start size must be greater than zero.")
    current_size = startsize
    # create lists where results are stored
    lists = [generate_list(listdata, startsize * (2 ** i)) for i in range(n_lists)]
    return lists


def generate_list(listdata: enumerations.ListData, size: int) -> List[Union[str, float, int]]:
    """
    Generate a list of the given datatype and size.

    listdata: data type of the list
    size: size of the list
    results: reference to list where results are stored. This list must not be reassigned to
    returns: formatted string
    """
    if listdata == enumerations.ListData.ints:
        return generate_list_with_ints(size)
    elif listdata == enumerations.ListData.floats:
        return generate_list_with_floats(size)
    elif listdata == enumerations.ListData.strings:
        return generate_list_with_strings(size)


def generate_list_with_ints(size: int) -> List[int]:
    """Generate a list with random integers."""
    return [random.randrange(constants.Min_Int_Value, constants.Max_Int_Value) for _ in range(size)]


def generate_list_with_floats(size: float) -> List[float]:
    """Generate a list with random floats."""
    # translate value from the range [0.0, 1.0] into the range [Min_Float_Value, Max_Float_Value]
    normalize = lambda x: x * (constants.Max_Float_Value - constants.Min_Float_Value) + constants.Min_Float_Value
    # return random samples of floats
    return [normalize(random.random()) for _ in range(size)]


def generate_list_with_strings(size: str) -> List[str]:
    """Generate a list with random strings."""
    # create function for randomly getting string size
    string_size = lambda: random.randint(constants.Min_String_Size, constants.Max_String_Size)
    # create function for creating a random string
    get_string = lambda: "".join([random.choice(string.printable) for _ in range(string_size())])
    return [get_string() for _ in range(size)]
