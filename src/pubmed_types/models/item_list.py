from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional


@dataclass
class ItemList:
    list_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListType",
            "type": "Attribute",
            "required": True,
        }
    )
    item: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "min_occurs": 1,
        }
    )
