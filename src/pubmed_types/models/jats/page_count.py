from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class PageCount:
    """
    <div> <h3>Page Count</h3> </div>
    """
    class Meta:
        name = "page-count"

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
