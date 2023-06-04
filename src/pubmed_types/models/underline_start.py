from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class UnderlineStart:
    """
    <div> <h3>Underline Start</h3> </div>
    """
    class Meta:
        name = "underline-start"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
