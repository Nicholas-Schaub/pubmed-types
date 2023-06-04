from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .name_of_substance import NameOfSubstance


@dataclass
class Chemical:
    registry_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistryNumber",
            "type": "Element",
            "required": True,
        }
    )
    name_of_substance: Optional[NameOfSubstance] = field(
        default=None,
        metadata={
            "name": "NameOfSubstance",
            "type": "Element",
            "required": True,
        }
    )
