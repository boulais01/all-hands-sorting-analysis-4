"""Test path module."""

from de import path, enumerations
from pathlib import Path


def test_path_bubble_sort_float():
    """Test the path method on a sample file."""
    filename = Path("tests/benchmarkable_functions.py")
    funcname = "bubble_sort"
    arr = [7.0, 5.1, 2.1, 1.19, 3.122, 4.5, 6.75]
    arr_sorted = sorted(arr)
    # ensure the return type of the path method is as expected
    assert callable(path.path(filename, funcname)[0])
    assert path.path(filename, funcname)[1] == enumerations.FunctionParamTypes.array_and_length
    # run sorting algorithm on test arr
    path.path(filename, funcname)[0](arr, len(arr))
    assert arr == arr_sorted

def test_path_bubble_sort_int():
    """Test the path method on a sample file."""
    filename = Path("tests/benchmarkable_functions.py")
    funcname = "bubble_sort"
    arr = [7, 5, 2, 1, 3, 4, 6]
    arr_sorted = sorted(arr)
    # ensure the return type of the path method is as expected
    assert callable(path.path(filename, funcname)[0])
    assert path.path(filename, funcname)[1] == enumerations.FunctionParamTypes.array_and_length
    # run sorting algorithm on test arr
    path.path(filename, funcname)[0](arr, len(arr))
    assert arr == arr_sorted

def test_path_bubble_sort_str():
    """Test the path method on a sample file."""
    filename = Path("tests/benchmarkable_functions.py")
    funcname = "bubble_sort_str"
    arr = ["apples", "oranges", "berries", "pineapples"]
    arr_sorted = sorted(arr)
    # ensure the return type of the path method is as expected
    assert callable(path.path(filename, funcname)[0])
    assert path.path(filename, funcname)[1] == enumerations.FunctionParamTypes.array_and_length
    # run sorting algorithm on test arr
    path.path(filename, funcname)[0](arr, len(arr))
    assert arr == arr_sorted
