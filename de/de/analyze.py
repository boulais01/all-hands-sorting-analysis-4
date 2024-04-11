"""Analyze benchmark data."""

from de import enumerations


def estimate_time_complexity(average_doubling_ratio: float) -> enumerations.TimeComplexity:
    """Estimate the time complexity given the average doubling ratio."""
    average_doubling_ratio_rounded = round(average_doubling_ratio)
    if average_doubling_ratio >= 1.75 and average_doubling_ratio <= 2.25:
        return enumerations.TimeComplexity.linear
    elif average_doubling_ratio > 2.25 and average_doubling_ratio < 3.75:
        return enumerations.TimeComplexity.linearithmic
    elif average_doubling_ratio >= 3.75 and average_doubling_ratio_rounded <= 4.25:
        return enumerations.TimeComplexity.quadratic
    elif average_doubling_ratio > 1.25 and average_doubling_ratio < 1.75:
        return enumerations.TimeComplexity.logarithmic
    elif average_doubling_ratio_rounded == 1:
        return enumerations.TimeComplexity.constant
    # indicate that it does not match any of our predefined values
    else:
        return enumerations.TimeComplexity.notsure
