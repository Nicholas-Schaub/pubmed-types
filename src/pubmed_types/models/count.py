from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Count:
    """
    <div> <h3>Count</h3> </div>
    """
    class Meta:
        name = "count"

    count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    count_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "count-type",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
