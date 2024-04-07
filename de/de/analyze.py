"""Analyze the doubling results and estimates O(n) based on benchmarks results."""
from de import benchmark, enumerations

def func_constant_time(lst):
    """Computing a constant time complexity"""
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
