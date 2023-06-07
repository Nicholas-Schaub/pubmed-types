from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class PubDateNotAvailable:
    """
    <div> <h3>Date Not Available Flag</h3> </div>
    """
    class Meta:
        name = "pub-date-not-available"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
