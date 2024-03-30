"""Define constants with dataclasses."""

from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    Min_Int_Value: int
    Max_Int_Value: int
    Min_Float_Value: float
    Max_Float_Value: float
    Min_String_Size: int
    Max_String_Size: int

constants = Constants(
    Min_Int_Value = -(1 << 32),
    Max_Int_Value = +(1 << 32),
    Min_Float_Value = float(-(1 << 32)),
    Max_Float_Value = float(+(1 << 32)),
    Min_String_Size = 1,
    Max_String_Size = 100,
)
