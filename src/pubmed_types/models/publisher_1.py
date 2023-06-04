from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .publisher_name_1 import PublisherName1


@dataclass
class Publisher1:
    class Meta:
        name = "Publisher"

    publisher_name: Optional[PublisherName1] = field(
        default=None,
        metadata={
            "name": "PublisherName",
            "type": "Element",
            "required": True,
        }
    )
    publisher_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublisherLocation",
            "type": "Element",
        }
    )
