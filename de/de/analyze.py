"""Analyze the doubling results and estimates O(n) based on benchmarks results."""
from de import benchmark, enumerations

# instead of this, something that takes in the benchmark list of tuples
# extracts the time values(stored in index 2 of each tuple) and the size
# index 1, and uses that to ascertain if the time complexity of the input function.

def func_constant_time(lst):
    """Computing a constant time complexity"""
    # for example; iterate through the given list. if in a doubling experiment,
    # the size should double for each run. If the run time is less than twice the
    # one before it, accounting with some constant for variability, then it may be constant.
    pass

def func_linear_time(lst):
    """Computing a linear time complexity"""
    for item in lst:
        pass

def func_logarithmic_time(lst):
    """Computing a logarithmic time complexity"""
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
