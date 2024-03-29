"""Run a benchmark on a function provided by a list-based structure."""

from listmutator import approach, generate
from typing import Tuple, List
from copy import deepcopy
import timeit

# ruff: noqa: PLR0913

# DONE: Add the complete implementation of benchmarking functions
# that support the creation of output like that shown in the README.md file
def benchmark(
    listtype: approach.ListType,
    listdata: approach.ListData,
    strategy: approach.BenchmarkStrategy,
    operation: approach.BenchmarkOperation,
    startsize: int,
    runs: int
) -> List[Tuple[int, int, float]]:
    """Benchmark the given operation on the given list."""
    benchmark_data: List[Tuple[int, int, float]] = []
    lists_to_use = generate.generate_lists_with_strategy(listtype, listdata, strategy, runs, startsize)
    run_index = 1
    for list_to_use in lists_to_use:
        list_to_use_copy = deepcopy(list_to_use)
        list_to_use_size = len(list_to_use)
        if operation == approach.BenchmarkOperation.removefirst:
            input("about to create removefirst...")
            print(list_to_use.display())
            print(len(list_to_use))
            lambda_func = lambda: list_to_use.removefirst()
        elif operation == approach.BenchmarkOperation.removelast:
            lambda_func = lambda: list_to_use.removelast()
        elif operation == approach.BenchmarkOperation.add:
            lambda_func = lambda: list_to_use + list_to_use
        elif operation == approach.BenchmarkOperation.iadd:
            lambda_func = lambda: list_to_use.__iadd__(list_to_use_copy)

        # test the lambda_func 5 times
        delta_t = timeit.timeit(lambda_func, number=5) / 5

        benchmark_data.append((run_index, list_to_use_size, delta_t))
        run_index += 1
    return benchmark_data


def find_minimum(benchmark_data: List[Tuple[int, int, float]]) -> Tuple[int, int, float]:
    """Find the minimum of the provided benchmark data."""
    return min(benchmark_data, key=lambda x: x[2])


def find_maximum(benchmark_data: List[Tuple[int, int, float]]) -> Tuple[int, int, float]:
    """Find the maximum of the provided benchmark data."""
    return max(benchmark_data, key=lambda x: x[2])


def find_average(benchmark_data: List[Tuple[int, int, float]]) -> float:
    """Find the average of the provided benchmark data."""
    delta_ts = map(lambda x: x[2], benchmark_data)
    return sum(delta_ts) / len(delta_ts)


def find_doubling_ratios(benchmark_data: List[Tuple[int, int, float]]) -> List[float]:
    """Return a list of doubling ratios for a sequence of runs."""
    doubling_ratios: List[float] = []
    for i in range(len(benchmark_data) - 1):
        # append the ratio of their delta_ts
        doubling_ratios.append(benchmark_data[i + 1][2] / benchmark_data[i][2])
    return doubling_ratios
