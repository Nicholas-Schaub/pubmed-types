from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .pmid import Pmid


@dataclass
class DeleteDocument:
    pmid: List[Pmid] = field(
        default_factory=list,
        metadata={
            "name": "PMID",
            "type": "Element",
        }
    )
