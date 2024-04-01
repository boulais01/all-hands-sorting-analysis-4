"""Test suite for the generate module."""

from de import generate, enumerations


def test_generate_lists_zero():
    """Ensure the function can handle an input of zero."""
    assert len(generate.generate_lists(enumerations.ListData.ints, 1, 0)) == 0
    assert len(generate.generate_lists(enumerations.ListData.floats, 1, 0)) == 0
    assert len(generate.generate_lists(enumerations.ListData.strings, 1, 0)) == 0

def test_generate_lists():
    """Ensure the function does not fail with basic input."""
    generated_ints = generate.generate_lists(enumerations.ListData.ints, 1, 5)
    assert len(generated_ints) == 5
    assert [len(the_list) for the_list in generated_ints] == [1 * (2 ** i) for i in range(5)]
    generated_floats = generate.generate_lists(enumerations.ListData.floats, 1, 5)
    assert len(generated_floats) == 5
    assert [len(the_list) for the_list in generated_floats] == [1 * (2 ** i) for i in range(5)]
    generated_strings = generate.generate_lists(enumerations.ListData.strings, 1, 5)
    assert len(generated_strings) == 5
    assert [len(the_list) for the_list in generated_strings] == [1 * (2 ** i) for i in range(5)]

def test_generate_list_with_ints_zero():
    """Ensure the function can handle an input of zero."""
    assert len(generate.generate_list_with_ints(0)) == 0

def test_generate_list_with_floats_zero():
    """Ensure the function can handle an input of zero."""
    assert len(generate.generate_list_with_floats(0)) == 0

def test_generate_list_with_strings_zero():
    """Ensure the function can handle an input of zero."""
    assert len(generate.generate_list_with_strings(0)) == 0

def test_generate_list_with_ints_nonuniform():
    """Ensure the function has a non-uniform output."""
    generated = generate.generate_list_with_ints(5)
    # assert that the generated results have more than one unique value
    assert len(set(generated)) > 1

def test_generate_list_with_floats_nonuniform():
    """Ensure the function has a non-uniform output."""
    generated = generate.generate_list_with_floats(5)
    # assert that the generated results have more than one unique value
    assert len(set(generated)) > 1

def test_generate_list_with_strings_nonuniform():
    """Ensure the function has a non-uniform output."""
    generated = generate.generate_list_with_strings(5)
    # assert that the generated results have more than one unique value
    assert len(set(generated)) > 1
