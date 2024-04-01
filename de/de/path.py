"""Functions that extract the filename and function name."""
# using getattr()

import inspect
<<<<<<< HEAD
import generator
from typing import Path
=======
from de import generate
>>>>>>> 21303b7fc74636f61e2e1b101bb40deafc2eb040

# how to get the parameters - is that somethign that I need to do
# not sure what the output should be
def path(filename: Path, funcname: str) -> :
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
        values = generator.int_generator()
    if type(parameters) == str:
        values = generator.str_generator()
    if type(parameters) == float:
        values = generator.float_generator()

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
