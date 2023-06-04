from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .issn_issn_type import IssnIssnType


@dataclass
class Issn1:
    class Meta:
        name = "ISSN"

    issn_type: Optional[IssnIssnType] = field(
        default=None,
        metadata={
            "name": "IssnType",
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
