from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .individual_name import IndividualName


@dataclass
class Group:
    group_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupName",
            "type": "Element",
        }
    )
    individual_name: List[IndividualName] = field(
        default_factory=list,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "min_occurs": 1,
        }
    )
