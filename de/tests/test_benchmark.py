"""Tests for the benchmark module."""

from de import benchmark, enumerations, path

from pathlib import Path

time_check_list = [(1, 100, 2.0000089765), (2, 200, 4.0032089765), (3, 400, 8.0076589765), (4, 800, 16.540089765)]

def test_benchmark_ints():
    """Test that the benchmark functions works as expected with integer input."""
    func, functype = path.path(Path("tests/benchmarkable_functions.py"), "bubble_sort")
    times_list = benchmark.benchmark(enumerations.ListData.ints, functype, func, 100, 5)
    assert isinstance(times_list, list)
    assert isinstance(times_list[0], tuple)
    assert len(times_list) == 5

def test_benchmark_floats():
    """Test that the benchmark functions works as expected with integer input."""
    func, functype = path.path(Path("tests/benchmarkable_functions.py"), "bubble_sort")
    times_list = benchmark.benchmark(enumerations.ListData.floats, functype, func, 100, 5)
    assert isinstance(times_list, list)
    assert isinstance(times_list[0], tuple)
    assert len(times_list) == 5

def test_benchmark_strs():
    """Test that the benchmark functions works as expected with integer input."""
    func, functype = path.path(Path("tests/benchmarkable_functions.py"), "bubble_sort_str")
    times_list = benchmark.benchmark(enumerations.ListData.strings, functype, func, 100, 5)
    assert isinstance(times_list, list)
    assert isinstance(times_list[0], tuple)
    assert len(times_list) == 5

def test_find_minimum():
    """Check that the find minimum function returns the fastest run time."""
    min_find = benchmark.find_minimum(time_check_list)
    assert isinstance(min_find, tuple)
    assert min_find[2] == 2.0000089765

def test_find_maximum():
    """Check that the find maximum function returns the slowest run time."""
    max_find = benchmark.find_maximum(time_check_list)
    assert isinstance(max_find, tuple)
    assert max_find[2] == 16.540089765

def test_compute_average():
    """Check that the compute average function returns the average of the times."""
    average = benchmark.compute_average(time_check_list)
    assert average == 7.637741673625