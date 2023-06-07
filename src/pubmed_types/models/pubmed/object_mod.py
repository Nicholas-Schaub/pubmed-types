from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .param import Param


@dataclass
class Object:
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    param: List[Param] = field(
        default_factory=list,
        metadata={
            "name": "Param",
            "type": "Element",
        }
    )
