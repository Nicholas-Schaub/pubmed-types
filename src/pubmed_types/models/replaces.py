from dataclasses import field
from pydantic.dataclasses import dataclass
from .replaces_id_type import ReplacesIdType


@dataclass
class Replaces:
    id_type: ReplacesIdType = field(
        default=ReplacesIdType.PUBMED,
        metadata={
            "name": "IdType",
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
