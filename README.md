# all-hands-sorting-analysis-4

The work for Team 4 of the All-Hands session, to implement a benchmarking framework. 

## What the Tool is Used For

This tool is used to run a doubling experiment on an input sorting algorithm

## How to Use the Tool

This tool is run by navigating into the first `de` folder, running a `poetry install`. 
With this setup complete, one runs a command similar to the example one below, replacing the
example inputs with the actual.

`poetry run de --filename path/to/sortingfile.py --funcname sortingfunction --listdata ints`

The `filename` and `funcname` parameters are required, as they have no default value.
`listdata` will default to `ints`, though the other options are `strings` and `floats`.

A sample output of running the program:

Command: ``

Output:

```

```

## Guidelines for Project Construction

It operates in the following fashion.
- Accept as input one or more Python source code files that contain one or more functions that perform sorting. For the purposes of creating your benchmarking framework you can assume that all sorting algorithms will implement the same function signature that you carefully document in a README and your tool's comments.
- Accept as input the fully-qualified name of a sorting function that should be subject to benchmarking.
- Accept as input the description of an input generation procedure that can automatically generate data suitable for the purposes of conducting a doubling experiment to evaluate the performance of the sorting algorithm.
- Automatically extract the sorting function from the provided Python source code file(s) and then reflectively invoke the function to sort data that was automatically generated.
- In a series of automatically completed benchmarking rounds, the tool should conduct a doubling experiment by which it generates data sets of increasing size and then uses them to evaluate the performance of the sorting algorithm.
- The tool should produce diagnostic data that shows the execution time for each round of the doubling experiment, a computed version of the doubling ratio based on the collected data, and a statement about the likely worst-case time complexity suggested by the doubling ratio.
- Your tool must be implemented with the Python programming language and use the Poetry system for managing dependencies and packaging.
- Your tool must provide a command-line interface implemented through the use of Typer and offer command-line arguments that fully support its configuration.
- Your tool can leverage Python source code that you previously implemented as a part of a course project as long as you carefully document the source of any Python code segments.
 
