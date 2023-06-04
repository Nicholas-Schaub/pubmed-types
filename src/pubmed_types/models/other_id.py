from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .other_id_source import OtherIdSource


@dataclass
class OtherId:
    class Meta:
        name = "OtherID"

    source: Optional[OtherIdSource] = field(
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
