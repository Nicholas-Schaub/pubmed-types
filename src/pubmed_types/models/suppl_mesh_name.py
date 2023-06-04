from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .suppl_mesh_name_type import SupplMeshNameType


@dataclass
class SupplMeshName:
    type: Optional[SupplMeshNameType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    ui: Optional[str] = field(
        default=None,
        metadata={
            "name": "UI",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
