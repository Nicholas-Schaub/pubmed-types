from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .section import Section


@dataclass
class Sections:
    section: List[Section] = field(
        default_factory=list,
        metadata={
            "name": "Section",
            "type": "Element",
            "min_occurs": 1,
        }
    )
