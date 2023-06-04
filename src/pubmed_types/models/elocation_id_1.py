from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .elocation_id_eid_type import ElocationIdEidType
from .elocation_id_valid_yn import ElocationIdValidYn


@dataclass
class ElocationId1:
    class Meta:
        name = "ELocationID"

    eid_type: Optional[ElocationIdEidType] = field(
        default=None,
        metadata={
            "name": "EIdType",
            "type": "Attribute",
            "required": True,
        }
    )
    valid_yn: ElocationIdValidYn = field(
        default=ElocationIdValidYn.Y,
        metadata={
            "name": "ValidYN",
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
