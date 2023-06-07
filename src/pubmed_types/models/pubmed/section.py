from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .location_label import LocationLabel
from .section_title import SectionTitle


@dataclass
class Section:
    location_label: Optional[LocationLabel] = field(
        default=None,
        metadata={
            "name": "LocationLabel",
            "type": "Element",
        }
    )
    section_title: Optional[SectionTitle] = field(
        default=None,
        metadata={
            "name": "SectionTitle",
            "type": "Element",
            "required": True,
        }
    )
    section: List["Section"] = field(
        default_factory=list,
        metadata={
            "name": "Section",
            "type": "Element",
        }
    )
