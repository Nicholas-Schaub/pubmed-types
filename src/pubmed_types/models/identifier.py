from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Identifier:
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
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
