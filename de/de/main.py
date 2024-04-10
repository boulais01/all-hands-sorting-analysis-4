"""Conduct experiments to evaluate performance of list concatenation."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console

from de import enumerations, benchmark, path
from pathlib import Path

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()

@cli.command()
def main(
    filename: Path = typer.Option(
        Path,
    ),
    funcname: str = typer.Option(
        str,
    ),
    listdata: enumerations.ListData = typer.Option(
        enumerations.ListData.ints,
    ),
    startsize: int = typer.Option(100),
    runs: int = typer.Option(5),
):
    """Evaluate the performance of a given sorting algorithm."""
    # display details about the efficiency of a sorting algorithm
    console.print(
        "\n[bold red]Benchmarking Tool for Sorting Algorithms[/bold red]\n"
    )
    console.print(f"Filepath: {filename}")
    console.print(f"Function: {funcname}")
    console.print(f"Data to sort: {listdata}")
    console.print(f"Number of runs: {runs}\n")
    # extract function from the given file
    func, param_types = path.path(filename, funcname)
    # perform the benchmarking operation
    benchmark_data = benchmark.benchmark(
        listdata, param_types, func, startsize, runs
    )
    console.print()
    # display the results concerning the minimum execution time
    # --> minimum value
    minimum_results = benchmark.find_minimum(benchmark_data)
    console.print(
        f"Minimum execution time: {minimum_results[2]:.10f} seconds",
        f"for run {minimum_results[0]} with size {minimum_results[1]}",
    )
    # --> maximum value
    maximum_results = benchmark.find_maximum(benchmark_data)
    console.print(
        f"Maximum execution time: {maximum_results[2]:.10f} seconds",
        f"for run {maximum_results[0]} with size {maximum_results[1]}",
    )
    # --> average value
    console.print()
    average_value = benchmark.compute_average(benchmark_data)
    console.print(
        f"Average execution time: {average_value:.10f} seconds"
        f" across runs 1 through {len(benchmark_data)}"
    )
    # --> average doubling ratio
    console.print()
    average_value = benchmark.compute_average_doubling_ratio(benchmark_data)
    console.print(
        f"Average doubling ratio: {average_value:.10f}"
        f" across runs 1 through {len(benchmark_data)}"
    )
