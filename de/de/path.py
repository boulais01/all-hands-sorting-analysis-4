"""Functions that extract the filename and function name."""
# using getattr()

import inspect
from typing import Path
from de import generate

# how to get the parameters - is that somethign that I need to do
# not sure what the output should be
def path(filename: Path, funcname: str, size: int):
    """Return the function call with the appropriate parameters"""
    # test to see if it is a sorting funtion
    # try:
    #     if sort in funcname:
    # catch:
    #     print("Are you sure this is a sorting algorithm?")
    
    # import the file
    import filename
    # could try and catch the bellow code
    # if filename.funcname() is False:
    #     print("This file does not seem to have that function.")

    # find what the parameter types are
    parameters = get_parameters(filename, funcname)
    if type(parameters) == int:
        values = generate.generate_list_with_ints(size)
    if type(parameters) == str:
        values = generate.generate_list_with_strings(size)
    if type(parameters) == float:
        values = generate.generate_list_with_floats(size)

    # return the function call with the parameters passed in
    return filename.funcname(values)

# https://stackoverflow.com/questions/23228664/how-to-check-which-arguments-a-function-method-takes
# hasattr() - checks if a file has the function

# def function(funcname):

def get_parameters(filename, funcname):
    import filename
    function_call = filename.funcname()
    parameters = inspect.getargspec(function_call).args
    return parameters
