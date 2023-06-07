from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List


@dataclass
class AccessionNumberList:
    accession_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AccessionNumber",
            "type": "Element",
            "min_occurs": 1,
        }
    )
