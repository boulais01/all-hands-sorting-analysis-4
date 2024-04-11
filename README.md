# all-hands-sorting-analysis-4

The work for Team 4 of the All-Hands session, to implement a benchmarking framework. 

## What the Tool is Used For

This tool is used to run a doubling experiment on an input sorting algorithm

## How to Use the Tool

This tool is run by navigating into the first `de` folder, running a `poetry
install`. With this setup complete, one runs a command similar to the example
one below, replacing the example inputs with the actual.

```
poetry run de --filename path/to/sortingfile.py --funcname sortingfunction --listdata ints --startsize 100 --runs 5
```

The `filename` and `funcname` parameters are required, as they have no default
value. `listdata` will default to `ints`, though the other options are `strings`
and `floats`. The `startsize` and `runs` parameters have default values shown
above, and are for noting what the initial size of the list to start will be and
how many doublings should be completed, respectively.

A sample output of running the program:

Command: `poetry run de --filename tests/benchmarkable_functions.py --funcname bubble_sort`

Output:

```text
Benchmarking Tool for Sorting Algorithms

Filepath: tests/benchmarkable_functions.py
Function: bubble_sort
Data to sort: ints
Number of runs: 5


Minimum execution time: 0.0002972880 seconds for run 1 with size 100
Maximum execution time: 0.0773113760 seconds for run 5 with size 1600

Average execution time: 0.0204783342 seconds across runs 1 through 5

Average doubling ratio: 4.0301311823 across runs 1 through 5

Estimated time complexity: O(n²)
```

In the case of the sample output, the `--filename` argument specifies the file path of the Python script containing the sorting algorithm to be benchmarked. The `--funcname` argument specifies the name of the specific sorting function within the file that is being benchmarked, which in this case is `bubble_sort`. Because arguments for both `--listdata`, `--startsize` and `--runs` were not provided, they are given the default values as defined which in this case are `ints`, `100` and `5` respectively

A sample command showcasing changing these default values: `poetry run de --filename tests/benchmarkable_functions.py --funcname quick_sort --startsize 50 --runs 10`

When discussing how the various files interact to make the benchmarking process succeed, it first leverages the `enumerations` file to define enums related to list data types and time complexity, enabling the specification of data types for sorting. Secondly, the `benchmark` file provides functions for benchmarking algorithms, including computing minimum and maximum execution times, average execution times, and estimating time complexity. Furthermore, the `path` module is employed to extract the specified sorting function from a given file. The `analyze` file utilizes `enumerations` to estimate the time complexity of sorting algorithms based on the average doubling ratio computed during benchmarking. Additionally, constants from the `constants` file aid in determining default behaviors when no arguments are supplied.

Running `de` without any arguments will benchmark six sample sorting algorithms
with their estimated runtime complexities. These are not always guaranteed to be
correct!

```sh
$ de

Benchmarking Tool for Sorting Algorithms

Estimated time complexity for tests/benchmarkable_functions.py -> bubble_sort: O(n²)
Estimated time complexity for tests/benchmarkable_functions.py -> bubble_sort_str: O(n²)
Estimated time complexity for tests/benchmarkable_functions.py -> selection_sort: O(n²)
Estimated time complexity for tests/benchmarkable_functions.py -> insertion_sort: O(n²)
Estimated time complexity for tests/benchmarkable_functions.py -> heap_sort: O(n)
Estimated time complexity for tests/benchmarkable_functions.py -> quick_sort: O(n log(n))
Estimated time complexity for tests/benchmarkable_functions.py -> merge_sort: O(n log(n))
```

### Available Options

```
Usage: de [OPTIONS]

Evaluate the performance of a given sorting algorithm.

--filename                  PATH                   [default: (dynamic)]
--funcname                  TEXT                   [default: (dynamic)]
--listdata                  [ints|strings|floats]  [default: ints]
--startsize                 INTEGER                [default: 100]
--runs                      INTEGER                [default: 5]
```

## Guidelines for Project Construction

It operates in the following fashion.

- Accept as input one or more Python source code files that contain one or more
  functions that perform sorting. For the purposes of creating your benchmarking
  framework you can assume that all sorting algorithms will implement the same
  function signature that you carefully document in a README and your tool's
  comments.
- Accept as input the fully-qualified name of a sorting function that should be
  subject to benchmarking.
- Accept as input the description of an input generation procedure that can
  automatically generate data suitable for the purposes of conducting a doubling
  experiment to evaluate the performance of the sorting algorithm.
- Automatically extract the sorting function from the provided Python source
  code file(s) and then reflectively invoke the function to sort data that was
  automatically generated.
- In a series of automatically completed benchmarking rounds, the tool should
  conduct a doubling experiment by which it generates data sets of increasing
  size and then uses them to evaluate the performance of the sorting algorithm.
- The tool should produce diagnostic data that shows the execution time for each
  round of the doubling experiment, a computed version of the doubling ratio
  based on the collected data, and a statement about the likely worst-case time
  complexity suggested by the doubling ratio.
- Your tool must be implemented with the Python programming language and use the
  Poetry system for managing dependencies and packaging.
- Your tool must provide a command-line interface implemented through the use of
  Typer and offer command-line arguments that fully support its configuration.
- Your tool can leverage Python source code that you previously implemented as a
  part of a course project as long as you carefully document the source of any
  Python code segments.
 
## Experimental Work

<!--

- Write and publish on the course web site a blog post that explains
  - (a) how you designed and implemented your benchmarking framework,
  - (b) the sorting algorithm functions that you chose to use in your doubling
    experiments,
  - (c) the runtime results from your experimental study with the benchmarking
    framework that you implemented and
  - (d) the running time results from an analytical evaluation that you
    conducted.
- Your blog post should clearly articulate
  - (a) whether or not the experimental and analytical results for your function
    are in alignment with each other,
  - (b) what is most likely to be the realistic runtime and true running time of
    a sorting function, and
  - (c) why you judge that your function has this runtime and running time,
  - (d) which sorting algorithm function from among those selected by your team
    members is the fastest, and
  - (e) why this specific implementation proved to be the fastest among all of
    the sorting algorithms.
- Present your findings to the entire class during the following week of the
  academic semester during the follow-on algorithm all-hands session.

-->
