from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Grant:
    grant_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrantID",
            "type": "Element",
        }
    )
    acronym: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acronym",
            "type": "Element",
        }
    )
    agency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
            "required": True,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )
