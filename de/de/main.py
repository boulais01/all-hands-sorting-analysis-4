"""Conduct experiments to evaluate performance of list concatenation."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console

from listmutator import approach, benchmark

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()

# TODO: Make sure that you implement all of the required functions in the other
# file that will ensure that these function(s) work correctly.


@cli.command()
def main(
    listtype: approach.ListType = typer.Option(
        approach.ListType.singlylinked,
    ),
    listdata: approach.ListData = typer.Option(
        approach.ListData.ints,
    ),
    strategy: approach.BenchmarkStrategy = typer.Option(
        approach.BenchmarkStrategy.double,
    ),
    operation: approach.BenchmarkOperation = typer.Option(
        approach.BenchmarkOperation.removefirst,
    ),
    startsize: int = typer.Option(1000),
    runs: int = typer.Option(10),
):
    """Evaluate the performance of list operations."""
    # display details about the configuration of the benchmarking tool
    console.print(
        "\n[bold red]Benchmarking Tool for List Operations[/bold red]\n"
    )
    console.print(f"Type of list: {listtype}")
    console.print(f"Data stored in list: {listdata}")
    console.print(f"Benchmarking strategy: {strategy}")
    console.print(f"Benchmarking operation: {operation}")
    console.print(f"Number of runs: {runs}\n")
    # perform the benchmarking operation
    benchmark_data = benchmark.benchmark(
        listtype, listdata, strategy, operation, startsize, runs
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
