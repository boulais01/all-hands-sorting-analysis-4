"""Functions that extract the filename and function name."""
# using getattr()

import inspect
import simon's generator module

# how to get the parameters - is that somethign that I need to do
def path(filename: path, funcname: string) -> ??:
    import filename
    if filename.hasattr() is False:
        print("This file does not seem to have that function.")
    try:
        filename.getattr(sort, )
    catch:
        print("Are you sure this is a sorting algorithm?")
    
    parameters = get_parameters(filename, funcname)
    if parameters == type int:
        call int generator function
    if parameters == type str:
        call str generator function
    if parameters == type float:
        call float generator function

# https://stackoverflow.com/questions/23228664/how-to-check-which-arguments-a-function-method-takes
# hasattr() - checks if a file has the function

# def function(funcname):

def get_parameters(filename, funcname):
    import filename
    function_call = filename.funcname()
    parameters = inspect.getargspec(function_call).args
    return parameters
