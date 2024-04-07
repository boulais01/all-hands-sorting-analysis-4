"""Analyze the doubling results and estimates O(n) based on benchmarks results."""
from de import benchmark, enumerations

from typing import List, Tuple, Callable
import time

# Assumption 1: Constant time complexity
def func_constant_time(lst):
    # Assuming this function operates in constant time
    pass

# Assumption 2: Linear time complexity
def func_linear_time(lst):
    # Assuming this function iterates over the entire list once
    for item in lst:
        pass

# Assumption 3: Logarithmic time complexity
def func_logarithmic_time(lst):
    # Assuming this function operates in logarithmic time
    length = len(lst)
    i = 1
    while i < length:
        i *= 2


# Scenario 1: Constant time complexity
print("Scenario 1: Constant Time Complexity")
times_constant = benchmark.benchmark(
    "data",
    enumerations.FunctionParamTypes.just_array,
    func_constant_time,
    10,
    5
)
print("Time Measurements:", times_constant)

# Scenario 2: Linear time complexity
print("\nScenario 2: Linear Time Complexity")
times_linear = benchmark.benchmark(
    "data",
    enumerations.FunctionParamTypes.just_array,
    func_linear_time,
    10,
    5
)
print("Time Measurements:", times_linear)

# Scenario 3: Logarithmic time complexity
print("\nScenario 3: Logarithmic Time Complexity")
times_logarithmic = benchmark.benchmark(
    "data",
    enumerations.FunctionParamTypes.just_array,
    func_logarithmic_time,
    10,
    5
)
print("Time Measurements:", times_logarithmic)
