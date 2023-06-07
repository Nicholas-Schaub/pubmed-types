from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .chemical import Chemical


@dataclass
class ChemicalList:
    chemical: List[Chemical] = field(
        default_factory=list,
        metadata={
            "name": "Chemical",
            "type": "Element",
            "min_occurs": 1,
        }
    )
