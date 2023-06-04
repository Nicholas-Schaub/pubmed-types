from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .descriptor_name import DescriptorName
from .qualifier_name import QualifierName


@dataclass
class MeshHeading:
    descriptor_name: Optional[DescriptorName] = field(
        default=None,
        metadata={
            "name": "DescriptorName",
            "type": "Element",
            "required": True,
        }
    )
    qualifier_name: List[QualifierName] = field(
        default_factory=list,
        metadata={
            "name": "QualifierName",
            "type": "Element",
        }
    )
