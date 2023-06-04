from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Pmid:
    class Meta:
        name = "PMID"

    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
