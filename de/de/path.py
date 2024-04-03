"""Functions that extract the filename and function name."""
# using getattr()

import inspect, os, sys
from pathlib import Path
from typing import Callable, Tuple
from de import generate, enumerations

# how to get the parameters - is that something that I need to do
# not sure what the output should be
def path(filename: Path, funcname: str) -> Tuple[Callable, enumerations.FunctionParamTypes]:
    """Return the function call with the appropriate parameters"""

    # ensure given file is Python file
    if not str(filename).endswith(".py"):
        raise ValueError("Given file is not a Python file.")
    if not filename.exists():
        raise ValueError("Given file does not exist.")
    # test to see if it is a sorting funtion
    if "sort" not in funcname:
        print("Warning: 'sort' not found in function name - are you sure this is a sorting algorithm?")

    the_function = get_function_as_callable(filename, funcname)

    # find what the parameter types are
    parameters = get_parameters(the_function)

    # let's consider two cases:
    #   functions with args of f(array)
    #   functions with args of f(array, length)
    if len(parameters) == 1:
        function_param_type = enumerations.FunctionParamTypes.just_array
    elif len(parameters) == 2:
        function_param_type = enumerations.FunctionParamTypes.array_and_length

    # return the function call with the description of its parameters
    return (the_function, function_param_type)

def get_function_as_callable(filename: Path, funcname: str) -> Callable:
    """Extract the specified function from the specified python file."""

    # execute code of given file
    exec(open(filename).read())

    # try to avoid calling a function that doesn't exist
    # checking different aspects about the file and the function

    # to check if funcname is a function
    # there is also the ismethod() function which might fit more appropriately
    if inspect.isfunction(filename.funcname) is False:
        print("Are you sure you passed in the correct function?")
    
    # to check if there are functions in the module
    if inspect.getmembers(filename) is None:
        print("Are you sure this function exists in this file?")

    else:
    # should we just put filename instead of sys.modules?
        return getattr(sys.modules[__name__], funcname)

# https://stackoverflow.com/questions/23228664/how-to-check-which-arguments-a-function-method-takes
# hasattr() - checks if a file has the function

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

def get_parameters(function_call):
    """Find the parameters of a function."""
    # another method to get a look at the args and kwds is inspect.signature
    parameters = inspect.getargspec(function_call).args
    return parameters

# simple path creation function
def str_path_creation(filename: str, funcname: str):
    """Return the function call with the appropriate parameters"""
    # convert strings -> function path
    # it is returning type string but in a path format
    complete_path_string = filename + "/" + funcname
    return os.path.normpath(complete_path_string)