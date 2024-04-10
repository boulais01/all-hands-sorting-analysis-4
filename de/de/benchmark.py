"""Run a benchmark on a function provided by a list-based structure."""

import time
from typing import List, Tuple, Callable

from de import enumerations, generate
from de.constants import constants

# ruff: noqa: PLR0913

def benchmark(
    listdata: enumerations.ListData,
    functype: enumerations.FunctionParamTypes,
    funcname: Callable,
    startsize: int,
    runs: int,
) -> List[Tuple[int, int, float]]:
    """Benchmark the data."""
    # initialize list and size, setup list generation
    times_list = []
    size = startsize
    generate_func = getattr(generate, "generate_list_with_" + listdata)
    list_one = generate_func(size)
    if functype is enumerations.FunctionParamTypes.just_array:
        for i in range(runs):
            if i > 0:
                size += size
                list_one += generate_func(size)
            start = time.perf_counter()
            funcname(list_one)
            stop = time.perf_counter()
            times_list.append((i + 1, size, stop - start))
    else:
        for i in range(runs):
            if i > 0:
                size += size
                list_one += generate_func(size)
            # Order passed in must be array, size
            start = time.perf_counter()
            funcname(list_one, size)
            stop = time.perf_counter()
            times_list.append((i + 1, size, stop - start))
    # return list of tuples (run_num, size, run_time)
    return times_list


def find_minimum(
    times_list: List[Tuple[int, int, float]],
) -> List[Tuple[int, int, float]]:
    """Find quickest run in list."""
    # return all data for a row in a tuple
    min_time = times_list[0]
    for i in times_list:
        if (
            i[2]
            < min_time[2]
        ):
            min_time = i
    return min_time


def find_maximum(
    times_list: List[Tuple[int, int, float]],
) -> List[Tuple[int, int, float]]:
    """Find slowest run in list."""
    # return all data for a row in a tuple
    max_time = times_list[0]
    for i in times_list:
        if (
            i[2]
            > max_time[2]
        ):
            max_time = i
    return max_time


def compute_average(times_list: List[Tuple[int, int, float]]) -> float:
    """Compute average runtime."""
    list_sum = 0
    for i in times_list:
        list_sum += i[2]
    return list_sum / len(times_list)


def compute_average_doubling_ratio(times_list: List[Tuple[int, int, float]]) -> float:
    times = [item[2] for item in times_list]
    # iterate through times, calculating doubling ratios between runs
    doubling_ratios = [times[i+1] / times[i] for i in range(len(times) - 1)]
    # calculate average doubling ratio
    return sum(doubling_ratios) / len(doubling_ratios)
