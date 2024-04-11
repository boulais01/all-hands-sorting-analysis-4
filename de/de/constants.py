"""Define constants with dataclasses."""

from dataclasses import dataclass
from de import enumerations
from typing import List, Tuple
from pathlib import Path

@dataclass(frozen=True)
class Constants:
    Min_Int_Value: int
    Max_Int_Value: int
    Min_Float_Value: float
    Max_Float_Value: float
    Min_String_Size: int
    Max_String_Size: int
    Benchmarkable_Functions_And_Data_Types: List[Tuple[Path, str, enumerations.ListData]]

constants = Constants(
    Min_Int_Value = -(1 << 32),
    Max_Int_Value = +(1 << 32),
    Min_Float_Value = float(-(1 << 32)),
    Max_Float_Value = float(+(1 << 32)),
    Min_String_Size = 1,
    Max_String_Size = 100,
    Benchmarkable_Functions_And_Data_Types = [
        (Path("tests/benchmarkable_functions.py"), "bubble_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "bubble_sort_str", enumerations.ListData.strings),
        (Path("tests/benchmarkable_functions.py"), "selection_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "insertion_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "heap_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "quick_sort", enumerations.ListData.ints),
        (Path("tests/benchmarkable_functions.py"), "merge_sort", enumerations.ListData.ints),
    ]
)
