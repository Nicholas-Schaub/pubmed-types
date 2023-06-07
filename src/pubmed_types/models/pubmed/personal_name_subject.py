from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .suffix import Suffix


@dataclass
class PersonalNameSubject:
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
    suffix: Optional[Suffix] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Element",
        }
    )
