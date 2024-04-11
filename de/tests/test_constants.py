"""Test suite for the constants module."""

from de import constants

def test_min_int_value():
    assert constants.Min_Int_Value == -(1 << 32)

def test_max_int_value():
    assert constants.Max_Int_Value == +(1 << 32)

def test_min_float_value():
    assert constants.Min_Float_Value == float(-(1 << 32))

def test_max_float_value():
    assert constants.Max_Float_Value == float(+(1 << 32))

def test_min_string_size():
    assert constants.Min_String_Size == 1

def test_max_string_size():
    assert constants.Max_String_Size == 100


