from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .suppl_mesh_name import SupplMeshName


@dataclass
class SupplMeshList:
    suppl_mesh_name: List[SupplMeshName] = field(
        default_factory=list,
        metadata={
            "name": "SupplMeshName",
            "type": "Element",
            "min_occurs": 1,
        }
    )
