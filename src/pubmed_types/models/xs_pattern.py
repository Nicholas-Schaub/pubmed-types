from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class XsPattern:
    class Meta:
        name = "xs:pattern"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
