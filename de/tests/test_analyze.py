"""Test analyze module."""

from de import analyze, enumerations


def test_analyze():
    """Ensure analyze works for various average doubling ratios."""
    assert analyze.estimate_time_complexity(1.01) == enumerations.TimeComplexity.constant
    assert analyze.estimate_time_complexity(1.96) == enumerations.TimeComplexity.linear
    assert analyze.estimate_time_complexity(3.99) == enumerations.TimeComplexity.quadratic
    assert analyze.estimate_time_complexity(1.54) == enumerations.TimeComplexity.logarithmic
    assert analyze.estimate_time_complexity(2.54) == enumerations.TimeComplexity.linearithmic
    assert analyze.estimate_time_complexity(100) == enumerations.TimeComplexity.notsure
