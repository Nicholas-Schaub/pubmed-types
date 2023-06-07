from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .author import Author
from .author_list_complete_yn import AuthorListCompleteYn
from .author_list_type import AuthorListType


@dataclass
class AuthorList:
    complete_yn: AuthorListCompleteYn = field(
        default=AuthorListCompleteYn.Y,
        metadata={
            "name": "CompleteYN",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[AuthorListType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "name": "Author",
            "type": "Element",
            "min_occurs": 1,
        }
    )
