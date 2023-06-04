from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .publication_type import PublicationType


@dataclass
class PublicationTypeList:
    publication_type: List[PublicationType] = field(
        default_factory=list,
        metadata={
            "name": "PublicationType",
            "type": "Element",
            "min_occurs": 1,
        }
    )
