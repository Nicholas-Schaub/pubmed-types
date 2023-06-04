from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .affiliation_info import AffiliationInfo
from .first_name import FirstName
from .identifier import Identifier


@dataclass
class IndividualName:
    first_name: Optional[FirstName] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "required": True,
        }
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Element",
            "required": True,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Element",
        }
    )
    affiliation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Affiliation",
            "type": "Element",
        }
    )
    affiliation_info: Optional[AffiliationInfo] = field(
        default=None,
        metadata={
            "name": "AffiliationInfo",
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
