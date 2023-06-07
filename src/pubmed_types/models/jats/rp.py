from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional


@dataclass
class Rp:
    """
    <div> <h3>Ruby Parenthesis</h3> </div>
    """
    class Meta:
        name = "rp"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
