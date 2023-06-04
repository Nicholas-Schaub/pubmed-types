from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .affiliation import Affiliation
from .identifier import Identifier


@dataclass
class AffiliationInfo:
    affiliation: Optional[Affiliation] = field(
        default=None,
        metadata={
            "name": "Affiliation",
            "type": "Element",
            "required": True,
        }
    )
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "name": "Identifier",
            "type": "Element",
        }
    )
