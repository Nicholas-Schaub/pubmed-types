from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .publisher_name import PublisherName


@dataclass
class Publisher:
    publisher_name: Optional[PublisherName] = field(
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
