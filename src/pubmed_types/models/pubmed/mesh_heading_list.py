from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .mesh_heading import MeshHeading


@dataclass
class MeshHeadingList:
    mesh_heading: List[MeshHeading] = field(
        default_factory=list,
        metadata={
            "name": "MeshHeading",
            "type": "Element",
            "min_occurs": 1,
        }
    )
