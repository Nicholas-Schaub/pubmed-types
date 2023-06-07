from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Hr:
    """
    <div> <h3>Horizontal Rule</h3> </div>
    """
    class Meta:
        name = "hr"

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
