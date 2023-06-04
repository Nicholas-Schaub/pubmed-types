from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .object_mod import Object


@dataclass
class ObjectList:
    object_value: List[Object] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
            "min_occurs": 1,
        }
    )
