from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .affiliation_info import AffiliationInfo
from .author_equal_contrib import AuthorEqualContrib
from .author_valid_yn import AuthorValidYn
from .collective_name import CollectiveName
from .identifier import Identifier
from .suffix_1 import Suffix1


@dataclass
class Author:
    valid_yn: AuthorValidYn = field(
        default=AuthorValidYn.Y,
        metadata={
            "name": "ValidYN",
            "type": "Attribute",
            "required": True,
        }
    )
    equal_contrib: Optional[AuthorEqualContrib] = field(
        default=None,
        metadata={
            "name": "EqualContrib",
            "type": "Attribute",
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Element",
        }
    )
    fore_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForeName",
            "type": "Element",
        }
    )
    initials: Optional[str] = field(
        default=None,
        metadata={
            "name": "Initials",
            "type": "Element",
        }
    )
    suffix: Optional[Suffix1] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Element",
        }
    )
    collective_name: Optional[CollectiveName] = field(
        default=None,
        metadata={
            "name": "CollectiveName",
            "type": "Element",
        }
    )
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "name": "Identifier",
            "type": "Element",
        }
    )
    affiliation_info: List[AffiliationInfo] = field(
        default_factory=list,
        metadata={
            "name": "AffiliationInfo",
            "type": "Element",
        }
    )
