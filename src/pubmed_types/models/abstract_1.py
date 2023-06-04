from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .abstract_text import AbstractText


@dataclass
class Abstract1:
    class Meta:
        name = "Abstract"

    abstract_text: List[AbstractText] = field(
        default_factory=list,
        metadata={
            "name": "AbstractText",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    copyright_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "CopyrightInformation",
            "type": "Element",
        }
    )
