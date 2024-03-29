"""Automatically generate data used for benchmarking."""

# TODO: Automatically generate data that will support the execution of a
# doubling experiment according to the strategy in the README.md file.

import random

from listmutator import approach, singlylinkedlist, doublylinkedlist
from typing import List, Union


def generate_list(listtype: approach.ListType, listdata: approach.ListData, size: int) -> Union[singlylinkedlist.LinkedList, doublylinkedlist.DoublyLinkedList]:
    """Generate a list of the given type and data type."""
    if listtype == approach.ListType.singlylinked:
        the_list = singlylinkedlist.LinkedList()
    if listtype == approach.ListType.doublylinked:
        the_list = doublylinkedlist.LinkedList()
    for i in range(size):
        # FIXME: no magic numbers
        the_list.addlast(random.randint(0, 10000))
    return the_list


def generate_lists_with_strategy(
    listtype: approach.ListType,
    listdata: approach.ListData,
    strategy: approach.BenchmarkStrategy,
    runs: int,
    startsize: int,
) -> List[Union[singlylinkedlist.LinkedList, doublylinkedlist.DoublyLinkedList]]:
    """Generate a list of lists, each with the given type and data type, according to the strategy."""
    if strategy == approach.BenchmarkStrategy.double:
        return [generate_list(listtype, listdata, size=(startsize * 2 ** i)) for i in range(runs)]
