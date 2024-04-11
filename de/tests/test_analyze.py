"""Test analyze module."""

from de import analyze, enumerations, path, benchmark
from pathlib import Path


def test_analyze():
    """Ensure analyze works for various average doubling ratios."""
    assert analyze.estimate_time_complexity(1.01) == enumerations.TimeComplexity.constant
    assert analyze.estimate_time_complexity(1.96) == enumerations.TimeComplexity.linear
    assert analyze.estimate_time_complexity(3.99) == enumerations.TimeComplexity.quadratic
    assert analyze.estimate_time_complexity(1.54) == enumerations.TimeComplexity.logarithmic
    assert analyze.estimate_time_complexity(2.54) == enumerations.TimeComplexity.linearithmic
    assert analyze.estimate_time_complexity(100) == enumerations.TimeComplexity.notsure

def test_analyze_all_sorting_algorithms():
    """Ensure all of the sample sorting algorithms are analyzed correctly."""
    def evaluate(funcname) -> enumerations.TimeComplexity:
        func, param_types = path.path(Path("tests/benchmarkable_functions.py"), funcname)
        # perform the benchmarking operation
        benchmark_data = benchmark.benchmark(
            enumerations.ListData.ints, param_types, func, startsize=100, runs=5
        )
        average_doubling_ratio = benchmark.compute_average_doubling_ratio(benchmark_data)
        estimated_time_complexity = analyze.estimate_time_complexity(average_doubling_ratio)
        return estimated_time_complexity
    sorting_algos = [
        ("bubble_sort", enumerations.TimeComplexity.quadratic),
        ("selection_sort", enumerations.TimeComplexity.quadratic),
        ("insertion_sort", enumerations.TimeComplexity.quadratic),
        ("heap_sort", enumerations.TimeComplexity.linearithmic),
        ("quick_sort", enumerations.TimeComplexity.quadratic),
        ("merge_sort", enumerations.TimeComplexity.linearithmic),
    ]
    for algo in sorting_algos:
        assert evaluate(algo[0]) == algo[1]
