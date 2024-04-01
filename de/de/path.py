"""Functions that extract the filename and function name."""
# using getattr()

import inspect
from pathlib import Path
from typing import Callable, Tuple
from de import generate, enumerations

# how to get the parameters - is that somethign that I need to do
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
    parameters = get_parameters(filename, funcname)

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
    import sys
    # TODO: this doesn't work well yet...
    # execute code of given file
    exec(open(filename).read())
    return getattr(sys.modules[__name__], funcname)

# https://stackoverflow.com/questions/23228664/how-to-check-which-arguments-a-function-method-takes
# hasattr() - checks if a file has the function

# def function(funcname):

def get_parameters(filename: str, funcname: str):
    import filename
    function_call = filename.funcname()
    parameters = inspect.getargspec(function_call).args
    return parameters
