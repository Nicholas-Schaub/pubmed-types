from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .affiliation_info import AffiliationInfo
from .identifier import Identifier
from .investigator_valid_yn import InvestigatorValidYn
from .suffix_1 import Suffix1


@dataclass
class Investigator:
    valid_yn: InvestigatorValidYn = field(
        default=InvestigatorValidYn.Y,
        metadata={
            "name": "ValidYN",
            "type": "Attribute",
            "required": True,
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
