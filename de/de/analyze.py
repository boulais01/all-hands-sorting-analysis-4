"""Analyze benchmark data."""

from de import enumerations


def estimate_time_complexity(average_doubling_ratio: float) -> enumerations.TimeComplexity:
    """Estimate the time complexity given the average doubling ratio."""
    average_doubling_ratio_rounded = round(average_doubling_ratio)
    # 2 <= r <= 2.25 is linear
    if average_doubling_ratio >= 1.75 and average_doubling_ratio <= 2.25:
        return enumerations.TimeComplexity.linear
    # 2.25 < r < 2.75 is linearithmic
    elif average_doubling_ratio > 2.25 and average_doubling_ratio < 2.75:
        return enumerations.TimeComplexity.linearithmic
    # 3.5 <= r < 4.5 is quadratic
    elif average_doubling_ratio_rounded == 4:
        return enumerations.TimeComplexity.quadratic
    # r < 1.75 is logarithmic
    elif average_doubling_ratio < 1.75:
        return enumerations.TimeComplexity.logarithmic
    # r approximately 1 is constant
    elif average_doubling_ratio_rounded == 1:
        return enumerations.TimeComplexity.constant
    # indicate that it does not match any of our predefined values
    else:
        return enumerations.TimeComplexity.notsure
