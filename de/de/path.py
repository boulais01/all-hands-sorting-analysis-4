"""Functions that extract the filename and function name."""
# using getattr()

import inspect
import os
# from typing import Path
from de import generate

# Path vs Callable?

# https://stackoverflow.com/questions/23228664/how-to-check-which-arguments-a-function-method-takes
# hasattr() - checks if a file has the function

# not sure what the output should be
def path(filename: str, funcname: str):
    """Return the function call with the appropriate parameters"""
    # convert strings -> function path
    # it is returning type string but in a path format
    complete_path_string = filename + "/" + funcname
    return os.path.normpath(complete_path_string)

def call_function_w_parameters(function_call: Path, size: int):
    """Return the full function call."""
    parameters = get_parameters(function_call)
    if type(parameters) == int:
        values = generate.generate_list_with_ints(size)
    if type(parameters) == str:
        values = generate.generate_list_with_strings(size)
    if type(parameters) == float:
        values = generate.generate_list_with_floats(size)
    # return the function call with the parameters passed in
    return function_call(values)

def get_parameters(function_call: Path):
    """Find the parameters of a function."""
    parameters = inspect.getargspec(function_call).args
    return parameters

# print(type(path("hi", "func")))