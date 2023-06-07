from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Break:
    """
    <div> <h3>Line Break</h3> </div>
    """
    class Meta:
        name = "break"

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
