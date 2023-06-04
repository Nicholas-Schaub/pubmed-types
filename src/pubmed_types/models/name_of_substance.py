from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class NameOfSubstance:
    ui: Optional[str] = field(
        default=None,
        metadata={
            "name": "UI",
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
