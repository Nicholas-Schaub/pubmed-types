from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .location_label_type import LocationLabelType


@dataclass
class LocationLabel:
    type: Optional[LocationLabelType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
