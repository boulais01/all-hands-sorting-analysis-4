"""Conduct experiments to evaluate performance of list concatenation."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console

from de import enumerations, benchmark, path, analyze
from de.constants import constants
from pathlib import Path
from typing import Union

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()

@cli.command()
def main(
    filename: Union[Path, None] = typer.Option(
        None,
    ),
    funcname: Union[str, None] = typer.Option(
        None,
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
    # default behavior if no arguments are supplied
    if filename is None and funcname is None:
        for func_info in constants.Benchmarkable_Functions_And_Data_Types:
            run(filename=func_info[0], funcname=func_info[1], listdata=func_info[2], startsize=startsize, runs=runs, just_print_time_complexity=True)
    else:
        run(filename=filename, funcname=funcname, listdata=listdata, startsize=startsize, runs=runs)

def run(filename: Path, funcname: str, listdata: enumerations.ListData, startsize: int, runs: int, just_print_time_complexity: bool = False):
    """Benchmark and analyze the given function."""
    # extract function from the given file
    func, param_types = path.path(filename, funcname)
    # perform the benchmarking operation
    benchmark_data = benchmark.benchmark(
        listdata, param_types, func, startsize, runs
    )
    # display the results concerning the minimum execution time

    # --> minimum value
    minimum_results = benchmark.find_minimum(benchmark_data)

    # --> maximum value
    maximum_results = benchmark.find_maximum(benchmark_data)

    # --> average value
    average_value = benchmark.compute_average(benchmark_data)

    # --> average doubling ratio
    average_doubling_ratio = benchmark.compute_average_doubling_ratio(benchmark_data)

    # --> estimated time complexity
    estimated_time_complexity = analyze.estimate_time_complexity(average_doubling_ratio)

    if not just_print_time_complexity:
        console.print(
            f"Filepath: {filename}",
            f"Function: {funcname}",
            f"Data to sort: {listdata}",
            f"Number of runs: {runs}\n",
            f"",
            f"Minimum execution time: {minimum_results[2]:.10f} seconds",
            f"for run {minimum_results[0]} with size {minimum_results[1]}",
            f"Maximum execution time: {maximum_results[2]:.10f} seconds",
            f"for run {maximum_results[0]} with size {maximum_results[1]}",
            f"",
            f"Average execution time: {average_value:.10f} seconds",
            f" across runs 1 through {len(benchmark_data)}",
            f"",
            f"Average doubling ratio: {average_doubling_ratio:.10f}",
            f" across runs 1 through {len(benchmark_data)}",
            f"",
        )

    if estimated_time_complexity == enumerations.TimeComplexity.notsure:
        console.print(
            f"[bold red]Unable to determine time complexity for {filename} -> {funcname} (average doubling ratio was {average_doubling_ratio}).[/bold red] [bold yellow]Perhaps try again?[/bold yellow]"
        )
    else:
        console.print(
            f"[bold green]Estimated time complexity for {filename} -> {funcname}: O({estimated_time_complexity})[/bold green]"
        )
