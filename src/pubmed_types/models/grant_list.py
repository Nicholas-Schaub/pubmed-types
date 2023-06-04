from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .grant import Grant
from .grant_list_complete_yn import GrantListCompleteYn


@dataclass
class GrantList:
    complete_yn: GrantListCompleteYn = field(
        default=GrantListCompleteYn.Y,
        metadata={
            "name": "CompleteYN",
            "type": "Attribute",
            "required": True,
        }
    )
    grant: List[Grant] = field(
        default_factory=list,
        metadata={
            "name": "Grant",
            "type": "Element",
            "min_occurs": 1,
        }
    )
