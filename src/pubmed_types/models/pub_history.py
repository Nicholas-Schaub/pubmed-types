from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .event import Event


@dataclass
class PubHistory:
    """
    <div> <h3>Publication History</h3> </div>
    """
    class Meta:
        name = "pub-history"

    event: List[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
