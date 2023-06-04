from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .reference import Reference


@dataclass
class ReferenceList:
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
        }
    )
    reference_list: List["ReferenceList"] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceList",
            "type": "Element",
        }
    )
