from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class TableCount:
    """
    <div> <h3>Table Count</h3> </div>
    """
    class Meta:
        name = "table-count"

    count: Optional[str] = field(
        default=None,
        metadata={
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
