from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class DispFormula1:
    class Meta:
        name = "DispFormula"

    math: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
