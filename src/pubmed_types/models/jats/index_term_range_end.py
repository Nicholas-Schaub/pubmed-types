from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class IndexTermRangeEnd:
    """
    <div> <h3>Index Term Range End</h3> </div>
    """
    class Meta:
        name = "index-term-range-end"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
