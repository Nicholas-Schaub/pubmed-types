from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .investigator import Investigator


@dataclass
class InvestigatorList:
    investigator: List[Investigator] = field(
        default_factory=list,
        metadata={
            "name": "Investigator",
            "type": "Element",
            "min_occurs": 1,
        }
    )
