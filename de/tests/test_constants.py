"""Test suite for the constants module."""

from de import constants
from pathlib import Path
from de import enumerations


constant = constants.Constants(-(1 << 32),
+(1 << 32),
float(-(1 << 32)),
float(+(1 << 32)),
 1,
 100,
[
        (Path("tests/benchmarkable_functions.py"), "bubble_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "bubble_sort_str", enumerations.ListData.strings),
        (Path("tests/benchmarkable_functions.py"), "selection_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "insertion_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "heap_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "quick_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "merge_sort", enumerations.ListData.ints),
    ])

def test_min_int_value():
    assert constant.Min_Int_Value == -(1 << 32)

def test_max_int_value():
    assert constant.Max_Int_Value == +(1 << 32)

def test_min_float_value():
    assert constant.Min_Float_Value == float(-(1 << 32))

def test_max_float_value():
    assert constant.Max_Float_Value == float(+(1 << 32))

def test_min_string_size():
    assert constant.Min_String_Size == 1

def test_max_string_size():
    assert constant.Max_String_Size == 100


