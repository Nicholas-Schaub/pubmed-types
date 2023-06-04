from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .group import Group


@dataclass
class GroupList:
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "min_occurs": 1,
        }
    )
